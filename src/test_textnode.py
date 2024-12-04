import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
  
  def test_eq_func(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertTrue(node.__eq__(node2))

  def test_with_url(self):
    node = TextNode("This is a text node", TextType.BOLD, 'https://boot.dev')
    node2 = TextNode("This is a text node", TextType.BOLD, 'https://boot.dev')
    self.assertEqual(node, node2)

  def test_dif_texttype(self):
    node = TextNode("This is a text node", TextType.ITALIC)
    node2 = TextNode("This is a text node", TextType.ITALIC)
    self.assertEqual(node, node2)
  
  def test_dif_texttype_url(self):
    node = TextNode("This is a text node", TextType.ITALIC, 'https://boot.dev')
    node2 = TextNode("This is a text node", TextType.ITALIC, 'https://boot.dev')
    self.assertEqual(node, node2)

  def test_not_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALIC)
    self.assertNotEqual(node, node2)

  def test_repr(self):
    node = TextNode("This is a text node", TextType.TEXT, 'https://boot.dev')
    self.assertEqual(
      'TextNode(This is a text node, text, https://boot.dev)',
      node.__repr__()
    )

if __name__ == "__main__":
  unittest.main()