from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal text"
    BOLD_TEXT = "Bold text"
    ITALIC_TEXT = "Italic text"
    CODE_TEXT = "Code text"
    LINKS = "Links"
    IMAGES = "Images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False

        if other.text == self.text and other.text_type == self.text_type and other.url == self.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    
