#!/usr/bin/env bash
pip install --upgrade -t main/lib -r requirements-vendor.txt
ln -fs $(pwd)/endpoints_proto_datastore/endpoints_proto_datastore main/lib/
