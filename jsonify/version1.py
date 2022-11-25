import json


def jsonify(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return json.dumps(res)
    return wrapper


@jsonify
def make_user(id, options):
    return {'id': id, 'live': False, 'options': options}
