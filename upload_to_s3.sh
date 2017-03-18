#!/bin/bash

if [ -z $TRAVIS ]
then
	echo "This is meant to be run by travis"
	exit 0
fi

source ~/virtualenv/python2.7/bin/activate

BUCKET="$1"
CACHE_TIME="$2"

aws s3 sync --exclude '*\.(bz2|gz|aac|flac|mp3|wma|gif|jpg|jpeg|png|avi|mov|mp4|webm|woff|woff2)$' --exclude='.webassets-cache' --metadata-directive  REPLACE --content-encoding=gzip --region=us-east-1 --cache-control "public, max-age=$CACHE_TIME" --delete output/ $BUCKET
# gzip_cache won't deal with these
aws s3 sync --include '*\.(bz2|gz|aac|flac|mp3|wma|gif|jpg|jpeg|png|avi|mov|mp4|webm|woff|woff2)$' --exclude='.webassets-cache' --metadata-directive  REPLACE --content-encoding='' --region=us-east-1 --cache-control "public, max-age=$CACHE_TIME" --delete output/ $BUCKET
