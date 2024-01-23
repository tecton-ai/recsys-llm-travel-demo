from tecton import batch_feature_view, DeltaConfig
from datetime import datetime, timedelta
from tecton.types import Float64, Field, Bool, String, Int64, Timestamp, Array

from feature_repo.data_sources.user_likes_batch import user_likes_batch
from feature_repo.entities import user

@batch_feature_view(
    sources=[user_likes_batch],
    entities=[user],
    mode='pandas',
    online=True,
    offline=True,
    feature_start_time=datetime(2023,1, 1),
    batch_schedule=timedelta(days=1),
    offline_store = DeltaConfig(
                    time_partition_size=timedelta(days=1),
                    subdirectory_override=None),
    description='User favorite activities on their profile',
    timestamp_field='last_updated_timestamp',
    schema=[Field("user_id", String),
                            Field("last_updated_timestamp", Timestamp),
                            Field("favorite_activity", Array(String))]
)
def user_likes_fv(user_likes_batch):
    return user_likes_batch[['user_id', 'favorite_activity', 'last_updated_timestamp']]