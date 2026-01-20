class HtmlNode:
    def __init__(self, tag:str | None = None, value:str | None = None, 
                 children:list["HtmlNode"] | None = None, props:dict | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = str()
        if self.props != None and len(self.props) > 0:
            for k in self.props:
                result += f' {k} = {self.props[k]}'
        return result
    
    def __repr__(self) -> str:
        return f'HtmlNode:({self.tag}, {self.value}, {self.props}, Children:{len(self.children)})'