import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QMessageBox
from PyQt5.QtGui import QDoubleValidator,QIntValidator

class jisuan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T+0工具v1.0")
        self.resize(600,300)
        self.label_buy = QLabel("买入价格")
        self.label_sell = QLabel("卖出价格")
        self.label_num = QLabel("买入的股数")
        self.label_hand = QLabel("买入手续费(‱)")
        self.label_money = QLabel("利息")
        self.input_num = QLineEdit()
        self.input_buy = QLineEdit()
        self.input_sell = QLineEdit()
        self.input_hand = QLineEdit()
        self.input_money = QLineEdit()
        self.button = QPushButton("预期盈利")
        self.button.clicked.connect(self.calculate)
        self.result = QLabel("结果将在此显示")
        self.input_num.setValidator(QIntValidator())
        self.input_buy.setValidator(QDoubleValidator())
        self.input_sell.setValidator(QDoubleValidator())
        self.input_hand.setValidator(QDoubleValidator())
        self.input_money.setValidator(QDoubleValidator())
        self.input_num.returnPressed.connect(self.input_buy.setFocus)
        self.input_buy.returnPressed.connect(self.input_sell.setFocus)
        self.input_sell.returnPressed.connect(self.input_hand.setFocus)
        self.input_hand.returnPressed.connect(self.input_money.setFocus)
        self.input_money.returnPressed.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.label_num)
        layout.addWidget(self.input_num)
        layout.addWidget(self.label_buy)
        layout.addWidget(self.input_buy)
        layout.addWidget(self.label_sell)
        layout.addWidget(self.input_sell)
        layout.addWidget(self.label_hand)
        layout.addWidget(self.input_hand)
        layout.addWidget(self.label_money)
        layout.addWidget(self.input_money)
        layout.addWidget(self.button)
        layout.addWidget(self.result)
        self.setLayout(layout)

    def calculate(self):
        text_buy = self.input_buy.text().strip()
        text_sell = self.input_sell.text().strip()
        text_num = self.input_num.text().strip()
        text_hand = self.input_hand.text().strip()
        text_money = self.input_money.text().strip()

        if not text_num:
            QMessageBox.warning(self,"输入错误","未输入股数")
            return
        if not text_buy:
            QMessageBox.warning(self,"输入错误","未输入买入价格")
            return
        if not text_sell:
            QMessageBox.warning(self,"输入错误","未输入卖出价格")
            return
        if not text_hand:
            QMessageBox.warning(self,"输入错误","未输入手续费")
            return
        if not text_money:
            QMessageBox.warning(self,"输入错误","未输入利息")
            return
        
        try:
            buy = float(text_buy)
            sell = float(text_sell)
            num = int(text_num)
            hand = float(text_hand)
            money = float(text_money)
        except ValueError:
            QMessageBox.warning(self,"输入错误","请输入合法数据")

        hand /= 10000
        profit = (sell-buy)*num
        com = (buy+sell)*num*hand
        flower = sell*num*0.0005
        result = profit-com-flower-money
        self.result.setText(f"计算得出预期成本为{result:.2f}")


        
app = QApplication(sys.argv)
window = jisuan()
window.show()
sys.exit(app.exec_())
