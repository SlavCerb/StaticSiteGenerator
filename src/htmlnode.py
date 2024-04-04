class HTMLNode:
    # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    # children - A list of HTMLNode objects representing the children of this node
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.props = props       
        self.children = children

    def to_html(self):
        # Child classes will override this method to render themselves as HTML.
        raise NotImplementedError()

    def props_to_html(self):
        # props_to_html(self) - This method should return a string that represents the HTML attributes of the node.
        # Then self.props_to_html() should return as an example:
        # href="https://www.google.com" target="_blank"
        proplist = []
        if self.props != None:
            proplist = list(self.props.keys())
            #print(proplist)
            for i in range(len(proplist)):
                #print(proplist[i])
                #print(self.props[proplist[i]])
                proplist[i]=f"{proplist[i]}=\"{self.props[proplist[i]]}\""
            #print(proplist)
            output = " ".join(proplist)
            #print(output)
            return output
        else:
            return None

    def __repr__(self):
        output = f"HTMLNode({self.tag}, {self.value}, {self.props}, {self.children})"
        return output

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node has no Value")

        output = ""
        if self.tag == None:
            output = self.value
        elif self.props != None:
            output = f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            output = f"<{self.tag}>{self.value}</{self.tag}>"

        return output

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag=tag, children=children)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent Node has no Tag")

        if self.children == False:
            raise ValueError("Parent Node has no Children")

        opener = f"<{self.tag}>"
        closer = f"</{self.tag}>"
        output = opener
        for child in self.children:
            output +=f"{child.to_html()}"

        output += closer
        return output