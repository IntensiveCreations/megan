from protorpc import message_types
from protorpc import messages
from protorpc import remote
import endpoints

from google.appengine.ext import ndb

from root_api import api_collection
from .models import User
from .messages import UserCreateRequest, UserResponse, UserListMessage, USER_RESOURCE, EchoResponse, ECHO_RESOURCE


@api_collection.api_class(resource_name='users')
class UserCollectionApi(remote.Service):
    @endpoints.method(
        USER_RESOURCE,
        UserResponse,
        path="users",
        http_method='POST')
    def post(self, request):

        new_user = User(username=request.username)
        new_user.put()

        new_user_message = UserResponse(username=new_user.username,
                                        join_date=new_user.join_date)

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
            user_message_list.append(UserResponse(username=user.username,
                                                  join_date=user.join_date))
        return UserListMessage(items=user_message_list)

