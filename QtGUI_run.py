#运行Guiv1_ui.py
from Guiv1_ui import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import sys,subprocess



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
        self.ui.pushButton_2.clicked.connect(self.run)
        self.ui
        self.show()

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        self.ui.lineEdit.setText(file_path.split('/')[-1])
        #label 设置
        self.ui.runpath.setText('/'.join(file_path.split('/')[0:-1]))

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
            self.ui.runpath.setText('/'.join(file_path.split('/')[0:-1]))
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
