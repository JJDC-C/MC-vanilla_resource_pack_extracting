暑假太闲了，试图学习python，写出了这么个东西。

这个脚本可以提取出MC中被混淆的资源文件（.minecraft/assets/objects），配合client.jar的解包可以得到MC的原版资源包——就这么简单。


注意：文件路径写错会导致错误（闪退），可以尝试将文件夹拖入命令行。

如不想在命令行中输出信息，可以在程序同目录下创建“noprint.txt”。

文件是先复制再重命名，所以当文件重复时会出现完成复制但未能命名的错误，可以先行删除已存在的文件。

在开始之前，请确保所有文件齐全，可用启动器“检查资源文件完整性”。


没有python的可以下载exe版，不过有概率报毒
