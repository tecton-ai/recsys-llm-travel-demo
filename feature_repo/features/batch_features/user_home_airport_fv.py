from tecton import batch_feature_view, Aggregation, DeltaConfig
from datetime import datetime, timedelta
from tecton.types import Field, String, Timestamp

from feature_repo.entities import user
from feature_repo.data_sources.user_home_airport import user_home_airport_batch

@batch_feature_view(
    sources=[user_home_airport_batch],
    entities=[user],
    mode='pandas',
    online=True,
    offline=True,
    feature_start_time=datetime(2023,1, 1),
    batch_schedule=timedelta(days=1),
    offline_store = DeltaConfig(
                    time_partition_size=timedelta(days=1),
                    subdirectory_override=None),
    description='User home airport',
    timestamp_field='last_updated_timestamp',
    schema=[Field("user_id", String),
                            Field("home_airport_code", String),
                            Field("home_airport_name", String),
                            Field("last_updated_timestamp", Timestamp)]
)
def user_home_airport_fv(user_home_airport_batch):
    return user_home_airport_batch[['user_id', 'home_airport_code', 'home_airport_name', 'last_updated_timestamp']]
