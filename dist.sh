#!/usr/bin/env bash
sh build-api.sh

gcloud app deploy --no-promote main/


