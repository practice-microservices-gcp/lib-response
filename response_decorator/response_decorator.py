import flask

def http_response(func):

    def flask_response(*args, **kwargs):
        response = func(*args, **kwargs)

        if (not hasattr(response, 'body')) or (not callable(response.body, 'to_json', None)):
            print('Error: The response is not serializable to JSON')
            raise Exception

        web_response = flask.Response(
            response.body.to_json(),
            status=response.status
        )

        web_response.headers['Content-Type'] = 'application/json'

        return web_response
    return flask_response