import endpoints

auth0_issuer = endpoints.Issuer(
    issuer='https://megan.auth0.com/',
    jwks_uri='https://megan.auth0.com/.well-known/jwks.json'
)

firebase_issuer = endpoints.Issuer(
    issuer='https://securetoken.google.com/megan-158015',
    jwks_uri='https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com'
)

api_collection = endpoints.api(
    name='megan',
    version='v1',
    api_key_required=False,
#    audiences={
#        'https://megan.auth0.com/': ['T8q5ftC6gqIpchpHWs7yfYoCMW4HHZDZ'],
#        'https://securetoken.google.com/megan-158015': ['https://securetoken.google.com/megan-158015'],
#    },
    allowed_client_ids=[
#        'T8q5ftC6gqIpchpHWs7yfYoCMW4HHZDZ',  # auth0
        'https://securetoken.google.com/megan-158015',  # firebase
    ],
    issuers={
#        'https://megan.auth0.com/': auth0_issuer,
        'https://securetoken.google.com/megan-158015': firebase_issuer,
    },
    auth_level=endpoints.AUTH_LEVEL.REQUIRED,
#    scopes=[endpoints.EMAIL_SCOPE]
)

