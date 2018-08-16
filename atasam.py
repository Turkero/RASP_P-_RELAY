import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QApplication, QLabel, QPushButton,QLineEdit, QCheckBox)
from PyQt5.QtGui import * 

#initilize pins for 
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(11,0)
GPIO.output(12,0)
GPIO.output(13,0)
GPIO.output(15,0)
pin = [11,12,13,15]


class led(object):
  def __init__(self, name, color):
    self.name = name
    self.color = color


ledx = ["led1","led2","led3","led4"]
ledx[0] = led("1","red")
ledx[1] = led("2","red")
ledx[2] = led("3","red")
ledx[3] = led("4","red")

class window(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()


#define initilize the leds as red leds.

	def init_ui(self):
		self.red = QPixmap('red.png')
		self.green = QPixmap('green.png')
		self.ledy = []

		for i in ledx:
			i = QLabel()
			i.setPixmap(self.red.scaled(100,100))
			self.ledy.append(i)




#LineEdit and Button are defined

		self.t = QLineEdit()
		self.b = QPushButton("PUSH")



#positioning
#putting leds
		hbox1 = QHBoxLayout()
		for i in self.ledy:
			hbox1.addWidget(i)

#putting button and lineedit
		hbox2 = QHBoxLayout()
		hbox2.addStretch()
		hbox2.addWidget(self.t)
		hbox2.addWidget(self.b)

#put horizontal widgets to vertical
		vbox = QVBoxLayout()
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		
		self.setLayout(vbox)
		

#clicked fonction
		self.b.clicked.connect(lambda: self.btn_clk(self.t))


		self.show()

	def change_color(self,i):
		if ledx[i].color == "red":
			ledx[i].color = "green"
			self.ledy[i].setPixmap(self.green.scaled(100,100))
			GPIO.output(pin[i],1)
			print("yak")
		else:
			ledx[i].color = "red"
			self.ledy[i].setPixmap(self.red.scaled(100,100))
			GPIO.output(pin[i],0)
			print("yakma")



	def btn_clk(self,t):
		print("basildi")
		if t.text() == "1":
			print("1")
			self.change_color(0)
		elif t.text() == "2":
			print("2")
			self.change_color(1)
		elif t.text() == "3":
			print("3")
			self.change_color(2)
		elif t.text() == "4":
			print("4")
			self.change_color(3)






app = QApplication(sys.argv)
a_window = window()
sys.exit(app.exec_())



# def window():
# 	app = QtWidgets.QApplication(sys.argv)
# 	w = QtWidgets.QWidget()
# 	l1 = QtWidgets.QLabel(w)
# 	l1 = QtWidgets.QLabel(w)
# 	l1.setText("hello")
# 	l2.
# 	l1.move(50,50)
# 	w.setWindowTitle("atasam1")
# 	w.setGeometry(300,300,300,300)
# 	w.show()
# 	sys.exit(app.exec_())

# window()
