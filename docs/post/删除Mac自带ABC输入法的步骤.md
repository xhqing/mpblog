创建于 2022-02-22<br>
关键词: Mac, 删除, 自带ABC输入法.

Mac自带的ABC输入法是不能在设置中通过直接按减号删除的，网上有的文章说关闭SIP系统就可以了，实践证明关闭SIP系统还是会保证com.apple.HIToolbox.plist文件的完整性。

考虑其本质，操作系统保持系统完整性其实就是在还原用户可能误操作的文件，既然如此，只要想办法不让操作系统修改用户操作的文件就好了。

步骤如下：

1、复制这个文件到随便一个方便操作的目录

```bash
cp ~/Library/Preferences/com.apple.HIToolbox.plist some-dir-path
```

2、用Xcode打开刚才复制的com.apple.HIToolbox.plist文件

3、编辑com.apple.HIToolbox.plist文件（依次点开 Root - AppleEnabledInputSources ，会看到一列 item ，找到其中 KeyboardLayout Name 为 ABC 的那一列，将整列 item 删掉，然后 command + S 保存。）

**4、找到刚才修改过的com.apple.HIToolbox.plist文件，鼠标右键，点击get info，当前用户权限更改为“read-only”并勾选上“Locked”**

**5、查看文件权限是否修改成功**
```bash
ls -l some-dir-path/com.apple.HIToolbox.plist
```

显示-r--------.....就是修改成功。

6、执行如下命令进行替换

```bash
rm ~/Library/Preferences/com.apple.HIToolbox.plist && cp some-dir-path/com.apple.HIToolbox.plist ~/Library/Preferences/ 
```

 注意这里不能直接cp，不会覆盖，要先rm删除原文件。

7、重启Mac