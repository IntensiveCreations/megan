#!/usr/bin/env bash
( cd main && python lib/endpoints/endpointscfg.py get_swagger_spec --hostname localhost:8080 -o static/ user.api.UserCollectionApi user.api.UserItemApi)

