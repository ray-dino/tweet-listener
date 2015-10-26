# Tweet Listener

Python script to capture tweets containing certain keywords.

## Installation

- run `sudo sh extensions.sh`
- run `pip install -requirements.txt`
- set environment variables
```
export TWITTER_CONSUMER_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export TWITTER_CONSUMER_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXX
export TWITTER_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export TWITTER_ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXXXXXXXXXX
export CASSANDRA_ADDRESS=XXX.X.X.X
export CASSANDRA_KEYSPACE=XXXXXXXX
export CQLENG_ALLOW_SCHEMA_MANAGEMENT=1
```
- run `python sync_db.py`

## Run

`python listen.py arg1 arg2 .. argN`
