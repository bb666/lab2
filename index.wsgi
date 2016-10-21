import sae
from lab2 import wsgi

application = sae.create_wsgi_app(wsgi.application)
