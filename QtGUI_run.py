from Guiv1_ui import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import sys,subprocess
import warnings
import os,csv,re,mmap
import pandas as pd

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.select_file)
        self.ui.lineEdit.setAcceptDrops(True) # 设置lineEdit接受拖拽
        self.ui.lineEdit.dragEnterEvent = self.dragEnterEvent # 设置拖拽进入事件
        self.ui.lineEdit.dropEvent = self.dropEvent # 设置拖拽释放事件
        self.profile_to_comboBox() # 添加这一行以自动填充comboBox
        self.setWindowTitle("VolatilityPro GUI By: Tokeii")
        self.setWindowIcon(QIcon("res/1.png"))
        self.setFixedSize(self.width(), self.height())
        #鼠标点击事件
        self.ui.pushButton_2.clicked.connect(self.run)
        self.ui.pushButton_3.clicked.connect(self.run2)
        self.ui.listWidget.itemDoubleClicked.connect(self.add_to_lineEdit_2) # 添加这一行以响应双击事件
        self.ui.reloadingButton.clicked.connect(self.reloadingButton)
        self.load_filescan_combobox()
        self.ui.pushButton_find.clicked.connect(lambda:self.find_regex_in_large_file(self.ui.lineEdit.text(),self.ui.lineEdit_findstr.text()))
        #dumpfilename
        
        #选择后直接执行load_filescan
        self.ui.comboBox_2.currentIndexChanged.connect(self.load_filescan)
        self.ui.pushButton_4.clicked.connect(lambda:self.load_csv_to_table('pslist'))
        self.ui.pushButton_5.clicked.connect(lambda:self.load_clipboard_to_table())
        self.ui.pushButton_6.clicked.connect(lambda:self.load_csv_to_table('atomscan'))
        self.ui.pushButton_7.clicked.connect(lambda:self.load_csv_to_table('drivermodule'))
        self.ui.pushButton_8.clicked.connect(lambda:self.load_csv_to_table('driverscan'))
        self.ui.pushButton_9.clicked.connect(lambda:self.load_csv_to_table('envars'))
        self.ui.pushButton_10.clicked.connect(lambda:self.load_csv_to_table('gditimers'))
        self.ui.pushButton_11.clicked.connect(lambda:self.load_csv_to_table('hivelist'))
        self.ui.pushButton_12.clicked.connect(lambda:self.load_csv_to_table('joblinks'))
        self.ui.pushButton_13.clicked.connect(lambda:self.load_csv_to_table('ldrmodules'))
        self.ui.pushButton_14.clicked.connect(lambda:self.load_csv_to_table('modscan'))
        self.ui.pushButton_15.clicked.connect(lambda:self.load_csv_to_table('modules'))
        self.ui.pushButton_16.clicked.connect(lambda:self.load_csv_to_table('netscan'))
        self.ui.pushButton_17.clicked.connect(lambda:self.load_csv_to_table('objtypescan'))
        self.ui.pushButton_18.clicked.connect(lambda:self.load_csv_to_table('psscan'))
        self.ui.pushButton_19.clicked.connect(lambda:self.load_csv_to_table('psxview'))
        self.ui.pushButton_20.clicked.connect(lambda:self.load_csv_to_table('shimcache'))
        self.ui.pushButton_21.clicked.connect(lambda:self.load_csv_to_table('callbacks'))
        self.ui.pushButton_22.clicked.connect(self.load_cmdline_to_table)
        self.show()

        
    def select_file(self):
        #加一个*.*格式
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", filter="Memory Dump Files (*.dmp *.iso *.bin *.img *.vmem *.hprof *.core *.elf *.raw)")
        self.ui.lineEdit.setText(file_path.split('/')[-1])
        #label 设置
        self.setWindowTitle('/'.join(file_path.split('/')[0:-1]))

    def profile_to_comboBox(self):
        with open("profilelist.cfg", "r") as f:
            profile_list = f.readlines()
        for profile in profile_list:
            self.ui.comboBox.addItem(profile.strip())

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.ui.lineEdit.setText(file_path.split('/')[-1])
            self.setWindowTitle('/'.join(file_path.split('/')[0:-1]))
    
    


    #执行命令 python volpro.py [imagename] (profile) (dumpfiles)
    def run(self):
        if self.ui.lineEdit.text() == "":
            # 弹出错误提示
            self.ui.lineEdit.setStyleSheet("border: 1px solid red;")
            return
            
        imagename = self.ui.lineEdit.text()
        profile = self.ui.comboBox.currentText()
        dumpfiles = self.ui.lineEdit_2.text()
        if self.ui.lineEdit_2.text() == "":
            command = f"python volpro.py {imagename} {profile}"
        else:
            dumpfiles = self.ui.lineEdit_2.text()
            command = f"python volpro.py {imagename} {profile} dumpfiles {dumpfiles}"
        subprocess.Popen(command, shell=True)
        
        #self.close()
    def run2(self):
        if self.ui.lineEdit.text() == "":
            # 弹出错误提示
            self.ui.lineEdit.setStyleSheet("border: 1px solid red;")
            return
        imagename = self.ui.lineEdit.text()
        profile = self.ui.comboBox.currentText()
        command = f"python volpro.py {imagename}"
        subprocess.Popen(command, shell=True)
    #加载filescan列表
    def load_filescan(self):
        #清空
        self.ui.listWidget.clear()
        filename = self.ui.comboBox_2.currentText()
        if not os.path.exists(f"output/{filename}"):
            return
        with open(f"output/{filename}", "r") as f:
            lines = f.readlines()
            #去除空行
            lines = [line for line in lines if line.strip()]
            #每行去掉空格，用逗号连接，只取每行第一个和最后一个,组成新的列表
            lines = [','.join(line.strip().split()).split(',')[0] +'\n'+','.join(line.strip().split()).split(',')[-1] for line in lines]
        for line in lines:
            self.ui.listWidget.addItem(''.join(line.replace('\Device\HarddiskVolume','disk')))
    #双击添加到lineEdit_2
    def add_to_lineEdit_2(self):
        self.ui.lineEdit_2.setText(self.ui.listWidget.currentItem().text().split('\n')[0])
        #dumpfilename
        wzpath = self.ui.listWidget.currentItem().text().split('\n')[1]
        dumpfilenamenew = wzpath.split('\\')[-1]
        self.ui.dumpfilename.setText(dumpfilenamenew)
    #加载filescan列表
    def load_filescan_combobox(self):
        if os.path.exists("output"):
            output_dir = "output"
            filescan_files = [f for f in os.listdir(output_dir) if "filescan" in f]
            self.ui.comboBox_2.addItems(filescan_files)
        else:
            self.ui.comboBox_2.addItems(["没有找到导出的filescan列表。"])
    #reloadingButton 重新加载filescan列表
    def reloadingButton(self):
        self.ui.comboBox_2.clear()
        self.load_filescan_combobox()
        self.ui.listWidget.clear()
        self.ui.lineEdit_2.clear()
        self.ui.dumpfilename.clear()
    # 一般的加载csv文件到table    
    def load_csv_to_table(self,filename):
        txt_file = rf"output/{filename}.txt"
        csv_file = rf"output/{filename}.csv"
        with open(txt_file, "r") as f:
            lines = f.readlines()
            data = [line.strip().split() for line in lines]
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        filename = f"output/{filename}.csv"
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            lines = f.readlines()
            lines = [line for line in lines if line.strip()]
            lines = [line.strip().split(',') for line in lines]
        self.ui.tableWidget.setRowCount(len(lines))
        self.ui.tableWidget.setColumnCount(len(lines[0]))
        for i, row in enumerate(lines):
            for j, col in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(col))
        self.ui.tableWidget.resizeColumnsToContents()
    # 加载clipboard到table
    def load_clipboard_to_table(self):
        filename = "clipboard"
        txt_file = rf"output/{filename}.txt"
        csv_file = rf"output/{filename}.csv"
        with open(txt_file, "r") as f:
            lines = f.readlines()
        # 处理文本数据
        data = []
        for line in lines:
            # 如果不是空行
            if line.strip():
                lst = line.strip().split()
                try:
                    lst[5] = ' '.join(lst[5:])
                    del lst[6:]
                except:
                    pass
                data.append(lst)
        # 使用 Pandas 创建数据帧，使用data[0]作为列名
        df = pd.DataFrame(data[1:], columns=data[0])
        # 将数据帧写入 CSV 文件
        df.to_csv(csv_file, index=False)
        filename = f"output/{filename}.csv"
        if not os.path.exists(filename):
            return
        lines=data
        self.ui.tableWidget.setRowCount(len(lines))
        self.ui.tableWidget.setColumnCount(len(lines[0]))
        for i, row in enumerate(lines):
            for j, col in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(col))
        self.ui.tableWidget.resizeColumnsToContents()
    # 加载cmdline到table
    def load_cmdline_to_table(self):
        cmdlinedata = 'output\cmdline.txt'
        with open(cmdlinedata, "r") as f:
            #正则匹配：pattern = r'(\w+\.exe)\s*pid:\s*(\d+)\s*Command line\s*:\s*(.*)'
            pattern = r'(\w+\.exe)\s*pid:\s*(\d+)\s*Command line\s*:\s*(.*)'
            matches = re.findall(pattern , f.read())
        newheader = ['ProcessName','PID','CommandLine']
        #写入csv文件
        with open('output\cmdline.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(newheader)
            for match in matches:
                writer.writerow(match)
        with open('output\cmdline.csv', "r") as f:
            lines = f.readlines()
            lines = [line for line in lines if line.strip()]
            lines = [line.strip().split(',') for line in lines]

        self.ui.tableWidget.setRowCount(len(lines))
        self.ui.tableWidget.setColumnCount(len(lines[0]))
        for i, row in enumerate(lines):
            for j, col in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(col))    
        self.ui.tableWidget.resizeColumnsToContents()
    # 搜索字符串
    def find_regex_in_large_file(self,file_path, regex):
        #取WindowTitle标题
        workdir = self.windowTitle()
        file_path = workdir + '/' + file_path
        with open(file_path, 'r+b') as file:
            mm = mmap.mmap(file.fileno(), 0)
            # 使用预编译的正则表达式进行搜索
            pattern = re.compile(bytes(regex, 'utf-8'))
            regexlist = []
            for match in pattern.finditer(mm):
                # 以utf-8格式解码以打印字符串
                try:
                    regexlist.append(match.group().decode('utf-8'))
                except:
                    pass
            mm.close()
        #加载到 tableWidget,宽度自适应
        self.ui.tableWidget.setRowCount(len(regexlist))
        self.ui.tableWidget.setColumnCount(1)
        for i, row in enumerate(regexlist):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(row))
        self.ui.tableWidget.resizeColumnsToContents()
            


if __name__ == "__main__":
    os.environ['QT_LOGGING_RULES'] = 'qt.imageio.*=false'
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=UserWarning, module='PIL')
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
