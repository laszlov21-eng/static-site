import os
import shutil
import sys

from generate_page import generate_pages_recursive


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    source_path = "static"
    dest_path = "docs"
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    copy_files_recursive(source_path, dest_path)

    generate_pages_recursive(
        basepath,
        "content",
        "template.html",
        "docs",
    )


main()