import requests
import sender_stand_request
import data
import configuration

def test_get_order_by_id():
    response2 = sender_stand_request.get_order_by_id()
    assert response2.status_code == 200



