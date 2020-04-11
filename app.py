import copy
import sys

from PyQt5.uic.uiparser import QtWidgets

import app_settings
from PyQt5 import QtWidgets, QtGui
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
    error_flag = 0
    macro_tact_shift = 0

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("mainwindow.ui", self)
        # ____Settings_tab_init____
        self.comboBox_arch.currentTextChanged.connect(self.arch_changed)
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
        # ____Macro_tab_init____
        for template in app_settings.Code_Templates.keys():
            self.comboBox_macro_template.addItem(template)
        self.pushButton_simulate.clicked.connect(self.simulate)
        self.textEdit_macro.mouseReleaseEvent = self.clear_color
        self.set_enabled_second_pair(0)
        self.tableWidget_macro.setColumnCount(4)
        self.tableWidget_macro.setHorizontalHeaderLabels(('Макро-операция', 'Операнд 1', ' Операнд 2', 'Такт'))
        self.tableWidget_macro.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.comboBox_macro_template.currentTextChanged.connect(self.template_changed)

        self.show()

    # Main button to start simulation
    def simulate(self):
        if self.comboBox_arch.currentText() == 'Своя':
            current_settings = User_settings
        else:
            current_settings = Arch_Dict[self.comboBox_arch.currentText()]
        if self.code_check(self.textEdit_macro.toPlainText()):
            self.fill_macro_table(current_settings)
        else:
            return 0

    # ____Settings tab functions____

    def arch_changed(self):
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

    def template_changed(self):
        sender = self.sender()
        if sender.currentText() != '':
            self.textEdit_macro.setReadOnly(1)
            self.textEdit_macro.clear()
            self.textEdit_macro.setPlainText(app_settings.Code_Templates[sender.currentText()])
        else:
            self.textEdit_macro.setReadOnly(0)

    def code_check(self, code):
        self.textEdit_macro.clear()
        for line in code.splitlines():
            words = line.split(' ')
            if (words[0] and words[0].upper() not in app_settings.Macro_command_list) and \
                    not (words[0][0] == '.' and words[0][-1] == ':'):
                self.textEdit_macro.appendHtml(f"<span style='background-color: red;'>{line}</p>")
                self.error_flag = 1
            else:
                self.textEdit_macro.appendHtml(f"<span style='background-color: white;'>{line}</p>")
        return not self.error_flag

    def clear_color(self, event):
        if self.error_flag:
            text = self.textEdit_macro.toPlainText()
            self.textEdit_macro.clear()
            for line in text.splitlines():
                self.textEdit_macro.appendHtml(f"<span style='background-color: white;'>{line}</p>")
            self.error_flag = 0

    def fill_macro_table(self, settings):
        self.macro_tact_shift = 0
        self.tableWidget_macro.clearContents()
        self.tableWidget_macro.setRowCount(0)
        code_lines = self.textEdit_macro.toPlainText().splitlines()
        for number, command in enumerate(code_lines):
            if command.split(' ')[0][0] != '.':
                row_count = self.tableWidget_macro.rowCount()
                self.tableWidget_macro.insertRow(row_count)
                self.tableWidget_macro.setItem(row_count, 0, QtWidgets.QTableWidgetItem(command.split(' ')[0].upper()))
                try:
                    self.tableWidget_macro.setItem(
                        row_count, 1, QtWidgets.QTableWidgetItem(command.split(' ', 1)[1].split(',')[0].upper()))
                except IndexError:
                    self.tableWidget_macro.setItem(row_count, 1, QtWidgets.QTableWidgetItem('-'))
                try:
                    self.tableWidget_macro.setItem(row_count, 2,
                                                   QtWidgets.QTableWidgetItem(command.split(', ')[1].upper()))
                except IndexError:
                    self.tableWidget_macro.setItem(row_count, 2, QtWidgets.QTableWidgetItem('-'))
                self.tableWidget_macro.setItem(
                    row_count, 3, QtWidgets.QTableWidgetItem
                    (str(1 + (self.tableWidget_macro.rowCount() - self.macro_tact_shift - 1) // 4)))
                if self.checkBox_arch_macro.isChecked():
                    if row_count != 0:
                        current_op = [self.tableWidget_macro.item(row_count, 0),
                                      self.tableWidget_macro.item(row_count, 1),
                                      self.tableWidget_macro.item(row_count, 2),
                                      self.tableWidget_macro.item(row_count, 3),
                                      row_count]
                        self.perform_macro_fusion(settings, previous_op, current_op)
                        previous_op = current_op
                    else:
                        previous_op = [self.tableWidget_macro.item(row_count, 0),
                                       self.tableWidget_macro.item(row_count, 1),
                                       self.tableWidget_macro.item(row_count, 2),
                                       self.tableWidget_macro.item(row_count, 3),
                                       row_count]

    def perform_macro_fusion(self, fusion_settings, first_op, second_op):
        if fusion_settings['Macro_Conditions']['Transfer'] == 1 and \
                first_op[0].text() in fusion_settings['Macro_Pairs'] and \
                first_op[3].text() != second_op[3].text():
            first_op[3] = QtWidgets.QTableWidgetItem(str(second_op[3].text()))
            self.tableWidget_macro.item(first_op[4], 3).setText(second_op[3].text())
            self.macro_tact_shift -= 1
        op_types = self.get_operands_type(first_op[1].text(), first_op[2].text())
        if (first_op[0].text() in fusion_settings['Macro_Pairs'] and
            second_op[0].text() in fusion_settings['Macro_Pairs'][first_op[0].text()] and
            fusion_settings['Macro_Pairs'][first_op[0].text()][second_op[0].text()] == 1) and \
                (op_types in fusion_settings['Macro_Operands'] and
                 fusion_settings['Macro_Operands'][op_types] == 1) and \
                (fusion_settings['Macro_Conditions']['64_Bit_Mode'] == 1 or
                 (first_op[1].text() not in app_settings.Register_dict['64_bit']
                  and first_op[2].text() not in app_settings.Register_dict['64_bit'])) and \
                (fusion_settings['Macro_Conditions']['32_Bit_Mode'] == 1 or
                 (first_op[1].text() not in app_settings.Register_dict['32_bit']
                  and first_op[2].text() not in app_settings.Register_dict['32_bit'])) and \
                (fusion_settings['Macro_Conditions']['16_Bit_Mode'] == 1 or
                 (first_op[1].text() not in app_settings.Register_dict['16_bit']
                  and first_op[2].text() not in app_settings.Register_dict['16_bit'])):
            tact_fusions, current_tact, current_row = 0, int(first_op[3].text()), first_op[4]
            while tact_fusions != 2 and current_tact == int(first_op[3].text()) and current_row > 0:
                if self.tableWidget_macro.item(current_row, 3).background() != QtGui.QColor(0, 0, 0):
                    tact_fusions += 0.5
                    #print('HEY')
                current_row -= 1
                current_tact = int(self.tableWidget_macro.item(current_row, 3).text())
            if (fusion_settings['Macro_Conditions']['Two_Pairs'] == 0 and tact_fusions == 0) or \
                (fusion_settings['Macro_Conditions']['Two_Pairs'] == 1 and tact_fusions < 2):
                if fusion_settings['Macro_Conditions']['Transfer'] == 0 and first_op[3].text() != second_op[3].text():
                    second_op[3] = QtWidgets.QTableWidgetItem(first_op[3].text())
                    self.tableWidget_macro.setItem(second_op[4], 3, QtWidgets.QTableWidgetItem(first_op[3].text()))
                self.macro_tact_shift += 1
                for i in range(4):
                    self.tableWidget_macro.item(first_op[4], i).setBackground(QtGui.QColor(255, 255, 0))
                    self.tableWidget_macro.item(second_op[4], i).setBackground(QtGui.QColor(255, 255, 0))
        # TODO

    @staticmethod
    def get_operands_type(op1, op2):
        result = ''
        if (op1 in app_settings.Register_dict['64_bit'] or op1 in app_settings.Register_dict['32_bit']
                or op1 in app_settings.Register_dict['16_bit'] or op1 in app_settings.Register_dict['8_bit']):
            result += 'Reg'
        elif op1.isdigit():
            result += 'Imm'
        elif '[' in op1:
            result += 'Mem'
        elif 'RIP' in op1:
            result += 'Rip'
        else:
            return 'none'
        if (op2 in app_settings.Register_dict['64_bit'] or op2 in app_settings.Register_dict['32_bit']
                or op2 in app_settings.Register_dict['16_bit'] or op2 in app_settings.Register_dict['8_bit']):
            result += '_Reg'
        elif op2.isdigit():
            result += '_Imm'
        elif '[' in op2:
            result += '_Mem'
        elif 'RIP' in op2:
            result += '_Rip'
        else:
            return result
        return result


app = QtWidgets.QApplication(sys.argv)
window = Ui()
sys.exit(app.exec())
