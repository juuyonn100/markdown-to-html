import re
import sys
import os

def convert(md_text):
    html = md_text

    # Headers
    html = re.sub(r'^###### (.*)', r'<h6>\1</h6>', html, flags=re.M)
    html = re.sub(r'^##### (.*)', r'<h5>\1</h5>', html, flags=re.M)
    html = re.sub(r'^#### (.*)', r'<h4>\1</h4>', html, flags=re.M)
    html = re.sub(r'^### (.*)', r'<h3>\1</h3>', html, flags=re.M)
    html = re.sub(r'^## (.*)', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^# (.*)', r'<h1>\1</h1>', html, flags=re.M)

    # Bold and italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)

    # Inline code
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)

    # Unordered lists
    lines = html.split('\n')
    output = []
    in_list = False
    for line in lines:
        if re.match(r'^[-*] (.*)', line):
            if not in_list:
                output.append('<ul>')
                in_list = True
            item = re.sub(r'^[-*] (.*)', r'<li>\1</li>', line)
            output.append(item)
        else:
            if in_list:
                output.append('</ul>')
                in_list = False
            output.append(line)
    if in_list:
        output.append('</ul>')
    html = '\n'.join(output)

    # Paragraphs (lines not already wrapped in tags)
    lines = html.split('\n')
    output = []
    for line in lines:
        stripped = line.strip()
        if stripped and not re.match(r'^<(h\d|ul|li|/ul)', stripped):
            output.append(f'<p>{stripped}</p>')
        else:
            output.append(line)
    html = '\n'.join(output)

    return html

def convert_file(input_path, output_path=None):
    with open(input_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html_body = convert(md_text)
    html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{os.path.basename(input_path)}</title>
</head>
<body>
{html_body}
</body>
</html>"""

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".html"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_full)

    print(f"Converted: {input_path} -> {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python md2html.py <input.md> [output.html]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    convert_file(input_path, output_path)
