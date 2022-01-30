from PyQt6.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QTableWidgetItem, QApplication
import re
from untitled import *
import sys
import os
import time, datetime
from youdaoEngine import *
import openpyxl as xl

ignoreList = [
  "am", "is", "are", "was", "were", "the", "i",
  "you", "we", "they", "them", "he", "him", "her", "she", "it", "an", "in"
]

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
        self.actionAbout_mengboTranslator.triggered.connect(self.aboutApp)
        self.actionExit.triggered.connect(self.close)

    def chooseFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "选择你需要解析的文件", "", "Txt file (*.txt)")
        if fileName:
            self.label_3.setText(fileName)
            self.label_4.setText(os.path.dirname(fileName))
            try:
                # If the txt file decode error or decode issue, handle this problem and notify customer
                print(f'open file>>: {fileName}')
                with open(fileName, errors='ignore') as file_obj:
                    # split a txt file into words
                    self.wordList = set(list(filter(None, re.split(r"[\n|\s|,|!|;|\"|.|']", file_obj.read()))))
                    self.wordList = [i.lower() for i in self.wordList]
                    # Use ignorelist function to kick simple words off, this process need to be refined in subsequence version
                    self.wordList = [i for i in self.wordList if not i in ignoreList]
                    self.listWidget.addItems(self.wordList)
                    lenOfList = len(self.wordList)
                    self.label_6.setText(str(lenOfList))
            except Exception as e:
                QMessageBox.warning(self, '文件读取失败', f'输入的文件无法被解析，请重新选择文件\n {str(e)}')

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
                try:
                    res = connect(word)
                except Exception as e:
                    QMessageBox.warning(self, '异常捕获', f'HTTP链接管理系统出错，请截图报送孙海涛\n{str(e)}')
                    break
                try:
                    outputWord = {
                        'word': res['query'],
                        'translation': res.get('web'),
                        'pronounce-us': res.get('basic').get('us-phonetic'),
                        'pronounce-uk': res.get('basic').get('uk-phonetic'),
                           }
                except:
                    outputWord = {
                        'word': res['query'],
                        'translation': [],
                        'pronounce-us': '',
                        'pronounce-uk': '',
                    }
                buffer_str = ''
                for word in outputWord.get('translation'):
                    buffer_str += f"{word.get('key')}: {','.join(word.get('value'))}\n"
                    break
                self.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(f"[{outputWord.get('pronounce-us')}]")))
                self.tableWidget_2.setItem(row, 2, QTableWidgetItem(buffer_str))
                self.result_list.append(outputWord)
        else:
            pass

    def saveInformation(self):
        currentTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filePath = f'{self.label_4.text()}/{currentTimeStamp}.xlsx'
        print(filePath)
        if os.path.exists(filePath):
            # pupop window to check the file
            print('duplicate file')
        else:
            if not self.result_list:
                QMessageBox.information(self, '空的缓存', '系统无法读取到任何缓存的单词解释\n请重新选择文件并执行')
                return
            workbook = xl.Workbook()
            workbook.save(filePath)
            sheet = workbook.active
            headers = ["Word", "Pronounce", "Translate"]
            sheet.append(headers)
            for word in self.result_list:
                dataBuffer = [word['word'], f"[{word.get('pronounce-us')}]"]
                for translate in word.get('translation'):
                    dataBuffer.append(f"{', '.join(translate.get('value'))}")
                    break
                sheet.append(dataBuffer)
            workbook.save(filePath)
            self.tableWidget_2.setRowCount(0)
            self.listWidget.clear()
            self.label_3.setText('')
            self.label_4.setText('')
            self.result_list.clear()
            self.wordList.clear()

    def aboutApp(self):
        QMessageBox.information(self, 'About mengboTranslator', 'v0.1 Demo version\n有困难找蒙博，蒙博啥都行！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())