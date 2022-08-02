from flask import request
from flask import current_app

def main():
    current_app.logger.info("Received request")
    return "---HEADERS---\n%s\n--BODY--\n%s\n-----\n" % (
        request.headers,
        request.get_data(),
    )
