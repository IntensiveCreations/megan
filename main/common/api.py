import logging
import os

from firebase import default_app
from firebase_admin import auth
from protorpc import remote
from protorpc import messages


# hack to have PATCH request accepts optional fields
import endpoints
from user.models import User

log = logging.getLogger(__name__)


def fields_to_optional(message):
    message_fields = {}
    for field in message.all_fields():
        new_field_cls = field.__class__
        kwargs = {
            'required': False,
            'repeated': field.repeated,
            'default': field.default
        }

        message_fields[field.name] = new_field_cls(field.number, **kwargs)

    message_fields['__module__'] = ''
    message_class = type("Test",
                         (messages.Message,),
                         message_fields)
    return message_class


class BaseService(remote.Service):

    def get_current_user(self, request):
        http_header_authorization = os.getenv('HTTP_AUTHORIZATION')

        if http_header_authorization is None:
            log.info("HTTP_AUTHORIZATION not found")
            return None

        # TODO: Token is always verified on Firebase server. Need to cache the session
        decoded_token = auth.verify_id_token(http_header_authorization)
        user_id = decoded_token['uid']

        user = User.get_by_id(user_id)

        if user is None:
            return User.get_or_insert(user_id)
        else:
            return user
