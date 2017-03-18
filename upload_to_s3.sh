#!/bin/bash

if [ -z $TRAVIS ]
then
	echo "This is meant to be run by travis"
	exit 0
fi

source ~/virtualenv/python2.7/bin/activate

BUCKET="$1"
CACHE_TIME="$2"

# gzip_cache won't deal with these
aws s3 sync --exclude '*' --include '*\.(bz2|gz|aac|flac|mp3|wma|gif|jpg|jpeg|png|avi|mov|mp4|webm|woff|woff2)$' --exclude='.webassets-cache' --region=us-east-1 --cache-control "public, max-age=$CACHE_TIME" output/ $BUCKET
# we don't specify --metadata-directive  REPLACE so it might just work
aws s3 sync --exclude='.webassets-cache' --content-encoding=gzip --region=us-east-1 --cache-control "public, max-age=$CACHE_TIME" output/ $BUCKET
