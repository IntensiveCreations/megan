from google.appengine.ext import ndb

class User(ndb.Model):
    """Models an individual User entry with username and date."""
    username = ndb.StringProperty()
    join_date = ndb.DateTimeProperty(auto_now_add=True)