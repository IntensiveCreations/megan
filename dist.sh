#!/usr/bin/env bash
#sh build-api.sh || exit 1

#gcloud endpoints services deploy main/static/meganv1openapi.json || exit 1
gcloud app deploy main/app.yaml --project megan-158015 || exit 1



