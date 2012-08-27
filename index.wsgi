import sae
import sys
import os

from todo import app 

application = sae.create_wsgi_app(app.wsgifunc())