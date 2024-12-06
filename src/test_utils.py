import unittest
from textnode import TextNode, TextType
from utils import split_nodes_delimiter

class TestHTMLNode(unittest.TestCase):
  def test_split_node_delim(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT)
      ],
      new_nodes
    )