#!/usr/bin/env bash
pip install --upgrade -t main/lib -r requirements-vendor.txt
ln -s $(pwd)/endpoints_proto_datastore/endpoints_proto_datastore main/lib/
