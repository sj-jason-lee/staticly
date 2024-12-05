from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag == None:
      raise ValueError("Invalid HTML: no tag")
    if self.children == None or len(self.children) == 0:
      raise ValueError("Invalid HTML: parent node requires children")

    return f"<{self.tag}{self.props_to_html()}>{"".join(list(map(lambda child: child.to_html(), self.children)))}</{self.tag}>"



