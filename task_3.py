from pprint import pprint
import requests


def introspection_info(obj) -> list:
    result = {'type': type(obj), 'attributes': dir(obj), 'builtins': getattr(obj, '__builtins__'), 'name': getattr(obj, '__name__')}
    return result


my_req = requests
info = introspection_info(my_req)
pprint(info)
