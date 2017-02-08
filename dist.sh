#!/usr/bin/env bash
sh build-api.sh || exit 1

gcloud service-management deploy main/static/meganv1openapi.json || exit 1
gcloud app deploy main/app.yaml || exit 1



