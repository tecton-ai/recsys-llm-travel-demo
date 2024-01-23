from tecton import stream_feature_view, BatchTriggerType, Aggregation
from datetime import datetime, timedelta
from tecton.aggregation_functions import last
from tecton import DeltaConfig
from tecton.types import Field, Timestamp, String, Int64

from feature_repo.entities import user
from feature_repo.data_sources.user_search_stream import user_searches_eventsource

schema_definition = [
    Field(name="transaction_timestamp", dtype=Timestamp),
    Field(name="user_id", dtype=String),
    Field(name="departure_date", dtype=String),
    Field(name="return_date", dtype=String),
    Field(name="destination_name", dtype=String),
    Field(name="origin_name", dtype=String),
]

@stream_feature_view(
    source=user_searches_eventsource,
    entities=[user],
    mode='pandas',
    online=True,
    offline=True,
    schema = schema_definition,
    feature_start_time=datetime(2023,1,1),
    description='Return the last trip search made by a user on the platform, updated continuously',
    timestamp_field="transaction_timestamp",
    manual_trigger_backfill_end_time=datetime(2023,11,15),
    batch_trigger = BatchTriggerType.MANUAL,
    batch_schedule=timedelta(days=1),
    offline_store = DeltaConfig(
                    time_partition_size=timedelta(days=1),
                    subdirectory_override=None)
)
def user_flight_search_fv(user_searches_eventsource):
    user_searches_eventsource['departure_date'] = user_searches_eventsource['departure_date'].astype(str).str.split().str[0]
    user_searches_eventsource['return_date'] = user_searches_eventsource['return_date'].astype(str).str.split().str[0]
    return user_searches_eventsource