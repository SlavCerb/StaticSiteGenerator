from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
        test_object = TextNode("This is a textnode", "bold", "https://www.boot.dev")
        print(test_object)

main()