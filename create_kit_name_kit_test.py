import pytest
import data
import sender_stand_request

@pytest.fixture(scope="session")
def session_headers():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    current_headers = data.headers_kits.copy()
    current_headers["Authorization"] = "Bearer " + auth_token
    return current_headers

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name, headers):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert_code_400(name, headers):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers)
    assert kit_response.status_code == 400

def negative_assert_without_name(headers):
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers)
    assert kit_response.status_code == 400


#prueba 1
def test_create_kit_1_letter_in_name_get_success_response(session_headers):
    positive_assert(data.name_with_one_letter, session_headers)

#prueba 2
def test_create_kit_511_letter_in_name_get_success_response(session_headers):
    positive_assert(data.name_with_511_letters, session_headers)

# #prueba 3
def test_create_user_0_letter_in_name_get_error_response(session_headers):
    negative_assert_code_400(data.name_in_blank, session_headers)

# #prueba 4
def test_create_user_512_letter_in_name_get_error_response(session_headers):
    negative_assert_code_400(data.name_with_512_letters, session_headers)

#prueba 5
def test_create_kit_has_special_symbol_in_name_get_success_response(session_headers):
    positive_assert(data.name_with_special_symbol, session_headers)

#prueba 6
def test_create_kit_has_space_in_name_get_success_response(session_headers):
    positive_assert(data.name_with_space, session_headers)

#prueba 7
def test_create_kit_has_number_in_name_get_success_response(session_headers):
    positive_assert(data.name_with_number_character, session_headers)

#prueba 8
def test_create_user_without_name_get_error_response(session_headers):
    negative_assert_without_name(session_headers)

#prueba 9
def test_create_user_has_number_in_name_get_error_response(session_headers):
    negative_assert_code_400(data.name_with_numbers, session_headers)