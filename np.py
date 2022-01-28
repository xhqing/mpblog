import os, sys

class TitleError(Exception):
    """TitleError"""

if __name__ == "__main__":
    try:
        post_title = sys.argv[1]
    except IndexError:
        raise TitleError(f"""\033[01;31;01m no title, `python3 np.py your_post_title`\033[01;31;01m""")

    os.system(f"touch ./post/{post_title}.md && open ./post/{post_title}.md")
