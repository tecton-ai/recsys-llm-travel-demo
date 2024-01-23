from tecton import RequestSource, on_demand_feature_view
from tecton.types import String, Timestamp, Int64, Field

request_schema = [Field('recommendation_airport', String)]

from feature_repo.features.batch_features.user_home_airport_fv import user_home_airport_fv
from feature_repo.features.stream_features.user_flight_search_fv import  user_flight_search_fv

transaction_request = RequestSource(schema=request_schema)

@on_demand_feature_view(
    sources=[user_home_airport_fv, user_flight_search_fv, transaction_request],
    mode='python',
    description="Generates a flight booking link",
    schema = [Field('booking_url', String)]
)
def get_booking_url(user_home_airport_fv, user_flight_search_fv, transaction_request):
    home_airport = user_home_airport_fv["home_airport_code"]
    destination_airport = transaction_request['recommendation_airport']
    departure_date = str(user_flight_search_fv['departure_date'])
    return_date = str(user_flight_search_fv['return_date'])

    return {
        'booking_url': (f"https://www.kayak.com/flights/{home_airport}-{destination_airport}/{departure_date}/{return_date}?sort=bestflight_a")
    }