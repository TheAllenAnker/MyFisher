# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from . import web


@web.route('/book/search')
def search():
    return 'Search part'