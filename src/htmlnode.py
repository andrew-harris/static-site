import re

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        output = ""
        if self.props:  # This checks if self.props is not None and not empty
            for item in self.props:
             output += f' {item}="{self.props[item]}"'
        return output
    
    def __eq__(self, other):
    
        if not isinstance(other, HTMLNode):
            return False
            
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode {self.props}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")

        if self.tag is None:
            return str(self.value)
        else:
            props_str = self.props_to_html()
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        output = ""

        if self.tag is None:
            raise ValueError("Missing tag")
        
        if self.children is None:
            raise ValueError("Missing children value")
    
        for child in self.children:
            output += child.to_html()

        return f"<{self.tag}>{output}</{self.tag}>"

