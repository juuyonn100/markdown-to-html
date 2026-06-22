# markdown-to-html

A simple Markdown to HTML converter written in pure Python (no dependencies).

## Features

- Converts headers (H1-H6)
- Bold and italic text
- Links and inline code
- Unordered lists
- Paragraph wrapping
- No external dependencies — pure Python regex-based parser

## Usage

```bash
# Convert to same name with .html extension
python md2html.py README.md

# Custom output filename
python md2html.py README.md output.html
```

## Example

Input (`example.md`):
```markdown
# Hello World

This is **bold** and *italic* text.

- Item one
- Item two

Check out [GitHub](https://github.com).
```

Output (`example.html`):
```html
<h1>Hello World</h1>
<p>This is <strong>bold</strong> and <em>italic</em> text.</p>
<ul>
<li>Item one</li>
<li>Item two</li>
</ul>
<p>Check out <a href="https://github.com">GitHub</a>.</p>
```

## Requirements

- Python 3.x

## Limitations

This is a lightweight parser intended for simple Markdown files. It does not support tables, nested lists, or code blocks.
