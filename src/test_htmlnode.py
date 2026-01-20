import unittest
from htmlnode import HtmlNode
class TestTextNode(unittest.TestCase):
    def test_props_to_html_with_none(self):
        node = HtmlNode("div", "content", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_single_prop(self):
        node = HtmlNode("a", "link", None, {"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), " href = https://www.boot.dev")

    def test_props_to_html_with_multiple_props(self):
        node = HtmlNode("img", None, None, {"src": "image.jpg", "alt": "An image"})
        result = node.props_to_html()
        self.assertIn(" src = image.jpg", result)
        self.assertIn(" alt = An image", result)

if __name__ == '__main__':
    unittest.main()