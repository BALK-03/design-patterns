import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from factory.python.applications import HTMLTextApplication

# Example test with HTML application - Closed for modification/Open for extenstion
html_app = HTMLTextApplication()
html_doc = html_app.create_document()
html_doc.open()