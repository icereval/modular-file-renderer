import os

try:
    from mfr import settings
except ImportError:
    settings = {}

config = settings.get('UNOCONV_EXTENSION_CONFIG', {})


ADDRESS = config.get('SERVER', os.environ.get('UNOCONV_PORT_2002_TCP_ADDR', '127.0.0.1'))
PORT = config.get('PORT', os.environ.get('UNOCONV_PORT_2002_TCP_PORT', '2002'))

SHARED_PATH = config.get('SHARED_PATH', '/tmp/mfrunoconvshared')

RENDER_MAP = config.get('RENDER_MAP', {
    '.ppt': {'doctype': 'presentation', 'format': 'pdf'},
    '.pptx': {'doctype': 'presentation', 'format': 'pdf'},
})