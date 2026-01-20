import unittest
from leafnode import LeafNode 

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_no_props(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="Plain text")
        self.assertEqual(node.to_html(), "Plain text")

    def test_to_html_with_tag_and_props(self):
        node = LeafNode(tag="a", value="Click me", props={"href": "https://www.boot.dev"})
        result = node.to_html()
        self.assertIn("<a", result)
        self.assertIn("href=https://www.boot.dev", result)
        self.assertIn(">Click me</a>", result)

    def test_to_html_raises_error_with_none_value(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == '__main__':
    unittest.main()