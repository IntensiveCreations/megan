import datetime
from itertools import chain

from google.appengine.api import search
from google.appengine.ext import ndb

from protorpc import remote

import endpoints
from common.api import BaseService, fields_to_optional
from root_api import api_collection
from .models import User
from .messages import *

import logging

log = logging.getLogger(__name__)


@api_collection.api_class(resource_name='users')
class UserCollectionApi(BaseService):

    @endpoints.method(
        path="users",
        http_method='GET',
        request_message=GetUsersMessage,
        response_message=User.ProtoCollection(User.RESPONSE_FIELDS)
    )
    def get(self, request):

        query_string = "distance(location, geopoint({}, {})) < {}".format(
            request.location.latitude,
            request.location.longitude,
            request.distance
        )
        log.info(query_string)

        query = search.Query(query_string=query_string)

        user_index = search.Index(name='user')
        results = user_index.search(query)

        ids = []

        for scored_document in results:
            log.error("doc_id:{}".format(scored_document.doc_id))
            ids.append(int(scored_document.doc_id))

        # objects = ndb.get_multi([ndb.Key(User, k) for k in ids])

        # user_list = User.query().order(-User.join_date)

        user_list = ndb.get_multi([ndb.Key(User, k) for k in ids])

        user_message_list = []

        for user in user_list:

            user_message_list.append(user.to_message())

        return user_message_list

    @User.method(
        path="users",
        http_method='POST',
        request_fields=User.REQUEST_FIELDS,
        response_fields=User.RESPONSE_FIELDS
    )
    def post(self, entity):
        user_key = entity.put()
        log.debug("user id is {}".format(user_key.id()))
        return entity


@api_collection.api_class(resource_name='user')
class UserItemApi(BaseService):
    @User.method(
        path="me",
        http_method='GET',
        response_fields=User.RESPONSE_FIELDS
    )
    def get(self, request):

        user = User.query().get()
        return user

    @endpoints.method(
        path="me",
        http_method='PATCH',
        request_message=fields_to_optional(User.ProtoModel(User.REQUEST_FIELDS)),
        response_message=User.ProtoModel(User.RESPONSE_FIELDS)
    )
    def patch(self, request):

        user_id = User.query().get().key.id()
        user_id_str = str(user_id)
        update_datetime = datetime.datetime.now()
        if request.location is not None:
            user_index = search.Index(name='user')

            log = logging.getLogger(__name__)
            log.error("user location is {},{}".format(request.location.latitude, request.location.longitude))

            geo_point = search.GeoPoint(request.location.latitude, request.location.longitude)

            user_document = search.Document(
                doc_id=user_id_str,
                fields=[search.DateField(name='datetime', value=update_datetime),
                        search.GeoField(name='location', value=geo_point)])

            user_index.put(user_document)

        @ndb.transactional
        def tx():
            user = User.get_by_id(user_id)
            User.from_message(request, user)
            user.last_online_datetime = update_datetime
            user.put()
            return user

        return tx()

