from protorpc import message_types
from protorpc import messages
from protorpc import remote
import endpoints

from google.appengine.ext import ndb

from .models import User
from .messages import UserCreateRequest, UserCreateResponse, UserListMessage

@endpoints.api(name='echo', version='v1')
class EchoApi(remote.Service):
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        USER_RESOURCE,
        # This method returns an Echo message.
        UserCreateResponse,
        path='createUser',
        http_method='POST',
        name='createUser')
    def create_user(self, request):

        new_user = User(username=request.username)
        new_user.put()

        new_user_message = UserCreateResponse(username=new_user.username,
                                              join_date=new_user.join_date)

        return new_user_message

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        message_types.VoidMessage,
        # This method returns an Echo message.
        UserList,
        path='users',
        http_method='GET',
        name='users')
    def users(self, request):

        user_list = User.query().order(-User.join_date)
        user_message_list = []

        for user in user_list:
            user_message_list.append(UserCreateResponse(username=user.username,
                                                        join_date=user.join_date))
        return UserList(items=user_message_list)

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        message_types.VoidMessage,
        # This method returns an Echo message.
        EchoResponse,
        path='echoGet',
        http_method='GET',
        name='echoGet')
    def echo_get(self, request):
        output_content = "Echo " * 2
        return EchoResponse(content=output_content)

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        ECHO_RESOURCE,
        # This method returns an Echo message.
        EchoResponse,
        path='echo',
        http_method='POST',
        name='echo')
    def echo(self, request):
        output_content = ' '.join([request.content] * request.n)
        return EchoResponse(content=output_content)

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        ECHO_RESOURCE,
        # This method returns an Echo message.
        EchoResponse,
        path='echo/{n}',
        http_method='POST',
        name='echo_path_parameter')
    def echo_path_parameter(self, request):
        output_content = ' '.join([request.content] * request.n)
        return EchoResponse(content=output_content)

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        message_types.VoidMessage,
        # This method returns an Echo message.
        EchoResponse,
        path='echo/getApiKey',
        http_method='GET',
        name='echo_api_key')
    def echo_api_key(self, request):
        return EchoResponse(content=request.get_unrecognized_field_info('key'))

    @endpoints.method(
        # This method takes an empty request body.
        message_types.VoidMessage,
        # This method returns an Echo message.
        EchoResponse,
        path='echo/getUserEmail',
        http_method='GET',
        # Require auth tokens to have the following scopes to access this API.
        scopes=[endpoints.EMAIL_SCOPE],
        # OAuth2 audiences allowed in incoming tokens.
        audiences=['your-oauth-client-id.com'])
    def get_user_email(self, request):
        user = endpoints.get_current_user()
        # If there's no user defined, the request was unauthenticated, so we
        # raise 401 Unauthorized.
        if not user:
            raise endpoints.UnauthorizedException
        return EchoResponse(content=user.email())
# [END echo_api]
