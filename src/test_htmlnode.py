import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self): 
        node = HTMLNode(
            "div", 
            "Hello, world!", 
            None, 
            {"class": "greeting", "href": "boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(), 
            ' class="greeting" href="boot.dev"',
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self): 
        node = LeafNode(None, "Hello world!")
        self.assertEqual(node.to_html(), "Hello, wolrd!")

if __name__ == "__main__": 
    unittest.main()