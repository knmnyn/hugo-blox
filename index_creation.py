import json 
import os 
import pandas as pd 
import argparse


class IndexCreation:
    def __init__(self, author_dir):
        self.author_dir = author_dir

    def loop_author_dir(self):
        index_dict = dict()
        for author_id in os.listdir(self.author_dir):
            # check if the author_id is a directory
            if not os.path.isdir(os.path.join(self.author_dir, author_id)):
                continue
            # the actual page is _index.md inside the author_id directory
            page_path = os.path.join(self.author_dir, author_id, "_index.md")
            # read the page
            with open(page_path, "r") as f:
                page_content = f.read()
            # Extract the title from the page content
            title_line = [line for line in page_content.split('\n') if line.startswith('title:')][0]
            title = title_line.replace('title:', '').strip()
            print(author_id, title)
            index_dict[author_id] = title

        # save it to a json, at "assets/author_index.json"
        with open("assets/author_index.json", "w") as f:
            json.dump(index_dict, f, indent=4)
        print("Saved to assets/author_index.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--author_dir", type=str, default="content/authors")
    args = parser.parse_args()

    index_creation = IndexCreation(args.author_dir)
    index_creation.loop_author_dir()
