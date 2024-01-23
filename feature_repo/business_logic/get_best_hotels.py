
def yelp_get_hotels(company_address, api_key):
    import json
    import time
    import urllib.request, urllib.error, urllib.parse

    API_KEY = api_key
    ADDRESS = company_address

    URL = "https://api.yelp.com/v3/businesses/search"
    PARAMS = {
        "term": "hotel",
        "location": ADDRESS,
        "sort_by": "rating",
        "limit": "3"
    }
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}"
    }

    encoded_params = urllib.parse.urlencode(PARAMS)
    request_url = f"{URL}?{encoded_params}"

    max_retries = 4  # Maximum number of retries
    retry_delay = 0.2  # Time delay (in seconds) between retries

    for attempt in range(max_retries):
        try:
            request = urllib.request.Request(request_url, headers=HEADERS)
            response = urllib.request.urlopen(request)
            response_data = response.read().decode("utf-8")
            data = json.loads(response_data)

            hotels = data["businesses"]
            #coffee_shop = data["businesses"][0]
            suggested_hotels = []
            for hotel in hotels:
                parsed_hotel_url = urllib.parse.urlparse(hotel['url'])
                clean_hotel_url = parsed_hotel_url.scheme + "://" + parsed_hotel_url.netloc + parsed_hotel_url.path
                suggested_hotels.append(f"{hotel['name']} located at {hotel['location']['address1']} "
                                        f"in {hotel['location']['city']}, {hotel['location']['state']}. "
                                        f"Average rating: {hotel['rating']} (based on {hotel['review_count']} reviews) "
                                        f"Yelp URL: {clean_hotel_url}")
            #name = coffee_shop["name"]
            #address = " ".join(coffee_shop["location"]["display_address"])
            return suggested_hotels
        except urllib.error.HTTPError as e:
            error_description = json.loads(e.read().decode('utf-8'))['error']['description']
            print(f"HTTPError: {e.code} - {e.reason}, Description: {error_description}")
        except urllib.error.URLError as e:
            print(f"URLError: {e.reason}")
        except Exception as e:
            print(f"Error: {str(e)}")

        # If an exception was caught and the loop hasn't ended yet, wait before retrying
        if attempt < max_retries - 1:
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print(f"Failed after {max_retries} attempts. Exiting.")

    return None
