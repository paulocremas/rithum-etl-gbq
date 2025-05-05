import requests
from modules.configuration.config import ACCESS_TOKEN, CURRENT_ORDER


# Function to make an API request
def requestApi(endpoint=None, filter_params=None):
    """Reads orders from the ChannelAdvisor API."""
    # Set up the request headers with the access token
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN.ACCESS_TOKEN}"}
    # Use provided filter parameters or default to an empty dictionary
    params = filter_params if filter_params else {}
    try:
        # Make a GET request to the specified endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        # Raise an exception if the response contains an HTTP error
        response.raise_for_status()
        # Return the response content as JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Print an error message if the request fails
        print(f"Error reading orders: {e}")
        if response is not None:
            # Print additional details about the response if available
            print(f"Response status code: {response.status_code}")
            print(f"Response body: {response.text}")
        # Return None in case of an error
        return None


def extractDataFromApi(configObject):
    """Extracts data from an API using a configuration object."""
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
            )  # Process only the link without parameters

        processed_data.extend(extracted_data["value"])
        # Check if the response contains valid data
        if extracted_data.get("@odata.nextLink"):
            endpoint = extracted_data["@odata.nextLink"]
        else:
            break  # Exit the loop if no data is returned

    # Return the processed data
    return processed_data
