from htmlnode import HtmlNode
from functools import reduce
class LeafNode(HtmlNode):
    def __init__(self,value: str ,tag: str | None = None, props: dict | None = None) -> None:
        super().__init__(tag = tag, value = value, children = None, props = props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        html_result = list()
        html_result.append(f'<{self.tag}')
        if self.props != None and len(self.props) > 0:
            for k in self.props:
                html_result.append(f' {k}={self.props[k]}')
        html_result.append('>')
        html_result.append(self.value)
        html_result.append(f'</{self.tag}>')
        return reduce(lambda a,b: a + b, html_result)

    def __repr__(self) -> str:
        return f'HtmlNode:({self.tag}, {self.value}, {self.props})'

# node = LeafNode(tag="p", value="Hello, world!")
# print(node.to_html())