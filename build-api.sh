#!/usr/bin/env bash
( cd main && python lib/endpoints/endpointscfg.py get_openapi_spec --hostname megan-158015.appspot.com -o static/ user.api.UserCollectionApi user.api.UserItemApi)  || exit 1
#( cd main && python lib/endpoints/endpointscfg.py get_openapi_spec --hostname localhost:8080 -o static/ user.api.UserCollectionApi user.api.UserItemApi)
gcloud endpoints services deploy main/static/meganv1openapi.json --project megan-158015 || exit 1
