import sender_stand_request
import configuration


# функция получения трека заказа
def get_track():
    response = sender_stand_request.post_new_orders().json()["track"]
    return response


track = get_track()

# функкция меняет значение параметра в запросе


def get_url_track():
    current_track = configuration.TRACK.copy
    current_track["track"] = track
    return current_track


# функция для позитивной проверки
def positive_assert():
    new_track_orders = sender_stand_request.get_orders()
    assert new_track_orders.status_code == 201
