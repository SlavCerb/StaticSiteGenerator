from htmlnode import HTMLNode, LeafNode, ParentNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.text_type_list = ["text", "bold", "italic", "code", "link", "image"]
    
    def __eq__(self, other):
        result = False
        if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
            result = True
        return result

    def __repr__(self):
        output = f"TextNode({self.text}, {self.text_type}, {self.url})"
        return output

    def text_node_to_html_node(self):
        if self.text_type not in self.text_type_list:
            raise Exception("Text Node Type NOT an approved Type")
        
        output = None
        if self.text_type == "text":
            output = LeafNode(None, self.text)
        
        elif self.text_type == "bold":
            output = LeafNode("b", self.text)

        elif self.text_type == "italic":
            output = HTMLNode("i", self.text)

        elif self.text_type == "code":
            output = HTMLNode("code", self.text)

        elif self.text_type == "link":
            output = HTMLNode("a", self.text, {"href": f"{self.url}"})

        elif self.text_type == "image":
            output = HTMLNode("img", "", {"src": f"{self.url}", "alt": f"{self.text}"})
        
        return output