import copy
import sys

from PyQt5.uic.uiparser import QtWidgets

import app_settings
from PyQt5 import QtWidgets
from PyQt5 import uic

User_settings = copy.deepcopy(app_settings.Template_settings)

Arch_Dict = {
    'Pentium M': app_settings.Pentium_M_settings,
    'Core 2': app_settings.Core_2_settings,
    'Nehalem': app_settings.Nehalem_settings,
    'Sandy Bridge': app_settings.Sandy_Bridge_settings,
    'Ivy Bridge': app_settings.Ivy_Bridge_settings,
    'Haswell': app_settings.Haswell_settings,
    'Broadwell': app_settings.Broadwell_settings,
    'Skylake': app_settings.Skylake_settings
}


class Ui(QtWidgets.QMainWindow):
    current_radio = 'none'

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("mainwindow.ui", self)
        self.comboBox_arch.currentTextChanged.connect(self.arch_change)
        for radio in self.scrollArea_macro_first_pair.findChildren(QtWidgets.QRadioButton):
            radio.toggled.connect(self.show_second_operators)
        for box in self.scrollArea_macro_second_pair.findChildren(QtWidgets.QCheckBox):
            box.toggled.connect(self.second_operator_change_state)
        self.checkBox_arch_macro.stateChanged.connect(self.macro_fusion_change_state)
        self.checkBox_arch_micro.stateChanged.connect(self.micro_fusion_change_state)
        for box in self.scrollArea_macro_operands.findChildren(QtWidgets.QCheckBox):
            box.stateChanged.connect(self.macro_operands_change_state)
        for box in self.scrollArea_macro_conditions.findChildren(QtWidgets.QCheckBox):
            box.stateChanged.connect(self.macro_conditions_change_state)
        for box in self.scrollArea_micro_pairs.findChildren(QtWidgets.QCheckBox):
            box.stateChanged.connect(self.micro_pairs_change_state)
        for box in self.scrollArea_micro_conditions.findChildren(QtWidgets.QCheckBox):
            box.stateChanged.connect(self.micro_conditions_change_state)
        self.pushButton_simulate.clicked.connect(self.simulate)
        self.textEdit_macro.mousePressEvent = self.clear_color
        self.set_enabled_second_pair(0)
        self.tableWidget_macro.setColumnCount(4)
        self.tableWidget_macro.setHorizontalHeaderLabels(('Макро-операция', 'Операнд 1', ' Операнд 2', 'Такт'))
        self.tableWidget_macro.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.show()

    # Main button to start simulation
    def simulate(self):
        if self.comboBox_arch.currentText() == 'Своя':
            current_settings = User_settings
        else:
            current_settings = Arch_Dict[self.comboBox_arch.currentText()]
        if self.code_check(self.textEdit_macro.toPlainText()):
            print(current_settings)
        else:
            return 0
        self.fill_macro_table()

    # ____Settings tab functions____

    def arch_change(self):
        sender = self.sender()
        last_item = sender.property('last_item')
        if sender.currentText() != 'Своя':
            current_dict = Arch_Dict[sender.currentText()]
            for box in self.scrollArea_macro_conditions.findChildren(QtWidgets.QCheckBox):
                box.setChecked(current_dict['Macro_Conditions'][box.objectName()[9:]])
            for box in self.scrollArea_micro_pairs.findChildren(QtWidgets.QCheckBox):
                box.setChecked(current_dict['Micro_Pairs'][box.objectName()[9:]])
            for box in self.scrollArea_micro_conditions.findChildren(QtWidgets.QCheckBox):
                box.setChecked(current_dict['Micro_Conditions'][box.objectName()[15:]])
            for box in self.scrollArea_macro_operands.findChildren(QtWidgets.QCheckBox):
                box.setChecked(current_dict['Macro_Operands'][box.objectName()[9:]])
            self.checkBox_arch_macro.setChecked(current_dict['Macro_Micro']['Macro'])
            self.checkBox_arch_micro.setChecked(current_dict['Macro_Micro']['Micro'])
            self.set_enabled_all(0)
        else:
            self.set_enabled_all(1)
            if last_item != 'Своя' or 'None':
                global User_settings
                User_settings = copy.deepcopy(Arch_Dict[last_item])
        self.clear_second_operators()
        sender.setProperty('last_item', sender.currentText())

    def macro_fusion_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя':
            User_settings['Macro_Micro']['Macro'] = int(sender.isChecked())

    def micro_fusion_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя':
            User_settings['Macro_Micro']['Micro'] = int(sender.isChecked())

    def second_operator_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' and self.current_radio != 'none':
            User_settings['Macro_Pairs'][self.current_radio][sender.objectName()[9:]] = int(sender.isChecked())

    def macro_operands_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя':
            User_settings['Macro_Operands'][sender.objectName()[9:]] = int(sender.isChecked())

    def macro_conditions_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя':
            User_settings['Macro_Conditions'][sender.objectName()[9:]] = int(sender.isChecked())

    def micro_conditions_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя':
            User_settings['Micro_Conditions'][sender.objectName()[15:]] = int(sender.isChecked())

    def micro_pairs_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя':
            User_settings['Micro_Pairs'][sender.objectName()[9:]] = int(sender.isChecked())

    def show_second_operators(self):
        sender = self.sender()
        self.current_radio = sender.objectName()[12:]
        if self.comboBox_arch.currentText() == 'Своя':
            current_dict = User_settings
            self.set_enabled_second_pair(1)
        else:
            current_dict = Arch_Dict[self.comboBox_arch.currentText()]
        if sender.isChecked():
            for box in self.scrollArea_macro_second_pair.findChildren(QtWidgets.QCheckBox):
                box.setChecked(current_dict['Macro_Pairs'][sender.objectName()[12:]][box.objectName()[9:]])

    def clear_second_operators(self):
        for radio in self.scrollArea_macro_first_pair.findChildren(QtWidgets.QRadioButton):
            if radio.isChecked():
                radio.setAutoExclusive(0)
                radio.setChecked(0)
                radio.setAutoExclusive(1)
        for box in self.scrollArea_macro_second_pair.findChildren(QtWidgets.QCheckBox):
            box.setChecked(0)
        self.current_radio = 'none'
        self.set_enabled_second_pair(0)

    def set_enabled_all(self, state):
        for box in self.scrollArea_macro_second_pair.findChildren(QtWidgets.QCheckBox):
            box.setEnabled(state)
        for box in self.scrollArea_macro_conditions.findChildren(QtWidgets.QCheckBox):
            box.setEnabled(state)
        for box in self.scrollArea_micro_pairs.findChildren(QtWidgets.QCheckBox):
            box.setEnabled(state)
        for box in self.scrollArea_macro_operands.findChildren(QtWidgets.QCheckBox):
            box.setEnabled(state)
        for box in self.scrollArea_micro_conditions.findChildren(QtWidgets.QCheckBox):
            box.setEnabled(state)
        self.checkBox_arch_macro.setEnabled(state)
        self.checkBox_arch_micro.setEnabled(state)

    def set_enabled_second_pair(self, state):
        for box in self.scrollArea_macro_second_pair.findChildren(QtWidgets.QCheckBox):
            box.setEnabled(state)

    # ____Macro tab functions____

    def code_check(self, code):
        flag = 1
        self.textEdit_macro.clear()
        for line in code.splitlines():
            words = line.split(' ')
            if words[0] and words[0].upper() not in app_settings.Macro_command_list:
                self.textEdit_macro.appendHtml(f"<span style='background-color: red;'>{line}</p>")
                flag = 0
            else:
                self.textEdit_macro.appendHtml(f"<span style='background-color: white;'>{line}</p>")
        return flag

    def clear_color(self, event):
        text = self.textEdit_macro.toPlainText()
        self.textEdit_macro.clear()
        for line in text.splitlines():
            self.textEdit_macro.appendHtml(f"<span style='background-color: white;'>{line}</p>")

    def fill_macro_table(self):
        code_lines = self.textEdit_macro.toPlainText().splitlines()
        self.tableWidget_macro.setRowCount(len(code_lines))
        tact = 1
        for number, command in enumerate(code_lines):
            self.tableWidget_macro.setItem(number, 0, QtWidgets.QTableWidgetItem(command.split(' ')[0].upper()))
            try:
                self.tableWidget_macro.setItem(number, 1, QtWidgets.QTableWidgetItem(command.split(' ', 1)[1].split(',')[0].upper()))
                #if command.split(' ')[1][-1] == ',':
                 #   self.tableWidget_macro.setItem(number, 1, QtWidgets.QTableWidgetItem(command.split(' ')[1][:-1].upper()))
            except IndexError:
                self.tableWidget_macro.setItem(number, 1, QtWidgets.QTableWidgetItem('-'))
            try:
                self.tableWidget_macro.setItem(number, 2, QtWidgets.QTableWidgetItem(command.split(',')[1].upper()))
            except IndexError:
                self.tableWidget_macro.setItem(number, 2, QtWidgets.QTableWidgetItem('-'))
            self.tableWidget_macro.setItem(number, 3, QtWidgets.QTableWidgetItem(str(tact + number // 4)))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
sys.exit(app.exec())
