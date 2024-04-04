import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

fail_message = "TEST FAILED"
testnode1 = HTMLNode("a", "testlink", {"href": "https://www.google.com", "target": "_blank"}, None)
testnode2 = HTMLNode("a", "testlink", {"href": "https://www.google.com"}, None)
testnode3 = HTMLNode("a", "testlink")
node = HTMLNode("p", "test string", None, [testnode1, testnode2])
leafnode1 = LeafNode("p", "test string", None)
leafnode2 = LeafNode("a", "test link", {"href": "https://www.google.com"})
pnode1 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
pnode2 = ParentNode(
    "p",
    [
        pnode1,
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

class TestHTMLNode(unittest.TestCase):
    def test_nodes(self):
        print("\nNodes Test 1 - Start")
        print(f" - {node.__repr__()}")
        print(f" - {testnode1.props_to_html()}")
        print(f" - {testnode2.props_to_html()}")
        print(f" - {testnode3.props_to_html()}")
        print("Nodes Test 1 - End")

    def test_leafnodes(self):
        print("\nLeaf Nodes Test 1 - Start")
        print(f" - {leafnode1.to_html()}")
        print(f" - {leafnode2.to_html()}")
        print("Leaf Nodes Test 1 - End")

    def test_parentnodes(self):
        print("\nParent Nodes Test 1 - Start")
        print(f" - {pnode1.to_html()}")
        print("Parent Nodes Test 1 - End")

    def test_parentnodes2(self):
        print("\nParent Nodes Test 2 - Start")
        print(f" - {pnode2.to_html()}")
        print("Parent Nodes Test 2 - End")

if __name__ == "__main__":
    unittest.main()