from protorpc import message_types
from protorpc import messages
import endpoints

class EchoRequest(messages.Message):
    content = messages.StringField(1)


class EchoResponse(messages.Message):
    """A proto Message that contains a simple string field."""
    content = messages.StringField(1)


class UserCreateRequest(messages.Message):
    username = messages.StringField(1, required=True)


class UserResponse(messages.Message):
    username = messages.StringField(1)
    join_date = message_types.DateTimeField(2)


class UserListMessage(messages.Message):
    items = messages.MessageField(UserResponse, 1, repeated=True)


USER_RESOURCE = endpoints.ResourceContainer(
    UserCreateRequest)

ECHO_RESOURCE = endpoints.ResourceContainer(
    EchoRequest,
    n=messages.IntegerField(2, default=1))
