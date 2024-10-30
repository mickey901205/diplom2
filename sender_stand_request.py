import configuration
import requests
import data
from data import order


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH,
                        json=body,
                        headers=data.headers)

def get_new_order_id():
    response = post_new_order(data.order)
    order_id = response.json()["track"]
    return order_id

def get_order_by_id():
    tack_id = get_new_order_id()
    return requests.get(configuration.URL_SERVICE + configuration.GER_ORDER + f"{tack_id}")




