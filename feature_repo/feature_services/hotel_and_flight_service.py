from tecton import FeatureService

from feature_repo.features.on_demand.get_booking_url import get_booking_url
from feature_repo.features.on_demand.get_best_hotels import get_best_hotels

bet_metrics_feature_service = FeatureService(
    name="hotel_and_flight_service:v1",
    features=[get_booking_url,
              get_best_hotels
              ]
)