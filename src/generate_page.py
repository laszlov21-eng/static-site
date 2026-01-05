from block_markdown import markdown_to_html_node, extract_title
import os


def generate_page(basepath,from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/',f'href="{basepath}')
    template = template.replace('src="/',f'src="{basepath}')
    with open(dest_path, "w") as f:
        f.write(template)


def generate_pages_recursive(basepath,dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isdir(from_path):
            os.mkdir(dest_path)
            generate_pages_recursive(basepath,from_path, template_path, dest_path)
        else:
            if from_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")
                generate_page(basepath,from_path, template_path, dest_path)
