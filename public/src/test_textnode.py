import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_neq(self):
        node3 = TextNode("This is a node", TextType.ITALIC_TEXT)
        node4 = TextNode("This is a super node", TextType.BOLD_TEXT)
        self.assertNotEqual(node3, node4)

    def test_url(self):
        node5 = TextNode("This is a node", "https://www.boot.dev")
        self.assertNotEqual(node5, None)


if __name__ == "__main__":
    unittest.main()
