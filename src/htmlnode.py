
from typing import Optional


class HTMLNode:
    """
    HTMLNode class

    Attributes
    ----------
    tag: str
         String representing the HTML tag name
    value: str
         String representing the value of the HTML tag
    children: list[HTMLNode]
         List of HTMLNode objects representing the children of the this node
    props: dict[str, str]
         Dictionary of key-value pairs representing attributes of the HTML tag
    """

    def __init__(self, tag, value, children, props):
        self.tag: Optional[str] = tag
        self.value: Optional[str] = value
        self.children: Optional[list[HTMLNode]] = children
        self.props: Optional[dict[str, str]] = props

    def __repr__(self):
        # TODO
        pass

    def props_to_html(self):
        if self.props is None:
            return None
        full_string: str = ""
        for k, v in self.props.items():
            full_string += f" {k}={v}"
        return full_string
    
    def to_html(self):
        raise NotImplementedError