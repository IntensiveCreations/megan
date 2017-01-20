#!/usr/bin/env bash
( cd main && python lib/endpoints/endpointscfg.py get_swagger_spec user.api.UserCollectionApi --hostname megan-api.endpoints.megan-production.cloud.google.com -o static/ )

