class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        result = False
        if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
            result = True
        return result

    def __repr__(self):
        output = f"TextNode({self.text}, {self.text_type}, {self.url})"
        return output

    