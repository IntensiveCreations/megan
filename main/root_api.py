import endpoints

#auth0_issuer = endpoints.Issuer(
#    issuer='https://megan.auth0.com/',
#    jwks_uri='https://megan.auth0.com/.well-known/jwks.json'
#)

#firebase_issuer = endpoints.Issuer(
#    issuer='https://securetoken.google.com/megan-158015',
#    jwks_uri='https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com'
#)
from endpoints import AUTH_LEVEL
from endpoints.api_config import ApiAuth

api_collection = endpoints.api(
    name='megan',
    version='v1',
    api_key_required=False,
#    issuers={'firebase': endpoints.Issuer(
#        'https://securetoken.google.com/megan-158015',
#        'https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com')},
#    audiences={'firebase': ['https://securetoken.google.com/megan-158015']},
#: ['https://securetoken.google.com/megan-158015'],
#    },
#    allowed_client_ids=[
 #       'https://securetoken.google.com/megan-158015',  # firebase
#        '*',
#    ],
#    issuers={
#        'https://securetoken.google.com/megan-158015': firebase_issuer,
#    },
#    scopes=[endpoints.EMAIL_SCOPE],
#    auth=ApiAuth()
#    auth_level=AUTH_LEVEL.REQUIRED
)

