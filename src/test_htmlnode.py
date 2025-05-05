import unittest

from htmlnode import *
from additional_functions import *

class test_htmlnode(unittest.TestCase):
    def test_eq(self):
        test_prop1={
            "href": "https://www.google.com",
            "target": "_blank",
            }

        test_prop2={
            "href": "https://www.bbc.com",
            "target": "_notblank",
            }

        test_prop3={
            "href": "https://www.google.com",
            "target": "_self",
            }
        
        test_prop4={
            "href": "https://www.google.com",
            "target": "_blank",
            }

        node = HTMLNode("testtag", "50", "child1", test_prop1)
        node2 = HTMLNode("testtag", "50", "child1", test_prop4)
        self.assertEqual(node, node2)

        node = HTMLNode("testtag", "50", "child1", test_prop1)
        node2 = HTMLNode("testtag", "50", "child1", test_prop2)
        self.assertNotEqual(node, node2)

        node = HTMLNode("testtag", "50", "child1", test_prop1)
        node2 = HTMLNode("testtag", "50", "child1", test_prop3)
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_to_html_with_greatgranchildren(self):
        greatgrandchild_node = LeafNode("b", "great grandchild")
        grandchild_node = ParentNode("i", [greatgrandchild_node])
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("span", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<span><div><i><b>great grandchild</b></i></div></span>",
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [web link](https://weblink.example)"
        )
        self.assertListEqual([("web link", "https://weblink.example")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

        node = TextNode(
            "Lets try another test ![image](https://i.imgur.com/zjjcJKZ.png) with a link [web link](https://weblink.example) and another image ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        new_nodes = split_nodes_link(new_nodes)

        for node in new_nodes:
            print(f"Text: '{node.text}', Type: {node.text_type}, URL: {node.url}")

        print("\nExpected nodes:")
        expected = [
            TextNode("Lets try another test ", TextType.TEXT),  # One space
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" with a link ", TextType.TEXT),
            TextNode("web link", TextType.LINK, "https://weblink.example"),
            TextNode(" and another image ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        for node in expected:
            print(f"Text: '{node.text}', Type: {node.text_type}, URL: {node.url}")

'''
        self.assertListEqual(
            [
                TextNode("Lets try another test ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" with a link ", TextType.TEXT),
                TextNode("web link", TextType.LINK, "https://weblink.example"),
                TextNode(" and another image ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
'''
if __name__ == "__main__":
    unittest.main()

