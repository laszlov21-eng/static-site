import unittest
from block_markdown import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        self.maxDiff = None
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is a list item
- This is another list item

```
code block
```

> This is a quote

1. This is an ordered list item
2. This is another ordered list item
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is a list item</li><li>This is another list item</li></ul><pre><code>code block</code></pre><blockquote>This is a quote</blockquote><ol><li>This is an ordered list item</li><li>This is another ordered list item</li></ol></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
