import os
import shutil

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

def modify_tr_operator():
    post_mdfiles = os.listdir("docs/post")
    for string in post_mdfiles:
        if string[-3:] != ".md":
            post_mdfiles.remove(string)

    for mdf in post_mdfiles:
        with open("docs/post/"+mdf, "r") as f:
            lines = f.readlines()
        for line in lines:
            if "\\tr" in line:
                index = lines.index(line)
                lines[index] = lines[index].replace("\\tr","\operatorname{tr}")

        with open("docs/post/"+mdf, "w") as f:
            for line in lines:
                f.write(line)

def first_line_add_br():
    post_mdfiles = os.listdir("docs/post")
    for string in post_mdfiles:
        if string[-3:] != ".md":
            post_mdfiles.remove(string)

    for mdf in post_mdfiles:
        with open("docs/post/"+mdf, "r") as f:
            lines = f.readlines()
        if lines[0][:3] == "创建于":
            lines[0] = lines[0].replace("\n","<br>\n")

        with open("docs/post/"+mdf, "w") as f:
            for line in lines:
                f.write(line)

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

    docs_sub = os.listdir("./docs")
    if "post" in docs_sub:
        shutil.rmtree("./docs/post")

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
    modify_tr_operator()
    first_line_add_br()

   # dp = "dp"
   # os.system(f"git add . && git commit -m \'{dp}\' && git push")

