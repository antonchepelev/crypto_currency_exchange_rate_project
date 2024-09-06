import sys
from PyQt6 import  QtWidgets, QtGui
import requests
from crypto import get_coin_by_symbol, attribute_mapping, coins_list
from smtp import send_email
from html_generator import html_generator
import time




class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        
        displays = {attr: attribute_mapping[attr] for attr in attribute_mapping}

        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.button = QtWidgets.QPushButton("Send Selected Data!")
        self.button.clicked.connect(self.send_mail_on_clicked)

        self.check_boxes = {attr: QtWidgets.QCheckBox(display) for attr, display in displays.items()}

       
        
        crypto_head_label = QtWidgets.QLabel("Cryptocurrencies") 
        
        crypto_head_label.setStyleSheet(
        """

        font-size:30px;
        font-weight:bolder;
        font-family:monospace;
        text-transform: uppercase;
        """ )
        
        attr_head_label = QtWidgets.QLabel("Attributes") 
        attr_head_label.setStyleSheet(
        """
        font-size:30px;
        font-weight:bolder;
        font-family:monospace;
        text-transform: uppercase;

        """ )



       
        self.table = QtWidgets.QTableWidget()
       
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.button)

      
        self.checkbox_layout = QtWidgets.QGridLayout()

       
        r = 0
        c = 0
        for attr, checkbox in self.check_boxes.items():
            self.checkbox_layout.addWidget(checkbox, r, c)
            checkbox.clicked.connect(lambda _, attr=attr: self.update_table(attr))
            r += 1
            if r >= 4:
                r = 0
                c += 1

        
        
        self.name_checkboxes = [QtWidgets.QCheckBox(coin.symbol) for coin in coins_list]
        self.crypto_name_layout = QtWidgets.QGridLayout()
        r = 0
        c = 0
        for coin, checkbox in zip(coins_list, self.name_checkboxes):
            self.crypto_name_layout.addWidget(checkbox, r, c)
            checkbox.clicked.connect(lambda _, coin=coin: self.update_table(coin.symbol))
            r += 1
            if r >= 10:
                r = 0
                c += 1


        
           
        self.layout.addWidget(crypto_head_label)
        self.layout.addLayout(self.crypto_name_layout)
        self.layout.addWidget(attr_head_label)
        self.layout.addLayout(self.checkbox_layout)
        


       
        self.layout.addWidget(self.table)
    
    def populate_table(self, columns, selected_coins):
        self.table.setRowCount(len(selected_coins))  
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)
        self.table.resizeColumnsToContents()
      
        for index, coin_name in enumerate(selected_coins):
            # item = QtWidgets.QTableWidgetItem(str(coin_name))
            # self.table.setItem(index,0 item)
            for index_2, column in enumerate(columns):
                if column == "image":
                 
                    coin_data = get_coin_by_symbol(coin_name)
                    image_url = coin_data.image

                
                    response = requests.get(image_url)
                    image_data = response.content

                    
                    
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(image_data)
                     
                   
                    item = QtWidgets.QTableWidgetItem()
                   
                    item.setIcon(QtGui.QIcon(pixmap))

                   

                    self.table.setItem(index, index_2, item)
                else:
                  
                    coin_data = get_coin_by_symbol(coin_name)
                    column_data = getattr(coin_data, column, "") 
        
                    item = QtWidgets.QTableWidgetItem(str(column_data))
               
                    self.table.setItem(index, index_2, item)

    def update_table(self, param):

        self.selected_attr = [attr for attr in self.check_boxes if self.check_boxes[attr].isChecked()]

        self.selected_coins = [checkbox.text() for checkbox in self.name_checkboxes if checkbox.isChecked()]


        self.populate_table(self.selected_attr, self.selected_coins)
    

    
    def send_mail_on_clicked(self):
        try:
            html = html_generator(self.selected_coins,self.selected_attr)
            receiver_email = self.email_input.text()
            if send_email(receiver_email,html) == True:
                QtWidgets.QMessageBox.information(self, "Success", "Email sent successfully!")

        except AttributeError :
            QtWidgets.QMessageBox.critical(self, "Error", f"Please provide an email")

    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    widget = MyWidget()
    app.setStyleSheet(
"""
QWidget {
font-family: Verdana, Geneva, sans-serif;

color: #000000;
font-weight: normal;
text-decoration: none;
font-style: normal;
font-variant: normal;


background-color: #d3ebf4;
}



"""
    )
    widget.resize(1200, 1000)
    widget.setWindowTitle("Cryptocurrency Rates")
    widget.setWindowIcon(QtGui.QIcon("crypto_exchange_rates/bitcoin.png"))
    widget.show()

    sys.exit(app.exec())
