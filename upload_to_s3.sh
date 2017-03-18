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
aws s3 sync --exclude '*' --include='*.bz2' --include='*.gz' --include='*.aac' --include='*.flac' --include='*.mp3' --include='*.wma' --include='*.gif' --include='*.jpg' --include='*.jpeg' --include='*.png' --include='*.avi' --include='*.mov' --include='*.mp4' --include='*.webm' --include='*.woff' --include='*.woff2' --exclude='theme/.webassets-cache/' --metadata-directive REPLACE --content-encoding=gzip --region=us-east-1 --cache-control 'public, max-age=$CACHE_TIME' output/ $BUCKET
aws s3 sync --exclude='*.bz2' --exclude='*.gz' --exclude='*.aac' --exclude='*.flac' --exclude='*.mp3' --exclude='*.wma' --exclude='*.gif' --exclude='*.jpg' --exclude='*.jpeg' --exclude='*.png' --exclude='*.avi' --exclude='*.mov' --exclude='*.mp4' --exclude='*.webm' --exclude='*.woff' --exclude='*.woff2' --exclude='theme/.webassets-cache/' --metadata-directive REPLACE --content-encoding=identity --region=us-east-1 --cache-control 'public, max-age=$CACHE_TIME' output/ $BUCKET
