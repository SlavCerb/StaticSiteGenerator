class HTMLNode:
    # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    # children - A list of HTMLNode objects representing the children of this node
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

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
        output = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return output