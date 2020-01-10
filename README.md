# PapersHelper
Help with my downloaded papers in a directory.

## backend(core) API design
所有请求会返回log字段。

- /files
    - get 获取文件树
        - ?q=xxx 筛选含有xxx的文件
    - /\<filename\>
        - /summary
            - get 获取指定文件的summary（不存在则创建）
            - /check
                - get 检查summary完整性
        - /refs
            - get 获取指定文件的全部ref（不存在则创建）
            - /link
                - get 对所有未匹配ref寻找匹配的文件
                - post 上传匹配信息，更新ref
        - /fulltxt
            - get 获取完整文本
    - /cachefulltxt
        - get 对所有文件获取fulltxt
- /folders
    - get 获取folder列表
    - /\<foldername\>
        - /summary
            - get 获取该文件夹的markdown summary（不存在则创建）
            /update
                - get 自动更新summary
            /check
                - get 获取summary检查结果
- /conf
    - get 获取系统配置
    - post 设置系统配置
- /test
    - get 测试代码


