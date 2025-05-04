import unittest

from htmlnode import *

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


if __name__ == "__main__":
    unittest.main()

