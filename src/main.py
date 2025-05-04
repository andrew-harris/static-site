from textnode import *
from htmlnode import *

def main():
        
    node = TextNode("This is a text node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    print(html_node)

if __name__=="__main__":
    main()
