# ChatBot For Ollama By Python

![alt text](ChatBot_For_Ollama.ico)

你的人工AI智能助手（较为简便的图形化的Ollama前端客户端，目前支持Windows，但是后续将支持Linux平台）

## 介绍

通过Pyside6和langchain相关Python库来编写此软件。
本软件为Ollama前端客户端，支持模型搜索，下载，删除等管理，以及支持大语言模型当前对话。
该项目为练手项目，可供学习Qt开发（Python）的用户参考，会不定期更新版本。
该软件界面比较简陋，但是功能基本齐全，但任然存在一些问题：对话时等待AI对话回复过程中存在假死现象（后期本人在学习QThread，之后解决）；下载模型过程实现上比较简陋等问题。

## 安装教程

1、从源代码打包成exe（使用nuitka）：
方式一：（不推荐）
    下载源码后解压，执行make.ps1的powershell脚本文件，执行完毕后从生成的output目录中就能找到生成的二进制文件啦！执行前请确认pip镜像速度稳定，构建过程中将会自动下载大量依赖，或者执行install-dependencies.ps1下载安装依赖

方式二：（推荐）
    （1）、请安装python最新版，用python -m venv "虚拟环境名称"来创建虚拟模拟环境（或者用conda创建虚拟环境）
    （2）、把源代码解压在虚拟环境中，然后执行make.ps1开始执行编译打包

依赖如下：
    langchain>=0.1.20
    langchain-ollama
    langchain_core
    pyside6
    nuitka
    psutil

2、从Release下载打包好的二进制文件，直接运行即可

## 使用说明

* 作为Ollama前端客户端，您可以从菜单栏中选择操作并执行。如图：
![alt text](.\image/image-1.png)
![alt text](.\image/image.png)

* 下载界面会弹出ollama模型搜索官网：
![alt text](.\image/image-2.png)

您可以在搜索界面搜索大语言模型并下载，注意会提示cmd弹窗，此为调用ollama执行下载程序操作，切不可随意关闭，如果关闭，下载将会终止（但是下载的内容会保存）

* 这是选择大语言模型界面：
![alt text](.\image/image-3.png)

* 查看当前使用模型：
![alt text](.\image/image-4.png)

* 选择开关Ollama服务：
![alt text](.\image/image-5.png)

* 查看Ollama版本：
![alt text](.\image/image-6_1.png)
![alt text](.\image/image-6_2.png)
该功能也可以查看Ollama的运行状态

## 参与贡献

欢迎有志者参与开发
