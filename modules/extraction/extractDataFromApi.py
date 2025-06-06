import requests
from modules.configuration.authorizationConfig import ACCESS_TOKEN
from modules.configuration.ordersConfig import CURRENT_ORDER
from modules.authorization.refreshAccessToken import refreshAccessToken


"""
Make a request to API
"""


# Function to make an API request
def requestApi(endpoint=None, filter_params=None):
    """Reads orders from the ChannelAdvisor API."""
    # Use provided filter parameters or default to an empty dictionary
    params = filter_params if filter_params else {}
    # Make a GET request to the specified endpoint

    response = requests.get(endpoint, headers=ACCESS_TOKEN.ACCESS_TOKEN, params=params)
    if response.status_code != 200:
        refreshAccessToken()
        response = requests.get(
            endpoint, headers=ACCESS_TOKEN.ACCESS_TOKEN, params=params
        )
    # Return the response content as JSON
    return response.json()


"""
Extracts data from an API using a configuration object.
After that it handles pagination if the request has more than 
100 objects in its response.
"""


def extractDataFromApi(configObject):
    processed_data = []
    endpoint = (
        configObject.ENDPOINT.format(ORDER_ID=CURRENT_ORDER.ID)
        if CURRENT_ORDER.CREATING_ORDER
        else configObject.ENDPOINT
    )

    while endpoint:
        # Make the API request
        if (
            endpoint == configObject.ENDPOINT or CURRENT_ORDER.CREATING_ORDER
        ):  # Use parameters only for the initial request
            extracted_data = requestApi(
                endpoint,
                getattr(
                    configObject, "PARAMS", None
                ),  # Get parameters from the config object, if available
            )
        else:
            extracted_data = requestApi(
                endpoint
            )  # Process only the link without parameters, for pagination

        processed_data.extend(extracted_data["value"])
        # Check if the response contains a next page
        if extracted_data.get("@odata.nextLink"):
            endpoint = extracted_data["@odata.nextLink"]
        else:
            break  # Exit the loop pagination is found

    # Return the processed data
    return processed_data
