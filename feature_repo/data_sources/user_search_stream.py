from tecton import PushSource, FileConfig
from tecton.types import String, Int64, Timestamp, Field

input_schema = [
    Field(name="transaction_timestamp", dtype=Timestamp),
    Field(name="user_id", dtype=String),
    Field(name="departure_date", dtype=Timestamp),
    Field(name="return_date", dtype=Timestamp),
    Field(name="destination_name", dtype=String),
    Field(name="origin_name", dtype=String),
]

user_searches_eventsource = PushSource(
    name="user_searches_stream",
    schema=input_schema,
    batch_config=FileConfig(
            uri='s3://travel-data-public-demo/future_trip_searches.parquet',
            file_format='parquet',
            timestamp_field='transaction_timestamp'
    ),
    description="User flight searches stream"
)