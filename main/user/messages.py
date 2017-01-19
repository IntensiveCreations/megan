from protorpc import message_types
from protorpc import messages


class UserCreateRequest(messages.Message):
    nickname = messages.StringField(10, required=True)
    email = messages.StringField(20, required=True)
    phone = messages.StringField(30, required=True)
    birth_date = messages.StringField(40, required=True)


class GeoMessage(messages.Message):
    latitude = messages.FloatField(10, required=True)
    longitude = messages.FloatField(20, required=True)


class UserPatchRequest(messages.Message):
    nickname = messages.StringField(10, required=False)
    email = messages.StringField(20, required=False)
    phone = messages.StringField(30, required=False)
    birth_date = messages.StringField(40, required=False)
    gender = messages.StringField(50, required=False)
    is_strokee = messages.BooleanField(60, required=False)
    is_stroker = messages.BooleanField(70, required=False)
    email = messages.StringField(80, required=False)
    phone = messages.StringField(90, required=False)
    photo = messages.StringField(100, required=False)
    photo_thumbnail = messages.StringField(110, required=False)
    home_location = messages.StringField(120, required=False)
    description = messages.StringField(130, required=False)
    latex_allergy = messages.BooleanField(140, required=False)
    nest = messages.BooleanField(150, required=False)
    location = messages.MessageField(GeoMessage, 160, required=False)


class UserResponse(messages.Message):
    nickname = messages.StringField(10)
    join_date = message_types.DateTimeField(20)
    email = messages.StringField(30)
    phone = messages.StringField(40)
    birth_date = messages.StringField(50)
    gender = messages.StringField(60)
    is_strokee = messages.BooleanField(70)
    is_stroker = messages.BooleanField(80)
    email = messages.StringField(90)
    phone = messages.StringField(100)
    photo = messages.StringField(110)
    photo_thumbnail = messages.StringField(120)
    home_location = messages.StringField(130)
    description = messages.StringField(140)
    latex_allergy = messages.BooleanField(150)
    nest = messages.BooleanField(160)
    last_online_datetime = message_types.DateTimeField(170)


class UserListMessage(messages.Message):
    items = messages.MessageField(UserResponse, 1, repeated=True)

