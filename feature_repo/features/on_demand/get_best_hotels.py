from tecton import RequestSource, on_demand_feature_view
from tecton.types import String, Timestamp, Int64, Field, Array

from feature_repo.business_logic.get_best_hotels import yelp_get_hotels
from feature_repo.business_logic.tecton_secret import yelp_api_key

request_schema = [Field('recommendation_destination', String)]

transaction_request = RequestSource(schema=request_schema)

@on_demand_feature_view(
    sources=[transaction_request],
    mode='python',
    description="Top rated hotels at the recommended city to check out",
    schema = [Field('hotel_recommendations', Array(String))]
)
def get_best_hotels(transaction_request):
    city_lookup = transaction_request["recommendation_destination"]
    best_hotels = yelp_get_hotels(city_lookup, yelp_api_key)
    return {'hotel_recommendations': best_hotels}

