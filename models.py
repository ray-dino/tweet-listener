from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Tweet(Model):
    id = columns.BigInt(primary_key=True)
    text = columns.Text()
    
    user_id = columns.BigInt()
    user_screen_name = columns.Text()
    user_name = columns.Text()
    
    geo_type = columns.Text()
    geo_coordinates = columns.List(value_type=columns.Float)

    created_at = columns.Text()
    raw_tweet = columns.Text()
