# Cpp_Concurrency_In_Action_zh-cn

此处存储的是 **《C++ Concurrency in Action》英文版的中文翻译** 中的正文+附录生成的pdf单文件，带目录，方便查阅。

原翻译出处是 https://github.com/xiaoweiChen/Cpp_Concurrency_In_Action
作者：Anthony Williams 译者：[陈晓伟](https://github.com/xiaoweiChen "xiaoweiChen")
版权属于他们。此处文档的许可也是GPL-2.0.
这份翻译基于原书第一版，讲的是C++11中的多线程应用。目前出了第二版，译者也翻译了，添加了C++14和C++17的内容。

我做的事情主要有：
- 用python将正文和附录的所有markdown文件合并到一个文件中。
- 删除了其中的`<br>`标签。
- 给代码段指明编程语言（c++），以便有语法高亮效果。
- 使用typora导出为pdf文件。
- 裁切了pdf文档四周的部分空白，优化版面显示。

我没有修改原译文中的内容。如果会修改其中内容然后再生成pdf文档的话，可以基于此处的markdown文档，然后用typora导出。
或者像我一样从头生成，那么在导出前需要先完成以下三步。1）去原翻译处下载文件。2）使用此处的python文件（需修改文件存放路径为你的存放位置）合并文档。3）用正则表达式批量删除`<br>`标签以及给代码块添加C++语言标识，用的是Notepad++，查找：(\```)([\s\S]*?)(\```)， 替换：```C++\2\3
