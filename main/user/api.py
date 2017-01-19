import datetime

from google.appengine.api import search
from google.appengine.ext import ndb

from protorpc import remote

import endpoints
from root_api import api_collection
from .models import User
from .messages import *

import logging


@api_collection.api_class(resource_name='users')
class UserCollectionApi(remote.Service):
    @endpoints.method(
        UserCreateRequest,
        UserResponse,
        path="users",
        http_method='POST')
    def post(self, request):

        new_user = User.from_message(request)
        user_key = new_user.put()
        log = logging.getLogger(__name__)
        log.error("user id is {}".format(user_key.id()))

        new_user_message = new_user.to_message()

        return new_user_message

    @endpoints.method(
        message_types.VoidMessage,
        UserListMessage,
        path="users",
        http_method='GET')
    def hello(self, request):

        user_list = User.query().order(-User.join_date)
        user_message_list = []

        for user in user_list:

            user_message_list.append(user.to_message())

        return UserListMessage(items=user_message_list)


@api_collection.api_class(resource_name='user')
class UserResourceApi(remote.Service):
    @endpoints.method(
        message_types.VoidMessage,
        UserResponse,
        path="me",
        http_method='GET')
    def post(self, request):

        user = User.get_by_id(5452478162141184)
        user_message = user.to_message()

        return user_message

    @endpoints.method(
        UserPatchRequest,
        UserResponse,
        path="me",
        http_method='PATCH')
    def patch(self, request):

        user_id = 5452478162141184
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

        return tx().to_message()

