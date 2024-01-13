import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=auth_token)


response = post_new_user(data.user_body)
token = "Bearer " + response.json()["authToken"]

print(response.status_code)
print(token)
headers_kits = {
    "Content-Type": "application/json",
    "Authorization": token
}
response2 = post_new_client_kit(data.kit_body, headers_kits)
print(response2.status_code)
print(response2.json())
