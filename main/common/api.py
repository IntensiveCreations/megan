from protorpc import remote
from protorpc import messages


# hack to have PATCH request accepts optional fields
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
    pass
