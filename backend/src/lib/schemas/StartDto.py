from flask_restx import Namespace


class StartDto:
    api = Namespace("Start", description="Start app")