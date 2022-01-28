# It's My Personal Blog (MPBlog) Repo
Based on [docsify](https://docsify.js.org/).

## MPBlog Address
https://xhqing.github.io/mpblog

## Usage
1. set alias in `~/.zshrc` for convenient.
```bash
alias np="python3 np.py"
alias dp="python3 dp.py"
```
remember exe `source ~/.zshrc` after set alias.

2. confirm you are in the root dir of mpblog.
```bash
pwd # /xx/xxx/.../mpblog/
```

3. usage
```bash
# new post, it will generate a your_post_title.md file in `./post` and open it automatically with typora (I use typora).
np your_post_title

# deploy on github. copy `./post` to `./docs/` and check or modify something automatically, git push the whole mpblog repo finally.
dp
```

## GitHub Page Setting
It's very easy.
![img](20220128215228.jpg)


## LICENSE
MIT
