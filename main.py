from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import re
from untitled import *
import sys
import os
import time
from youdaoEngine import *

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.actionConnector()
        self.workingFlag = True
        self.wordList = []
        self.result_list = []

    def actionConnector(self):
        self.pushButton.clicked.connect(self.chooseFile)
        self.pushButton_2.clicked.connect(self.chooseOutDir)
        self.pushButton_3.clicked.connect(self.translationEngine)
        self.pushButton_5.clicked.connect(self.saveInformation)

    def chooseFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Txt file (*.txt)")
        if fileName:
            self.label_3.setText(fileName)
            self.label_4.setText(os.path.dirname(fileName))
            with open(fileName) as file_obj:
                self.wordList = set(list(filter(None, re.split(r"[\n|\s|,|!|;|\"|.|']", file_obj.read()))))
                self.wordList = [i.lower() for i in self.wordList]
                self.listWidget.addItems(self.wordList)
                lenOfList = len(self.wordList)
                self.label_6.setText(str(lenOfList))

    def chooseOutDir(self):
        dirName= QFileDialog.getExistingDirectory(self, "选择一个你要输出的目录", os.getcwd())
        print(dirName)
        if dirName:
            self.label_4.setText(os.path.dirname(dirName))

    def translationEngine(self):
        self.result_list = []
        if self.wordList:
            self.tableWidget_2.setRowCount(0)
            for row, word in enumerate(self.wordList):
                print(row, word)
                time.sleep(0.5)
                self.tableWidget_2.insertRow(row)
                self.tableWidget_2.setItem(row, 0, QTableWidgetItem(word))
                res = connect(word)
                # print(type(res))
                # json_obj = json.loads(res)
                outputWord = {
                    'word': res['query'],
                    'translation': res.get('web'),
                    'pronounce-us': res.get('basic').get('us-phonetic'),
                    'pronounce-uk': res.get('basic').get('uk-phonetic'),
                       }
                buffer_str = ''
                for word in res.get('web'):
                    buffer_str += f"{word.get('key')}: {','.join(word.get('value'))}\n"
                    break
                    # buffer_str += f"{','.join(word.get('value'))}\n"
                self.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(f"[{res.get('basic').get('us-phonetic')}]")))
                self.tableWidget_2.setItem(row, 2, QTableWidgetItem(buffer_str))
                self.result_list.append(outputWord)
        else:
            pass

    def saveInformation(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())