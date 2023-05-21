import configuration
import requests
import data


# функция создания нового заказа
def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.orders_body)


def get_orders():
    return requests.get(configuration.URL_SERVICE + configuration.TRACK,
                        params={"trask"})
