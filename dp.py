import os

class TitleError(Exception):
    """TitleError class"""

def gen_sidebar():
    post_mdfiles = os.listdir("docs/post")
    for string in post_mdfiles:
        if string[-3:] != ".md":
            post_mdfiles.remove(string)
            
    with open("docs/_sidebar.md", "w") as f:
        f.write(" - 目录\n")
        for mdf in post_mdfiles:
            f.write(f"   - [{mdf[:-3]}](post/{mdf})\n")

if __name__ == "__main__":

    post_mdfiles = os.listdir("./post")
    for string in post_mdfiles:
        if string[-3:] != ".md":
            post_mdfiles.remove(string)

    for mdf in post_mdfiles:
        with open("./post/"+mdf, "r") as f:
            text = f.readlines()

        for line in text:
            if line[:2] == "# ":
                raise TitleError(f"""\033[01;31;01m {mdf} {line} Please use 2 '#', {'#'+line}\033[01;31;01m""")

    os.system("cp -r ./post ./docs/")
    post_mdfiles = os.listdir("./docs/post")
    for string in post_mdfiles:
        if string[-3:] != ".md":
            post_mdfiles.remove(string)

    for mdf in post_mdfiles:
        with open("./docs/post/"+mdf, "r") as f:
            text = f.readlines()

        if "## 参考文献\n" in text:
            index = text.index("## 参考文献\n")
            for i in range(index, len(text)):
                if text[i][0] == "[":
                    text[i] = text[i][:-1]+"<br>"+"\n"

        with open("./docs/post/"+mdf, "w") as f:
            for line in text:
                f.write(line)

    gen_sidebar()

    os.system("git add docs")
    os.system("git commit 'dp'")
    os.system("git push")
            

