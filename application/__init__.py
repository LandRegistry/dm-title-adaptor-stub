import json
from flask import Flask, request
import os
import logging
from logger import logging_config

logging_config.setup_logging()
LOGGER = logging.getLogger(__name__)

LOGGER.info("Starting the server")


app = Flask(__name__, static_folder='static')


# Register routes after establishing the db prevents improperly loaded modules
# caused from circular imports
from .title.views import title_bp  # noqa


app.config.from_pyfile("config.py")
app.register_blueprint(title_bp)
app.url_map.strict_slashes = False


@app.route("/health")
def check_status():
    return json.dumps({
        "Status": "OK",
        "headers": str(request.headers),
        "commit": str(os.getenv("COMMIT", "LOCAL"))
    })
