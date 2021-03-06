import logging
from flask import Blueprint, jsonify
import json
import os


LOGGER = logging.getLogger(__name__)

title_bp = Blueprint('title', __name__,
                     template_folder='templates',
                     static_folder='static')


@title_bp.route('/titlenumber/<title_no>', methods=['GET'])
def get_deed(title_no):

    with open(os.getcwd() + '/application/title/data.json') as data_file:
        titles = json.load(data_file)
    try:
        result = titles[title_no]
    except:
        result = None

    if result is None:
        return  "Title does not exist"

    return result['response']
