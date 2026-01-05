import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    extract_title,
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

- This is a list item
- This is another list item

"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "- This is a list item\n- This is another list item",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        markdown = """
# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.

- This is a list item
- This is another list item

"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "- This is a list item\n- This is another list item",
            ],
        )

    def test_block_to_block_type(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "* list\n* list"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. list"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_extract_title(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.
"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is a heading")


if __name__ == "__main__":
    unittest.main()
