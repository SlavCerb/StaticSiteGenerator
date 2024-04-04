import unittest

from htmlnode import HTMLNode

fail_message = "TEST FAILED"
testnode1 = HTMLNode("a", "testlink", None, {"href": "https://www.google.com", "target": "_blank"})
testnode2 = HTMLNode("a", "testlink", None, {"href": "https://www.google.com"})
testnode3 = HTMLNode("a", "testlink")

class TestHTMLNode(unittest.TestCase):
    def test_nodes(self):
        print("\nNodes Test 1 - Start")
        node = HTMLNode("p", "test string", [testnode1, testnode2], None)
        print(f" - {node.__repr__()}")
        print(f" - {testnode1.props_to_html()}")
        print(f" - {testnode2.props_to_html()}")
        print(f" - {testnode3.props_to_html()}")
        print("Nodes Test 1 - End")

if __name__ == "__main__":
    unittest.main()