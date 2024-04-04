import unittest

from textnode import TextNode

fail_message = "TEST FAILED"

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        print("\nEquality Test 1 - Start")
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2, fail_message)
        print("Equality Test 1 - End")
    
    def test_eq2(self):
        print("\nEquality Test 2 - Start")
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(node, node2, fail_message)
        print("Equality Test 2 - End")

    def test_noteq1(self):
        print("\nInequality Test 1 - Start")
        node = TextNode("This is a text poop", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2, fail_message)
        print("Inequality Test 1 - End")

    def test_noteq2(self):
        print("\nInequality Test 2 - Start")
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2, fail_message)
        print("Inequality Test 2 - End")

    def test_noteq3(self):
        print("\nInequality Test 3 - Start")
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2, fail_message)
        print("Inequality Test 3 - End")

    def test_urlnone(self):
        print("\nURL None Test 1 - Start")
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2, fail_message)
        print("URL None Test 1 - End")

    def test_typenoteq1(self):
        print("\nType Inequality Test 1 - Start")
        node = TextNode("This is a text node", "bold")
        node2 = TextNode(34, "bold")
        self.assertNotEqual(node, node2, fail_message)
        print("Type Inequality Test 1 - End")

    def test_typenoteq2(self):
        print("\nType Inequality Test 2 - Start")
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", 34.56)
        self.assertNotEqual(node, node2, fail_message)
        print("Type Inequality Test 2 - End")

    def test_typenoteq3(self):
        print("\nType Inequality Test 3 - Start")
        node = TextNode("This is a text node", "bold", True)
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2, fail_message)
        print("Type Inequality Test 3 - End")

if __name__ == "__main__":
    unittest.main()

