import sender_stand_request
import data

def get_headers_kits(token):
    current_headers = data.headers_kits.copy()
    current_headers["Authorization"] = "Bearer " + token
    return current_headers

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name, token):
    headers_kits = get_headers_kits(token)
    kit_body = get_kit_body(name)
    print(headers_kits)
    print(kit_body)

    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers_kits)
    assert kit_response.status_code ==201
    assert kit_response.json()["name"] == name

def negative_assert_symbol(name, token):
    headers_kits = get_headers_kits(token)
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers_kits)
    assert kit_response.status_code == 400

def negative_assert_without_name(token):
    headers_kits = get_headers_kits(token)
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers_kits)
    assert kit_response.status_code == 400


#Prueba 1. Creación de un nuevo usuario o usuaria
#El parámetro "firstName" contiene dos caracteres
def test_create_kit_1_letter_in_name_get_success_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    positive_assert("a", auth_token)

#prueba 2
def test_create_kit_511_letter_in_name_get_success_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert(name, auth_token)

#prueba 3
def test_create_user_0_letter_in_name_get_error_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    name = ""
    negative_assert_symbol(name, auth_token)
#prueba 4
def test_create_user_512_letter_in_name_get_error_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert_symbol(name, auth_token)
#prueba 5
def test_create_kit_has_special_symbol_in_name_get_success_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    name = "\"№%@\","
    positive_assert(name, auth_token)

#prueba 6
def test_create_kit_has_space_in_name_get_success_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    name = "A Aaa"
    positive_assert(name, auth_token)

#prueba 7
def test_create_kit_has_number_in_name_get_success_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    name = "123"
    positive_assert(name, auth_token)

#prueba 8
def test_create_user_without_name_get_error_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    negative_assert_without_name(auth_token)

#prueba 9
def test_create_user_has_number_in_name_get_error_response():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    name = 123
    negative_assert_symbol(name, auth_token)


