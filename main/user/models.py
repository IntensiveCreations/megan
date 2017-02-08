from itertools import chain

from google.appengine.ext import ndb
from google.appengine.ext.ndb.model import Property

import dateutil.parser
from endpoints_proto_datastore.ndb.model import EndpointsAliasProperty
from endpoints_proto_datastore.utils import MessageFieldsSchema
from .messages import UserResponse
from endpoints_proto_datastore.ndb import EndpointsModel


class User(EndpointsModel):

    RW_MESSAGE_FIELDS_SCHEMA = (
        'nickname',
        'birth_date',
        'gender',
        'is_strokee',
        'is_stroker',
        'email',
        'phone',
        'home_location',
        'description',
        'is_latex_allergic',
        'has_nest',
    )

    RO_MESSAGE_FIELDS_SCHEMA = (
        'join_date',
        'calculated_field_test',
        'last_online_datetime'
    )

    WR_MESSAGE_FIELDS_SCHEMA = (
    )

    # do not show any fields by default
    _message_fields_schema = ()

    REQUEST_FIELDS = MessageFieldsSchema(
        list(chain(RW_MESSAGE_FIELDS_SCHEMA, RW_MESSAGE_FIELDS_SCHEMA)),
        name="UserRequestFields",
    )
    REQUEST_PATCH_FIELDS = MessageFieldsSchema(
        list(chain(RW_MESSAGE_FIELDS_SCHEMA, RW_MESSAGE_FIELDS_SCHEMA)),
        name="UserRequestPatchFields",
    )
    RESPONSE_FIELDS = MessageFieldsSchema(
        list(chain(RW_MESSAGE_FIELDS_SCHEMA, RO_MESSAGE_FIELDS_SCHEMA)),
        name="UserResponseFields",
    )

    """Models an individual User entry."""
    nickname = ndb.StringProperty(required=True, indexed=False, default="NoName")
    join_date = ndb.DateTimeProperty(required=True, indexed=True, auto_now_add=True)
    birth_date = ndb.DateProperty(required=False, indexed=False)
    gender = ndb.StringProperty(required=False, indexed=False)
    is_strokee = ndb.BooleanProperty(required=True, indexed=False, default=False)
    is_stroker = ndb.BooleanProperty(required=True, indexed=False, default=False)
    email = ndb.StringProperty(required=False, indexed=False)
    phone = ndb.StringProperty(required=False, indexed=False)
    photo = ndb.StringProperty(required=False, indexed=False)
    photo_thumbnail = ndb.StringProperty(required=False, indexed=False)
    home_location = ndb.StringProperty(required=False, indexed=False)
    description = ndb.StringProperty(required=False, indexed=False)
    is_latex_allergic = ndb.BooleanProperty(required=True, indexed=False, default=False)
    has_nest = ndb.BooleanProperty(required=True, indexed=False, default=False)
    last_online_datetime = ndb.DateTimeProperty(required=True, indexed=False, auto_now_add=True)

    @EndpointsAliasProperty()
    def calculated_field_test(self):
        return self.nickname + "yeah"

    def populate_non_null_value(self, ** kwds):
        cls = self.__class__
        for name, value in kwds.iteritems():
            prop = getattr(cls, name)  # Raises AttributeError for unknown properties.
            if not isinstance(prop, Property):
                raise TypeError('Cannot set non-property %s' % name)
            if value is not None:
                prop._set_value(self, value)

    def to_message(self):
        return UserResponse(
            nickname=self.nickname,
            join_date=self.join_date,
            email=self.email,
            phone=self.phone,
            birth_date=self.birth_date.isoformat(),
            gender=self.gender,
            is_strokee=self.is_strokee,
            is_stroker=self.is_stroker,
            photo=self.photo,
            photo_thumbnail=self.photo_thumbnail,
            home_location=self.home_location,
            description=self.description,
            latex_allergy=self.latex_allergy,
            nest=self.nest,
            last_online_datetime=self.last_online_datetime
        )

    @classmethod
    def from_message(cls, message, existing_user=None):

        if existing_user is None:
            return User(
                nickname=message.nickname,
                email=message.email,
                phone=message.phone,
                birth_date=dateutil.parser.parse(message.birth_date))
        else:
            return existing_user.populate_non_null_value(
                nickname=message.nickname,
                email=message.email,
                phone=message.phone,
                birth_date=None if message.birth_date is None else dateutil.parser.parse(message.birth_date),
                gender=message.gender,
                is_strokee=message.is_strokee,
                is_stroker=message.is_stroker,
                photo=message.photo,
                photo_thumbnail=message.photo_thumbnail,
                home_location=message.home_location,
                description=message.description,
                latex_allergy=message.latex_allergy,
                nest=message.nest
            )

