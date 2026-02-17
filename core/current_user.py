import threading

_user = threading.local()

def set_current_user(user):
    _user.value = user

def get_current_user():
    return getattr(_user, "value", None)