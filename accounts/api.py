import requests
import json
from decouple import config

class HemisApi:
    def user_data_json(self, username, password):
        login_url = 'https://student.samduuf.uz/rest/v1/auth/login'
        user_url = 'https://student.samduuf.uz/rest/v1/account/me'
        api_token = config("HEMIS_API_TOKEN")
        headers =  {
            "Authorization": f"Bearer {api_token}",
            "Content-Type":"application/json"
            }

        user = {
        "login": username,
        "password": password
        }
        user_response = requests.post(login_url, data=json.dumps(user), headers=headers)
        if user_response.json().get('success'):
            user_token = user_response.json().get('data').get('token')
        else:
            return 'error'
        
        
        if user_token == "error":
            return 'error'
        headers = {
            "Authorization": f"Bearer {user_token}",
            "Content-Type":"application/json"
        }

        response = requests.get(user_url, headers=headers)
        return response.json()