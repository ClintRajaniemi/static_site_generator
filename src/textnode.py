from enum import Enum


class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"


class TextNode:
    """
    Text node class

    Attributes
    -----------
    text: string
          Text content of the node
    text_type: TextType
               The type of text this node contains
    url: string
         The URL of the link or image, if the text is a link
    """

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Compare equality with another TextNode object

        Parameters
        ----------
        self: this instance of TextNode
        other: the TextNode instance to compare with self

        Returns
        -------
        bool
        """
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    