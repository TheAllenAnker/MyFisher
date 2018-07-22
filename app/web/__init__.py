# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from flask import Blueprint


web = Blueprint('web', __name__)


from . import main
from . import book