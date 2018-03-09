# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payloaddlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import marsmission as mmc
import rocket as mmr

class Ui_Dialog(object):
    mm=[]
    mr=[]
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(400, 510)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 450, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 321, 411))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 121, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 121, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 121, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 320, 121, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 360, 121, 21))
        self.label_9.setObjectName("label_9")
        self.txted_o2 = QtWidgets.QTextEdit(self.groupBox)
        self.txted_o2.setEnabled(False)
        self.txted_o2.setGeometry(QtCore.QRect(190, 30, 104, 31))
        self.txted_o2.setObjectName("txted_o2")
        self.txted_h20 = QtWidgets.QTextEdit(self.groupBox)
        self.txted_h20.setEnabled(False)
        self.txted_h20.setGeometry(QtCore.QRect(190, 70, 104, 31))
        self.txted_h20.setObjectName("txted_h20")
        self.txted_plant = QtWidgets.QTextEdit(self.groupBox)
        self.txted_plant.setEnabled(False)
        self.txted_plant.setGeometry(QtCore.QRect(190, 150, 104, 31))
        self.txted_plant.setObjectName("txted_plant")
        self.txted_food = QtWidgets.QTextEdit(self.groupBox)
        self.txted_food.setEnabled(False)
        self.txted_food.setGeometry(QtCore.QRect(190, 110, 104, 31))
        self.txted_food.setObjectName("txted_food")
        self.txted_fuel = QtWidgets.QTextEdit(self.groupBox)
        self.txted_fuel.setEnabled(False)
        self.txted_fuel.setGeometry(QtCore.QRect(190, 230, 104, 31))
        self.txted_fuel.setObjectName("txted_fuel")
        self.txted_rover = QtWidgets.QTextEdit(self.groupBox)
        self.txted_rover.setEnabled(False)
        self.txted_rover.setGeometry(QtCore.QRect(190, 270, 104, 31))
        self.txted_rover.setObjectName("txted_rover")
        self.txted_crew = QtWidgets.QTextEdit(self.groupBox)
        self.txted_crew.setEnabled(False)
        self.txted_crew.setGeometry(QtCore.QRect(190, 310, 104, 31))
        self.txted_crew.setObjectName("txted_crew")
        self.txted_habitat = QtWidgets.QTextEdit(self.groupBox)
        self.txted_habitat.setEnabled(False)
        self.txted_habitat.setGeometry(QtCore.QRect(190, 190, 104, 31))
        self.txted_habitat.setObjectName("txted_habitat")
        self.txted_extras = QtWidgets.QTextEdit(self.groupBox)
        self.txted_extras.setEnabled(False)
        self.txted_extras.setGeometry(QtCore.QRect(190, 350, 104, 31))
        self.txted_extras.setObjectName("txted_extras")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setmm(self, mm,mr):
        self.mm=mm
        self.mr=mr
        
        var=mr.payload[mmr.payld.OXY]
        self.txted_o2.setText(str(format(var,'.3f')))		
        var=mr.payload[mmr.payld.H2O]
        self.txted_h20.setText(str(format(var,'.3f')))	
        var=mr.payload[mmr.payld.FOOD]
        self.txted_food.setText(str(format(var,'.3f')))
        var=mr.payload[mmr.payld.PLNT]
        self.txted_plant.setText(str(format(var,'.3f')))
        var=mr.payload[mmr.payld.HAB]
        self.txted_habitat.setText(str(format(var,'.3f')))        
        var=mr.payload[mmr.payld.CREW]
        self.txted_crew.setText(str(format(var,'.3f')))        
        var=mr.payload[mmr.payld.ROV]
        self.txted_rover.setText(str(format(var,'.3f'))) 
        var=mr.payload[mmr.payld.FUEL]
        self.txted_fuel.setText(str(format(var,'.3f'))) 
        var=mr.payload[mmr.payld.EXTRAS]
        self.txted_extras.setText(str(format(var,'.3f')))        
   
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Payload"))
        self.groupBox.setTitle(_translate("Dialog", "Payload"))
        self.label.setText(_translate("Dialog", "Oxygen"))
        self.label_2.setText(_translate("Dialog", "Water"))
        self.label_3.setText(_translate("Dialog", "Plant"))
        self.label_4.setText(_translate("Dialog", "Food"))
        self.label_5.setText(_translate("Dialog", "Fuel"))
        self.label_6.setText(_translate("Dialog", "Habitat"))
        self.label_7.setText(_translate("Dialog", "Rover"))
        self.label_8.setText(_translate("Dialog", "Crew"))
        self.label_9.setText(_translate("Dialog", "Extra Supplies"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

