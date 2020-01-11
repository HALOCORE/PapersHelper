# PapersHelper
Help with my downloaded papers in a directory.

## 安装与运行
> 所有的命令，都是从当前目录出发运行
### 安装core后端运行环境
我是用的是python 3.7。首先创建名为_venv的python虚拟环境:
```
python3.7 -m venv _venv
```
接着进入虚拟环境：
```
cd _venv
source bin/activate
```
接着安装python包：
```
pip install -r requirements.txt
```
### 运行core后端
启动django:
```
cd core
python manage.py runserver
```
测试模块功能(不启动django):
```
cd core
python -m core.test
```
### 安装helperui前端运行环境
如果没有node和npm，先通过nvm安装它们。接下来：
```
cd frontend/helperui
npm install
```

### 运行helperui前端
```
npm start
```
接着访问http://localhost:3000/

## backend(core) API design
所有请求会返回log字段。

- /reload
    - 更新全部
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


