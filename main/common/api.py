from google.appengine.ext import ndb
from protorpc import remote
from protorpc import messages


# hack to have PATCH request accepts optional fields
import endpoints
from user.models import User


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

    @ndb.transactional
    def tx_create_or_get_user(self, user_id, extra):
        user = User.get_by_id(user_id)
        if user is None:
            user = User(id=user_id)
        return user

    def get_current_user(self):
        endpoints_user = endpoints.get_current_user()
        if endpoints_user is None:
            raise endpoints.ForbiddenException()

        user_id = endpoints_user.user_id()

        user = User.get_by_id(user_id)

        if user is None:
            return self.tx_create_or_get_user(user_id)
        else:
            return user
