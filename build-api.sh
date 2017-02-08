#!/usr/bin/env bash
( cd main && python lib/endpoints/endpointscfg.py get_swagger_spec --hostname megan.endpoints.megan-158015.cloud.goog -o static/ user.api.UserCollectionApi user.api.UserItemApi)

