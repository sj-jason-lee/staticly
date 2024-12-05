import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):
  @unittest.expectedFailure
  def test_no_children(self):
    child_node = HTMLNode('a', 'this is a link', children=None, props={'href': 'https://boot.dev'})
    node = LeafNode('a', 'test value', children=[child_node], props=None)

  def test_to_html_no_props(self):
    node = LeafNode('a', 'this is a test value', props=None) 
    self.assertEqual(
      '<a>this is a test value</a>',
      node.to_html()
    )