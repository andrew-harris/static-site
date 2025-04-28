from enum import Enum

class text_type(Enum):
    NORMAL_TEXT = 'normal'
    BOLD_TEXT = 'bold'
    ITALIC_TEXT = 'italic'
    CODE_TEXT = 'code'
    LINK = 'link'
    IMAGES = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return self == other


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url}"



