import requests
import os
import base64

SERVER_URL = "https://api.zoom.us/v2"

ACCESS_TOKEN_URL = "https://zoom.us/oauth/token"

CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")

authorization_header_value = base64.b64encode(f"{CLIENT_ID}:{SECRET_ID}".encode("utf-8")).decode(encoding="utf-8")

ACCESS_HEADER = {
    "Content-Type" : "application/x-www-form-urlencoded",
    "Authorization": f"Basic {authorization_header_value}"
}

ACCESS_URL_PARAMETERS = {
    "grant_type" : "account_credentials",
    "account_id" : os.environ.get("ACCOUNT_ID")
}


def get_access_token():
    """
    Returns the access token of the user
    """
    access_token_response = requests.post(ACCESS_TOKEN_URL, data = ACCESS_URL_PARAMETERS, headers = ACCESS_HEADER)

    if access_token_response.status_code == 200:
        access_token = access_token_response.json()["access_token"]
        print(f"Access Token: {access_token}")
    else:
        print(access_token_response.url)
        print("Failed to obtain access token.")


def get_all_recordings(userId):
    """
    Gets all recordings from the user account
    
    Parameter userId: is an integer representing the user id
    """
    recordings_url = SERVER_URL + f"/users/{userId}/recordings"
    response = requests.get(recordings_url)
    if response.status_code == 200:
        return response.json()['meetings'] 
    else:
        print("Failed to get recordings")

get_access_token()

# curl -X POST https://zoom.us/oauth/token -d 'grant_type=account_credentials' -d 'account_id={accountID}' -H 'Host: zoom.us' -H 'Authorization: Basic Base64Encoded(clientId:clientSecret)'
# curl -X POST https://zoom.us/oauth/token -d 'grant_type=account_credentials' -d 'account_id=5yiPLwmTTpQVBnMxOlf32q' -H 'Host: zoom.us' -H 'Authorization: Basic aGwbwxOgK6eGHEO0W1DOCv5WCODeVxoet7DFEON7bR23gP5qEW7cmeWCbCEO3ApBEWlRwCVpDWB=='