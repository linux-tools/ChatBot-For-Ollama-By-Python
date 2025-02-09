import sys #调用系统相关的库
import os #调用系统相关的库
import psutil #调用系统相关的库
import re #调用系统相关的库

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox #引用Pyside6相关的Qt库
from PySide6.QtWebEngineWidgets import QWebEngineView #引用Pyside6相关的Qt库

from Modules_UI.Chat import Ui_MainWindow #引用Chat.py
from Modules_UI.Ask import Ui_DialogUseModels #引用Ask.py
from Modules_UI.Version import Ui_DialogVersion #引用Version.py
from Modules_UI.OllamaState import Ui_DialogForStateOllama #引用OllamaState.py
from Modules_UI.SearchForLLMs import Ui_DialogForSearchLLMs #引用SearchForLLMs.py
from Modules_UI.RemoveLLMs import Ui_DialogForRemoveLLMs #引用RemoveLLMs.py

from langchain_ollama import OllamaLLM #调用langchain-ollama库
from langchain_core.prompts import ChatPromptTemplate #调用langchain模板库

class Application(QMainWindow,Ui_MainWindow): #调用Chat.py
    def __init__(self):
        super(Application, self).__init__()
        self.setupUi(self)

class DialogUseModels(QDialog,Ui_DialogUseModels): #调用Ask.py
    def __init__(self):
        super(DialogUseModels,self).__init__()
        self.setupUi(self)

class DialogVersion(QDialog,Ui_DialogVersion): #调用Version.py
    def __init__(self):
        super(DialogVersion,self).__init__()
        self.setupUi(self)

class DialogOnOrOffOllama(QDialog,Ui_DialogForStateOllama): #调用OllamaState.py
    def __init__(self):
        super(DialogOnOrOffOllama,self).__init__()
        self.setupUi(self)

class DialogForSaecrhLLMs(QDialog,Ui_DialogForSearchLLMs): #调用SearchForLLMs.py
    def __init__(self):
        super(DialogForSaecrhLLMs,self).__init__()
        self.setupUi(self)

class DialogForRemoveLLMs(QDialog,Ui_DialogForRemoveLLMs): #调用RemoveLLMs.py
    def __init__(self):
        super(DialogForRemoveLLMs,self).__init__()
        self.setupUi(self)

#以下为AI初始化操作
###################################################
bot = ""
model = OllamaLLM(model=bot)
template = """
请回答以下问题。

这是上一对话记录: {context}

问题: {question}

答案:
""" #对话模板
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model #通过管道操作符传递模板
context = ""
###################################################

def about(): #显示版本信息
    version_show = DialogVersion()
    version_show.show()
    version_show.pushButton.clicked.connect(version_show.close)
    version_show.exec()

def check_current_llm(): #查看当前使用的AI
    msg1 = QMessageBox() #创建对象
    if bot != "":
        QMessageBox.information(msg1, "当前使用模型",bot,QMessageBox.StandardButton.Ok)
    else:
        QMessageBox.warning(msg1,"提示","你尚未选择可用的大语言模型，请选择大语言模型使用",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.No)

def choose(): #选择模型
    def exit_dialog():
        global context,bot,model,prompt,chain
        bot = ask.lineEdit.text()
        context = ""
        llms_pattern = r'.+:+[^a-z^A-Z]+[b]?$'  # 检查bot参数是否有效
        if not re.match(llms_pattern,bot):
            msg_bot_not_valid = QMessageBox()
            QMessageBox.critical(msg_bot_not_valid, "警告", f"{bot}名称无效")
        else:
            check_is_exist = os.popen(f"ollama list {bot}").read() #检查模型是否存在
            if check_is_exist == "":
                msg_llms_is_not_exist = QMessageBox()
                QMessageBox.warning(msg_llms_is_not_exist,"警告",f"{bot}模型不存在")
            else:
                #############################
                #模型切换，实际上是重新初始化
                model = OllamaLLM(model=bot)
                prompt = ChatPromptTemplate.from_template(template)
                chain = prompt | model
                #############################
                ask.close()
    if is_run_ollama(): #检测哦ollama是否运行
        information = os.popen("ollama list")
        text = information.read()
        ask = DialogUseModels()
        ask.show()
        ask.textEdit.setText(text)
        ask.pushButton.clicked.connect(exit_dialog)
    else:
        msg_warn_for_choose = QMessageBox()
        QMessageBox.warning(msg_warn_for_choose,"警告","当前Ollama没有运行")

def send_msg_to_ai(): #调用Ollama的接口
    global context
    if not is_run_ollama():
        msg_for_not_run_ollama = QMessageBox()
        QMessageBox.critical(msg_for_not_run_ollama,"警告","当前Ollama未运行")
    if bot == "": #此处警告
        msg_for_not_choose_llm = QMessageBox()
        choose_button = QMessageBox.critical(msg_for_not_choose_llm, "警告", "你尚未选择可用的大语言模型，请选择大语言模型使用",QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.No)
        if choose_button == QMessageBox.StandardButton.No:
            main_win.close()
    else:
        ###################################################################重要部分
        main_win.textBrowser.clear()
        user_input = main_win.plainTextEdit.toPlainText()
        result = chain.invoke({"context": context, "question": user_input}) #对话核心代码
        main_win.plainTextEdit.clear()
        main_win.textBrowser.setMarkdown(result)
        context += f"\nUser:{user_input}\nAI:{result}"
        ###################################################################重要部分

def is_installed_in_app():#判断是否安装Ollama
    username = os.popen("echo %username%").read().strip()
    path = rf'C:\Users\{username}\AppData\Local\Programs\Ollama\ollama app.exe'
    return os.path.exists(path)

