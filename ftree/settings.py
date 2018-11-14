import os


ENCODING = 'utf-8'

MAX_SIZE = 1024 * 1024
MAX_CHILDREN = 50
MAX_DEPTH = 20

LOAD_FILE_HASHES = os.path.join(os.path.expanduser('~'), '.ftreeloadhashes')
