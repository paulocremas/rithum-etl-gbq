## Rithum API to Google BigQuery ETL

This ETL process was developed as commissioned by ChannelFront LLC. It extracts order data (items and distribution details) from the Rithum API for Looker visualization.

---
### Summary

1. [Configuration](#config)
2. [Authorization](#auth)
3. [APP.py](#app)
4. [Extraction](#extract)
5. [Transform](#transform)
6. [Load](#load)
7. [E-mail](#load)

---
<a id="config"></a>
### [Configuration Modules](https://github.com/paulocremas/rithum-etl-gbq/tree/main/modules/configuration)
#### [authorizationConfig.py](https://github.com/paulocremas/rithum-etl-gbq/blob/main/modules/configuration/authorizationConfig.py)
This module contains 3 classes:
1. APIConfig class, which holds essential credentials for accessing the ChannelAdvisor API. It is instantiated immediately upon import and provides configuration for other modules
   * CLIENT_ID: Your application's unique identifier obtained from the Developer Console after OAuth 2.0 registration
   * CLIENT_SECRET: The secret password generated for your application within the Developer Console
   * REFRESH_TOKEN: A long-lived token, also generated in the Developer Console, used to obtain short-lived access tokens for API requests
   * ENDPOINT: The URL for the ChannelAdvisor access token endpoint
     
2. The AccessToken class is a simple container for storing API access token details. It is instantiated immediately as ACCESS_TOKEN
   * ACCESS_TOKEN: The temporary access token used to authenticate API requests
   * EXPIRES_IN: The remaining lifetime (in seconds) of the current ACCESS_TOKEN
  
3. This class configures the OAuth2
   * ENDPOINT: The URL for the ChannelAdvisor OAuth2 endpoint
   * REDIRECT_URI: Used to set the waypoint for authorization


#### [ordersConfig.py](https://github.com/paulocremas/rithum-etl-gbq/blob/main/modules/configuration/ordersConfig.py)
This module contains 8 classes and 1 function:

1. DistributionCenters - Manages distribution center names, accessible by their ID (it is instantiated immediately upon import)
    *  ENDPOINT: The URL for the ChannelAdvisor distribution centers API endpoint
    *  PARAMS: Specifies the fields to be extracted on the API request
    *  DISTRIBUTION_CENTERS_DICT: Stores the mapping of distribution center IDs (keys) to their names (values)

3. BigQueryConfig (it is instantiated immediately upon import)
    * TABLE_ID: Configuration settings for interacting with Google BigQuery
    * GOOGLE_APPLICATION_CREDENTIALS: The path to the Google Cloud service account credentials file
    * CLIENT: An initialized BigQuery client object

4. OrdersApiCall (it is instantiated immediately upon import)
    * ENDPOINT: The URL for the ChannelAdvisor orders API endpoint
    * PARAMS: Receives extraction date parameters (via the SetOrdersApiParams function)

5. Function SetOrdersApiParams
    * Consults the last order date by querying BigQuery
    * Sets the API request parameters to retrieve orders from one second after the last order date up to the current time.
   
7. Fulfillments: in this API call you can find the distribution center ID of the item requested (it is instantiated immediately upon import)
    * ENDPOINT: The URL for the ChannelAdvisor Fulfillments API endpoint
    * PARAMS: Specifies the fields to be extracted on the API request

8. ItemInOrder: Used to request item data from each order (it is instantiated immediately upon import)
    * ENDPOINT: The URL for the ChannelAdvisor Items in Order API endpoint. It must be filled with an order ID
    * PARAMS: Specifies the fields to be extracted on the API request 

9. CurrentOrder 
    * ID: Stores the current Order ID to consult it
    * CREATE_DATE_UTC: Stores the current Order ID to insertt it into the item class
    * CREATING_ORDER: The scripts uses this bool as a switch to know when a request is currently dealing with an order

10. Item: This class serves as a blueprint for creating items destined for BigQuery. Its variables directly correspond to the fields in the BigQuery database table.

11. DataToInsert: It's list of item's as dicts to be inserted as dataframe (it is instantiated immediately upon import)
---

<a id="auth"></a>
### [Authorization Modules](https://github.com/paulocremas/rithum-etl-gbq/tree/main/modules/authorization)
#### [refreshAccessToken.py](https://github.com/paulocremas/rithum-etl-gbq/blob/main/modules/authorization/firstAuth.py)
This module grants access to your Developer Console Application (must have a single waypoint configured on authorizationConfig 3rd class and in Dev Console App)
  * get_authorization_url(): creates a custom url for authorization
  * open_browser_for_authorization(authorization_url): Opens the user's browser to the authorization URL
It's used only on the first login.

#### [refreshAccessToken.py](https://github.com/paulocremas/rithum-etl-gbq/blob/main/modules/authorization/refreshAccessToken.py)
This module refreshes the access token using the "REFRESH_TOKEN" globally, allowing the script to make requests on the API
