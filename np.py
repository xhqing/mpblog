import os, sys
import time

class TitleError(Exception):
    """TitleError"""

class TitleDuplicated(Exception):
    """Title Duplicated"""

def is_cn(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

def is_en(strs):
    up = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lo = "qwertyuiopasdfghjklzxcvbnm"
    assert len(up) == 26
    assert len(lo) == 26

    is_enf = True
    for s in strs:
        if (s in up) or (s in lo) or (s==" "):
            continue
        else:
            is_enf = False
            break
    return is_enf

# def write_keywords():
#     with open(f"./post/{post_title}.md", "a") as f:
#         f.write("关键词: " + ", ".join(keywords_list) + ".")

def write_createtime():
    with open(f"./post/{post_title}--未完成.md", "w") as f:
        f.write("创建于 " + time.strftime("%Y-%m-%d", time.localtime()) + "\n")

if __name__ == "__main__":
    try:
        post_title = sys.argv[1]
    except IndexError:
        raise TitleError(f"""\033[01;31;01m no title, `python3 np.py your_post_title`\033[01;31;01m""")

    cpost_dir = os.listdir("./post")
    if f"{post_title}.md" in cpost_dir or f"{post_title}--未完成.md" in cpost_dir:
        raise TitleDuplicated(f"""\033[01;31;01m {post_title}.md or {post_title}-未完成.md has already exist in ./post, please choose another one. \033[01;31;01m""")

    os.system(f"touch post/{post_title}--未完成.md")
    
    write_createtime()
    with open(f"./post/{post_title}--未完成.md", "a") as f:
        f.write("关键词: ")
    # add keywords
    # first_input = True
    # keywords_list = []
    # while True:
    #     if first_input:
    #         print("请输入本篇文章的关键词(仅支持中英文词组, 输入字母`q`退出, `回车`确定): ")
    #         first_input = False
    #     else:
    #         print("已经添加的关键词: ", keywords_list)
    #         print("请继续添加关键词: ")
        
    #     keyword = input()
    #     if keyword == "q":
    #         write_keywords()
    #         break
        
    #     keywords_list.append(keyword)
        
        # if is_cn(keyword) or is_en(keyword):
        #     keywords_list.append(keyword)
            # print("是否要继续添加关键词? y/n")
            # while True:
            #     yorn = input()
            #     if yorn in ["Y","y"]:
            #         break
            #     elif yorn in ["N","n"]:
            #         break
            #     else:
            #         print("Please input Y/y/N/n")

            # if yorn in ["y","Y"]:
            #     continue
            # else:
            #     write_keywords()
            #     break

        # else:
        #     print("""添加失败, 如果是中文关键词请输入全中文字符, 如果是英文关键词只支持大小写字母和空格字符.""")
    

    os.system(f"open ./post/{post_title}--未完成.md")
