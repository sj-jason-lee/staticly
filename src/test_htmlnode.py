import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode('a', 'this is a link', children=None, props={'href': 'https://boot.dev'})
    self.assertEqual(
      ' href="https://boot.dev"',
      node.props_to_html()
    )
  
  def test_values(self):
    node = HTMLNode('a', 'this is a link', children=None, props={'href': 'https://boot.dev'})
    self.assertEqual(
      node.tag,
      'a'
    )
    self.assertEqual(
      node.value,
      'this is a link'
    )
    self.assertEqual(
      node.children,
      None
    )
    self.assertEqual(
      node.props,
      {'href': 'https://boot.dev'}
    )

  def test_repr(self):
    node = HTMLNode('a', 'this is a link', children=None, props={'href': 'https://boot.dev'})
    self.assertEqual(
      "HTMLNode(a, this is a link, children: None, {'href': 'https://boot.dev'})",
      node.__repr__()
    )
  