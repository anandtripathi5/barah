# utils.py
import uuid
import logging
import flask

original_log_id = ''
log_id = ''

# Generate a new request ID, optionally including an original request ID

def _generate_request_id(original_id=''):
    new_id = uuid.uuid4()
    if original_id:
        new_id = "{},{}".format(original_id, new_id)

    return new_id

# Returns the current request ID or a new one if there is none
# In order of preference:
#   * If we've already created a request ID and stored it in the flask.g context local, use that
#   * If a client has passed in the X-Request-Id header, create a new ID with that prepended
#   * Otherwise, generate a request ID and store it in flask.g.request_id


def request_id():
    global log_id
    global original_log_id

    if flask.has_request_context():
        if log_id is not None and log_id != '' and getattr(flask.g, 'request_id', None) == log_id:
           return log_id
        headers = flask.request.headers
        original_log_id = headers.get("X-Request-Id")
        new_uuid = _generate_request_id(original_log_id)
        flask.g.request_id = new_uuid
        log_id = new_uuid

    if not log_id:
        new_uuid = _generate_request_id()
        log_id = new_uuid

    return log_id


class RequestIdFilter(logging.Filter):
    # This is a logging filter that makes the request ID available for use in
    # the logging format. Note that we're checking if we're in a request
    # context, as we may want to log things before Flask is fully loaded.
    def filter(self, record):
        if flask.has_request_context():
            record.request_id = request_id()
        else:
            record.request_id = request_id()
        return True