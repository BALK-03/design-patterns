import os, sys
from abc import ABC, abstractmethod

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from factory.python.documents import TextDocument, RichTextDocument, HTMLDocument

class Application(ABC):
    def open_document(self):
        doc = self.create_document()
        doc.open()
        return doc

    @abstractmethod
    def create_document(self):
        pass


class TextApplication(Application):
    def create_document(self):
        return TextDocument()
    

class RichTextApplication(Application):
    def create_document(self):
        return RichTextDocument()
    

class HTMLTextApplication(Application):
    def create_document(self):
        return HTMLDocument()
