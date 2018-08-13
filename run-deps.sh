#!/usr/bin/env bash
pip install --upgrade -t main/lib -r requirements-vendor.txt
ln -s $(pwd)/endpoints-proto-datastore/endpoints_proto_datastore/ main/lib/

mkdir -p ide-libs
GOOGLE_APPENGINE_SDK="/c/sdks/Cloud SDK/google-cloud-sdk/platform/google_appengine/"
ln -s "${GOOGLE_APPENGINE_SDK}/google" ide-libs/


