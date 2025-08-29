from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass


class TextDocument(Document):
    def open(self):
        print("Opening a plain text document.")

    def save(self):
        print("Saving a plain text document.")


class RichTextDocument(Document):
    def open(self):
        print("Opening a rich text document.")

    def save(self):
        print("Saving a rich text document.")


class HTMLDocument(Document):
    def open(self):
        print("Opening a HTML text document.")

    def save(self):
        print("Saving a HTML text document.")
