import json
import requests

_url = 'https://reqres.in/'
email = 'eve.holt@reqres.in'
password = 'pistol'
password_two = 'cityslicka'


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}



def post_request_api_register_successful():
    """Method to do a POST request to the API for REGISTER - SUCCESSFUL"""

    data = {
        'email': email,
        'password': password
    }

    loc_url = _url + 'api/prregister'

    try:
        response = requests.post(url=loc_url, data=json.dumps(data), headers=headers)

        # Check the response, and if it's not 2xx we will consider it an error
        if not response.status_code // 100 == 2:
            print('Error: Unexpected response {}'.format(response))
            fail_status = response.status_code
            body_json = 'none'
            return fail_status, body_json
        else:
            success_status = response.status_code
            body_json = json.loads(json.dumps(response.json()))
            id_response = body_json['id']
            token_response = body_json['token']
            return success_status, id_response, token_response
    except requests.exceptions.RequestException as e:
        # A serious failure like an SSLError or Invalid URL
        print('Exception Error: {}'.format(e))


def post_request_api_login_successful():
    """Method to do a POST request to the API for LOGIN - SUCCESSFUL"""

    data = {
        'email': email,
        'password': password_two
    }

    loc_url = _url + 'api/login'

    try:
        response = requests.post(url=loc_url, data=json.dumps(data), headers=headers)

        # Check the response, and if it's not 2xx we will consider it an error
        if not response.status_code // 100 == 2:
            print('Error: Unexpected response {}'.format(response))
            fail_status = response.status_code
            body_json = 'none'
            print(fail_status, body_json)
            return fail_status, body_json
        else:
            success_status = response.status_code
            body_json = json.loads(json.dumps(response.json()))
            token_response = body_json['token']
            return success_status, token_response
    except requests.exceptions.RequestException as e:
        # A serious failure like an SSLError or Invalid URL
        print('Exception Error: {}'.format(e))


def get_request_api_list_resource():
    """Method to do a GET request to the API for listing details of a resource """

    loc_url = _url + 'api/unknown/3'

    try:
        response = requests.get(url=loc_url, headers=headers)

        # Check the response, and if it's not 2xx we will consider it an error
        if not response.status_code // 100 == 2:
            print('Error: Unexpected response {}'.format(response))
            fail_status = response.status_code
            body_json = 'none'
            print(fail_status, body_json)
            return fail_status, body_json
        else:
            success_status = response.status_code
            id_from_json = json.loads(json.dumps(response.json()))['data']['id']
            return success_status, id_from_json
    except requests.exceptions.RequestException as e:
        # A serious failure like an SSLError or Invalid URL
        print('Exception Error: {}'.format(e))
