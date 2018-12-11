#!/usr/bin/env bash
set -ex

cd infrastructure
docker build -t deploy .
docker run deploy