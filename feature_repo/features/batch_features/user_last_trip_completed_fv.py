from tecton import batch_feature_view, Aggregation, FilteredSource, DeltaConfig
from tecton.aggregation_functions import last
from datetime import datetime, timedelta
from tecton.types import Field, String, Timestamp

from feature_repo.entities import user
from feature_repo.data_sources.user_historic_trips import user_historic_trips_batch

@batch_feature_view(
    sources=[FilteredSource(user_historic_trips_batch)],
    entities=[user],
    mode='pandas',
    online=True,
    offline=True,
    feature_start_time=datetime(2023,1, 1),
    batch_schedule=timedelta(days=1),
    offline_store = DeltaConfig(
                    time_partition_size=timedelta(days=1),
                    subdirectory_override=None),
    description='Last 5 trips the user completed in the last 365 days',
    timestamp_field='return_date', #notice we set the timestamp to the return date; that is the trip completion date
    schema=[Field("user_id", String),
                            Field("destination_name", String),
                            Field("return_date", Timestamp)],
    aggregation_interval=timedelta(days=1),
    aggregations = [Aggregation(column="destination_name", function=last(5), time_window=timedelta(days=365))]
)

def user_last_trip_completed_fv(user_historic_trips_batch):
    return user_historic_trips_batch[['user_id', 'destination_name', 'return_date']]