from tecton import FeatureService

from feature_repo.features.batch_features.user_last_trip_completed_fv import user_last_trip_completed_fv
from feature_repo.features.batch_features.user_home_airport_fv import user_home_airport_fv
from feature_repo.features.batch_features.user_likes_fv import user_likes_fv
from feature_repo.features.stream_features.user_flight_search_fv import user_flight_search_fv

user_feature_service = FeatureService(
    name="user_service:v1",
    features=[user_last_trip_completed_fv,
              user_home_airport_fv,
              user_likes_fv,
              user_flight_search_fv]
)