def is_run_ollama(): #判断是否运行ollama，运行返回True
    flag = False
    process_name = 'ollama.exe'
    all_pid = psutil.pids()
    for pid in all_pid:  # 检查是否启动Ollama
        p = psutil.Process(pid)
        if p.name() == process_name:
            flag = True
            break
    return flag

def control_service_open_ollama_menu(): #控制ollama服务开关
    ############################
    def on_ollama(): #打开Ollama
        if not is_run_ollama():
            cmd = r'"C:\\Users\\%username%\\AppData\\Local\\Programs\\Ollama\\ollama app.exe"'.strip()
            os.popen(cmd)
            choose_menu.textEdit.setText("Ollama目前在运行")
    ############################
    def off_ollama(): #关闭Ollama
        if is_run_ollama():
            for proc in psutil.process_iter():
                if "ollama.exe" in proc.name().lower():
                    proc.terminate()
                if "ollama app.exe" in proc.name().lower():
                    proc.terminate()
            choose_menu.textEdit.setText("Ollama目前处于关闭状态")
    ############################
    choose_menu = DialogOnOrOffOllama()
    choose_menu.show()
    if is_run_ollama():
        choose_menu.textEdit.setText("Ollama目前在运行")
    else:
        choose_menu.textEdit.setText("Ollama目前处于关闭状态")
    choose_menu.pushButton.clicked.connect(on_ollama) #开按钮
    choose_menu.pushButton_2.clicked.connect(off_ollama) #关按钮
    choose_menu.exec()

def ollama_llms_download(): #下载大语言模型
    ##################################
    def work():
        target = search.lineEdit.text()
        llms_pattern = r'.+:+[^a-z^A-Z]+[b]?$'
        if re.match(llms_pattern,target):
            msg_finish = QMessageBox()
            QMessageBox.information(msg_finish, "信息",f"{target}将开始下载，请不要关闭命令提示符窗口，待下载完成后，会自动关闭窗口，如果只闪现一下，请检查下载模型名称是否正确或是否已下载")
            os.popen(f'start cmd.exe /K "ollama pull {target} && exit"')
            search.lineEdit.clear()
        else:
            msg_llms_name_invalid = QMessageBox()
            QMessageBox.warning(msg_llms_name_invalid,"警告",f"{target}名称无效")
    ###################################
    search = DialogForSaecrhLLMs()
    search.webEngineView.load("https://ollama.com/search")
    search.webEngineView.show()
    search.pushButton.clicked.connect(work)
    search.pushButton_2.clicked.connect(search.close)
    search.show()
    search.exec()

def ollama_rm_llms(): #删除大语言模型
    ###########################################
    def rm_llms():
        target = rm_llm.lineEdit.text()
        llms_pattern = r'.+:+[^a-z^A-Z]+[b]?$'
        if re.match(llms_pattern,target): #检查输入是否合法
            check_is_exist = os.popen(f"ollama list {target}").read()  # 检查模型是否存在
            check_pattern = r'.+[not found]$'
            if re.match(check_pattern,check_is_exist):
                msg_llms_is_not_exist = QMessageBox()
                QMessageBox.warning(msg_llms_is_not_exist, "警告", f"你不能删除，因为{target}模型不存在")
            else:
                rm_llm.textBrowser.clear()
                os.popen(f"ollama rm {target}")
                information = os.popen("ollama list").read()
                rm_llm.textBrowser.setText(information)
        else:
            msg_cannot_rm_llms = QMessageBox()
            QMessageBox.warning(msg_cannot_rm_llms,"警告",f"你不能删除，因为{target}名称无效")
    ###########################################
    rm_llm = DialogForRemoveLLMs()
    rm_llm.pushButton.clicked.connect(rm_llms)
    rm_llm.pushButton_2.clicked.connect(rm_llm.close)
    information = os.popen("ollama list").read()
    rm_llm.textBrowser.setText(information)
    rm_llm.show()
    rm_llm.exec()

def ollama_version():
    msg_ollama_version = QMessageBox()
    version_of_ollama = os.popen("ollama -v").read()
    QMessageBox.information(msg_ollama_version,"Ollama Version",version_of_ollama)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 初始化
    if is_installed_in_app(): #安装了ollama的则开始使用
        if not is_run_ollama():
            msg_run = QMessageBox()
            QMessageBox.information(msg_run,"提示","您没有运行Ollama,接下来将运行Ollama")
            check = QMessageBox.question(msg_run,"提问","是否打开Ollama",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if check == QMessageBox.StandardButton.Yes:
                cmd = r'"C:\\Users\\%username%\\AppData\\Local\\Programs\\Ollama\\ollama app.exe"'
                os.popen(cmd)
        main_win = Application()
        main_win.show() #展示窗口
        main_win.actionCurrent_LLM.triggered.connect(check_current_llm) #查看当前模型
        main_win.actionAbout.triggered.connect(about) #跳转到关于界面
        main_win.actionChoose_Language_Models.triggered.connect(choose) #进入选择界面
        main_win.action_Open_or_close_ollama.triggered.connect(control_service_open_ollama_menu) #进入Ollama开关界面
        main_win.actionExit.triggered.connect(main_win.close) #退出程序
        main_win.actionDownload_LLMs.triggered.connect(ollama_llms_download) #下载大语言模型
        main_win.actionCheck_Ollama_Version.triggered.connect(ollama_version) #查看Ollama版本
        main_win.actionRemove_LLMs.triggered.connect(ollama_rm_llms) #移除大语言模型
        main_win.pushButton.clicked.connect(send_msg_to_ai) #跳转到对ai发送信息的函数
        app.exec()
    else: #否则不进入
        msg_exit = QMessageBox()
        QMessageBox.critical(msg_exit, "Error", "你没有安装Ollama，无法使用")