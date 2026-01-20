from enum import Enum
from typing import Optional
class TextType(Enum):
    TEXT = 'text (plain)'
    BOLD = '**Bold text**'
    ITALIC = '_Italic text_'
    CODE = 'Code text'
    LINKS = 'Links, in this format: [anchor text](url)'
    IMAGES = 'Images, in this format: ![alt text](url)'


class TextNode:
    def __init__(self, text:str, text_type:TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, TextNode):
            return False
        if self.text != value.text or self.text_type != value.text_type or self.url != value.url:
            return False
        return True
    
    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'