import copy
import os
import sys

from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic.uiparser import QtWidgets
from mainwindow import Ui_MainWindow
import app_settings
from PyQt5 import QtWidgets, QtGui

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

Micro_Dict = {
    'Pentium M': app_settings.Macro_micro_dict,
    'Core 2': app_settings.Macro_micro_dict_Core_2,
    'Nehalem': app_settings.Macro_micro_dict_Nehalem,
    'Sandy Bridge': app_settings.Macro_micro_dict_Sandy_Bridge,
    'Ivy Bridge': app_settings.Macro_micro_dict_Ivy_Bridge,
    'Haswell': app_settings.Macro_micro_dict_Haswell,
    'Broadwell': app_settings.Macro_micro_dict_Broadwell,
    'Skylake': app_settings.Macro_micro_dict_Skylake
}

Code_Dict = {}


class Ui(QtWidgets.QMainWindow, Ui_MainWindow):
    current_radio = 'none'
    error_flag = 0
    macro_tact_shift = 0
    current_language = 'ru'

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_translate.clicked.connect(self.translate)
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
        self.pushButton_macro_import.clicked.connect(self.import_code)
        self.pushButton_simulate.clicked.connect(self.simulate)
        self.textEdit_macro.enterEvent = self.clear_color
        self.set_enabled_second_pair(0)
        self.tableWidget_macro.setColumnCount(4)
        self.tableWidget_macro.setHorizontalHeaderLabels(('Макро-операция', 'Операнд 1', ' Операнд 2', 'Такт'))
        self.tableWidget_macro.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.comboBox_macro_template.currentTextChanged.connect(self.template_changed)
        # ____Micro_tab_init____
        self.tableWidget_micro.setColumnCount(10)
        self.tableWidget_micro.setHorizontalHeaderLabels(('Макро-операция', 'Операнд 1', ' Операнд 2',
                                                          'READ', 'MODIFY', 'ADDRESS', 'WRITE',
                                                          'Unfused domain', 'Fused domain', 'Тип'))
        self.tableWidget_micro.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.show()

    def translate(self):
        if self.current_language == 'ru':
            self.current_language = 'en'
        else:
            self.current_language = 'ru'

        self.comboBox_macro_template.clear()
        self.comboBox_macro_template.addItem('')

        if self.current_language == 'ru':
            self.tableWidget_macro.setHorizontalHeaderLabels(('Макро-операция', 'Операнд 1', ' Операнд 2', 'Такт'))
            self.tableWidget_micro.setHorizontalHeaderLabels(('Макро-операция', 'Операнд 1', ' Операнд 2',
                                                              'READ', 'MODIFY', 'ADDRESS', 'WRITE',
                                                              'Unfused domain', 'Fused domain', 'Тип'))
            self.label_arch_settings.setText('Настройки архитектуры')
            self.label_arch_processor.setText('Архитектура процессора')
            self.checkBox_arch_macro.setText('Макро слияние')
            self.checkBox_arch_micro.setText('Микро слияние')
            self.label_user_arch.setText('Настройки своей архитектуры')
            self.label_user_micro.setText('Микро-операции из архитектуры')
            self.label_macro_fusion_settings.setText('Настройки слияния макро-операций')
            self.label_macro_pairs_settings.setText('Сливаемые пары операций')
            self.label_macro_first_pair.setText('Первая операция')
            self.label_macro_second_pair.setText('Вторая операция')
            self.label_macro_first_pair_operands.setText('Допустимые операнды первой операции')
            self.checkBox_Reg_Reg.setText('Регистр + Регистр')
            self.checkBox_Reg_Imm.setText('Регистр + Непосредственный операнд')
            self.checkBox_Reg_Mem.setText('Регистр + Память')
            self.checkBox_Reg_RIP.setText('Регистр + RIP Адрес')
            self.checkBox_Mem_Imm.setText('Память + Непосредственный операнд')
            self.checkBox_Mem_Reg.setText('Память + Регистр')
            self.checkBox_Reg.setText('Регистр')
            self.checkBox_Mem.setText('Память')
            self.checkBox_RIP.setText('RIP Адрес')
            self.label_macro_conditions.setText('Условия')
            self.checkBox_Two_Pairs.setText('Две пары в такт')
            self.checkBox_Transfer.setText(
                'Перенос первой инструкции на следующий такт при попадании на последний декодер')
            self.label_macro_mode.setText('Режимы слияния')
            self.checkBox_16_Bit_Mode.setText('16 бит')
            self.checkBox_32_Bit_Mode.setText('32 бит')
            self.checkBox_64_Bit_Mode.setText('64 бит')
            self.label_micro_fusion_settings.setText('Настройки слияния микро-операций')
            self.label_micro_pairs_settings.setText('Сливаемые пары операций')
            self.checkBox_Address_Write.setText('Вычисление адреса + Запись данных')
            self.checkBox_Read_Modify.setText('Чтение данных + Изменение данных')
            self.label_micro_conditions.setText('Условия')
            self.checkBox_micro_Combo.setText('Слияние двух типов пар операций')
            self.checkBox_micro_Rip_Imm.setText('RIP и непосредственный операнд в одной иструкции')
            self.label_micro_operated_registers.setText('Оперируемые регистры и операнды')
            self.checkBox_micro_Reg.setText('Регистры')
            self.checkBox_micro_Mem.setText('Память')
            self.checkBox_micro_Mmx.setText('MMX')
            self.checkBox_micro_Xmm.setText('XMM')
            self.checkBox_micro_Rip.setText('RIP Адрес')
            self.checkBox_micro_Imm.setText('Непосредственные операнды')
            self.tabWidget.setTabText(0, 'Параметры')
            self.tabWidget.setTabText(1, 'Макро уровень')
            self.tabWidget.setTabText(2, 'Микро уровень')
            self.label_macro_template.setText('Вариант программного кода')
            self.label.setText('Импорт вариантов')
            self.pushButton_macro_import.setText('Файл...')
            self.pushButton_simulate.setText('Моделировать')
            self.comboBox_arch.setItemText(0, 'Своя')
        else:
            self.tableWidget_macro.setHorizontalHeaderLabels(('Macro-operation', 'Operand 1', ' Operand 2', 'Tact'))
            self.tableWidget_micro.setHorizontalHeaderLabels(('Macro-operation', 'Operand 1', ' Operand 2',
                                                              'READ', 'MODIFY', 'ADDRESS', 'WRITE',
                                                              'Unfused domain', 'Fused domain', 'Type'))
            self.label_arch_settings.setText('Architecture settings')
            self.label_arch_processor.setText('Processor architecture')
            self.checkBox_arch_macro.setText('Macro fusion')
            self.checkBox_arch_micro.setText('Micro fusion')
            self.label_user_arch.setText('Custom architecture settings')
            self.label_user_micro.setText('Micro-operations used from')
            self.label_macro_fusion_settings.setText('Macro fusion settings')
            self.label_macro_pairs_settings.setText('Fuseable operation pairs')
            self.label_macro_first_pair.setText('First operation')
            self.label_macro_second_pair.setText('Second operation')
            self.label_macro_first_pair_operands.setText('Valid operands for first operation')
            self.checkBox_Reg_Reg.setText('Register + Register')
            self.checkBox_Reg_Imm.setText('Register + Immediate operand')
            self.checkBox_Reg_Mem.setText('Register + Memory')
            self.checkBox_Reg_RIP.setText('Register + RIP Address')
            self.checkBox_Mem_Imm.setText('Memory + Immediate operand')
            self.checkBox_Mem_Reg.setText('Memory + Register')
            self.checkBox_Reg.setText('Register')
            self.checkBox_Mem.setText('Memory')
            self.checkBox_RIP.setText('RIP Address')
            self.label_macro_conditions.setText('Conditions')
            self.checkBox_Two_Pairs.setText('Two pairs in one tact')
            self.checkBox_Transfer.setText(
                'Transferring the first instruction to the next tact when it get on the last decoder')
            self.label_macro_mode.setText('Fusion modes')
            self.checkBox_16_Bit_Mode.setText('16 bit')
            self.checkBox_32_Bit_Mode.setText('32 bit')
            self.checkBox_64_Bit_Mode.setText('64 bit')
            self.label_micro_fusion_settings.setText('Micro fusion settings')
            self.label_micro_pairs_settings.setText('Fuseable operation pairs')
            self.checkBox_Address_Write.setText('Address calculation + Data write')
            self.checkBox_Read_Modify.setText('Read data + Data modification')
            self.label_micro_conditions.setText('Conditions')
            self.checkBox_micro_Combo.setText('Fusion two types of operation pairs')
            self.checkBox_micro_Rip_Imm.setText('RIP and immediate operand in one instruction')
            self.label_micro_operated_registers.setText('Manageable registers and operands')
            self.checkBox_micro_Reg.setText('Registers')
            self.checkBox_micro_Mem.setText('Memory')
            self.checkBox_micro_Mmx.setText('MMX')
            self.checkBox_micro_Xmm.setText('XMM')
            self.checkBox_micro_Rip.setText('RIP Address')
            self.checkBox_micro_Imm.setText('Immediate operands')
            self.tabWidget.setTabText(0, 'Settings')
            self.tabWidget.setTabText(1, 'Macro level')
            self.tabWidget.setTabText(2, 'Micro level')
            self.label_macro_template.setText('Assembly code option')
            self.label.setText('Import options')
            self.pushButton_macro_import.setText('File...')
            self.pushButton_simulate.setText('Simulate')
            self.comboBox_arch.setItemText(0, 'Custom')

    # Main button to start simulation
    def simulate(self):
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
            current_settings = User_settings
        else:
            current_settings = Arch_Dict[self.comboBox_arch.currentText()]
        if self.code_check(self.textEdit_macro.toPlainText()):
            self.fill_macro_table(current_settings)
            self.fill_micro_table(current_settings)

    # ____Settings tab functions____

    def arch_changed(self):
        sender = self.sender()
        last_item = sender.property('last_item')
        if sender.currentText() != 'Своя' and self.comboBox_arch.currentText() != 'Custom':
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
            if last_item != 'Своя' and last_item is not None and last_item != 'Custom':

                global User_settings
                User_settings = copy.deepcopy(Arch_Dict[last_item])
        self.clear_second_operators()
        sender.setProperty('last_item', sender.currentText())

    def macro_fusion_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
            User_settings['Macro_Micro']['Macro'] = int(sender.isChecked())

    def micro_fusion_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
            User_settings['Macro_Micro']['Micro'] = int(sender.isChecked())

    def second_operator_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom' \
                and self.current_radio != 'none':
            User_settings['Macro_Pairs'][self.current_radio][sender.objectName()[9:]] = int(sender.isChecked())

    def macro_operands_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
            User_settings['Macro_Operands'][sender.objectName()[9:]] = int(sender.isChecked())

    def macro_conditions_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
            User_settings['Macro_Conditions'][sender.objectName()[9:]] = int(sender.isChecked())

    def micro_conditions_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
            User_settings['Micro_Conditions'][sender.objectName()[15:]] = int(sender.isChecked())

    def micro_pairs_change_state(self):
        sender = self.sender()
        global User_settings
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
            User_settings['Micro_Pairs'][sender.objectName()[9:]] = int(sender.isChecked())

    def show_second_operators(self):
        sender = self.sender()
        self.current_radio = sender.objectName()[12:]
        if self.comboBox_arch.currentText() == 'Своя' or self.comboBox_arch.currentText() == 'Custom':
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
        self.comboBox_arch_micro.setEnabled(state)

    def set_enabled_second_pair(self, state):
        for box in self.scrollArea_macro_second_pair.findChildren(QtWidgets.QCheckBox):
            box.setEnabled(state)

    # ____Macro tab functions____

    def import_code(self):
        if self.current_language == 'ru':
            filename = QFileDialog.getOpenFileName(self, 'Импорт вариантов кода', None, 'Текстовый файл (*.txt)')[0]
        else:
            filename = QFileDialog.getOpenFileName(self, 'Import code examples', None, 'Text file (*.txt)')[0]
        if os.path.isfile(str(filename)):
            file = open(filename, 'r')
            code = ''
            Code_Dict.clear()
            self.comboBox_macro_template.clear()
            self.comboBox_macro_template.addItem('')
            for line in file:
                if line == '\n':
                    if self.current_language == 'ru':
                        Code_Dict['Вариант ' + str(self.comboBox_macro_template.count())] = code
                        self.comboBox_macro_template.addItem('Вариант ' + str(self.comboBox_macro_template.count()))
                    else:
                        Code_Dict['Example ' + str(self.comboBox_macro_template.count())] = code
                        self.comboBox_macro_template.addItem('Example ' + str(self.comboBox_macro_template.count()))
                    code = ''
                else:
                    if line[0] != '#':
                        code += line
            if self.current_language == 'ru':
                Code_Dict['Вариант ' + str(self.comboBox_macro_template.count())] = code
                self.comboBox_macro_template.addItem('Вариант ' + str(self.comboBox_macro_template.count()))
            else:
                Code_Dict['Example ' + str(self.comboBox_macro_template.count())] = code
                self.comboBox_macro_template.addItem('Example ' + str(self.comboBox_macro_template.count()))
            file.close()

    def template_changed(self):
        sender = self.sender()
        if sender.currentText() != '':
            self.textEdit_macro.setReadOnly(1)
            self.textEdit_macro.clear()
            self.textEdit_macro.setPlainText(Code_Dict[sender.currentText()])
        else:
            self.textEdit_macro.setReadOnly(0)

    def code_check(self, code):
        self.textEdit_macro.clear()
        code_marks = []
        for line in code.splitlines():
            words = line.split('\t')
            local_error_flag = 0
            if words[0] != '' and ' ' not in words[0] and ',' not in words[0] and \
                    words[0][-1] == ':' and words[0][:-1].upper() not in code_marks:
                code_marks.append(words[0][:-1].upper())
            else:
                if words[0] != '':
                    self.error_flag, local_error_flag = 1, 1
            if len(words) < 3 and not(len(words) == 1 and words[0] != '' and words[0][-1] == ':'):
                self.error_flag, local_error_flag = 1, 1
            if len(words) > 2 and not local_error_flag:
                if words[1] == '' or ' ' in words[1] or ',' in words[1] or \
                        words[1].upper() not in app_settings.Macro_command_list:
                    self.error_flag, local_error_flag = 1, 1
                elif (words[1][0] == 'j' or words[1][0] == 'J') and (words[2].upper() + ':\t') not in code.upper():
                    self.error_flag, local_error_flag = 1, 1
            if len(words) > 2 and words[1][0] != 'j' and words[1][0] != 'J' and not local_error_flag:
                try:
                    if ' ' in words[2].split(', ')[0].upper() or ',' in words[2].split(', ')[0].upper() or \
                            self.get_operand_type_micro(words[2].split(', ')[0].upper()) == '-':
                        self.error_flag, local_error_flag = 1, 1
                except IndexError:
                    self.error_flag, local_error_flag = 1, 1
                try:
                    if ' ' in words[2].split(', ')[1].upper() or ',' in words[2].split(', ')[1].upper() or \
                            self.get_operand_type_micro(words[2].split(', ')[1].upper()) == '-':
                        self.error_flag, local_error_flag = 1, 1
                except IndexError:
                    self.error_flag, local_error_flag = self.error_flag, local_error_flag
            if local_error_flag:
                self.textEdit_macro.setTextBackgroundColor(QtGui.QColor("red"))
                self.textEdit_macro.append(line)
                self.textEdit_macro.setTextBackgroundColor(QtGui.QColor("white"))
            else:
                self.textEdit_macro.append(line)
        return not self.error_flag

    def clear_color(self, event):
        if self.error_flag:
            text = self.textEdit_macro.toPlainText()
            self.textEdit_macro.clear()
            for line in text.splitlines():
                self.textEdit_macro.append(line)
            self.error_flag = 0

    def fill_macro_table(self, settings):
        self.macro_tact_shift = 0
        self.tableWidget_macro.clearContents()
        self.tableWidget_macro.setRowCount(0)
        code_lines = self.textEdit_macro.toPlainText().splitlines()
        for number, command in enumerate(code_lines):
            if len(command.split('\t')) > 2:
                row_count = self.tableWidget_macro.rowCount()
                self.tableWidget_macro.insertRow(row_count)
                self.tableWidget_macro.setItem(row_count, 0, QtWidgets.QTableWidgetItem(command.split('\t')[1].upper()))
                try:
                    self.tableWidget_macro.setItem(
                        row_count, 1, QtWidgets.QTableWidgetItem(command.split('\t')[2].split(', ')[0].upper()))
                except IndexError:
                    self.tableWidget_macro.setItem(row_count, 1, QtWidgets.QTableWidgetItem('-'))
                try:
                    self.tableWidget_macro.setItem(row_count, 2, QtWidgets.QTableWidgetItem(command.split('\t')[2].
                                                                                            split(', ')[1].upper()))
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
                1 in fusion_settings['Macro_Pairs'][first_op[0].text()].values() and \
                first_op[3].text() != second_op[3].text():
            first_op[3] = QtWidgets.QTableWidgetItem(str(second_op[3].text()))
            self.tableWidget_macro.item(first_op[4], 3).setText(second_op[3].text())
            self.macro_tact_shift -= 1
        op_types = self.get_operands_type_macro(first_op[1].text(), first_op[2].text())
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
            while tact_fusions != 2 and current_tact == int(first_op[3].text()) and current_row >= 0:
                if self.tableWidget_macro.item(current_row, 3).background() == QtGui.QColor(255, 255, 0):
                    tact_fusions += 0.5
                current_row -= 1
                if current_row >= 0:
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

    @staticmethod
    def get_operands_type_macro(op1, op2):
        result = ''
        if (op1 in app_settings.Register_dict['64_bit']
                or op1 in app_settings.Register_dict['32_bit']
                or op1 in app_settings.Register_dict['16_bit']
                or op1 in app_settings.Register_dict['8_bit_h']
                or op1 in app_settings.Register_dict['8_bit_l']):
            result += 'Reg'
        elif op1.isdigit():
            result += 'Imm'
        elif '[' in op1:
            result += 'Mem'
        elif 'RIP' in op1:
            result += 'Rip'
        else:
            return 'none'
        if (op2 in app_settings.Register_dict['64_bit']
                or op2 in app_settings.Register_dict['32_bit']
                or op2 in app_settings.Register_dict['16_bit']
                or op2 in app_settings.Register_dict['8_bit_h']
                or op2 in app_settings.Register_dict['8_bit_l']):
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

    # ____Micro tab functions____

    def fill_micro_table(self, settings):
        self.tableWidget_micro.clearContents()
        self.tableWidget_micro.setRowCount(0)
        code_lines = self.textEdit_macro.toPlainText().splitlines()
        Default_Micro_Dict = app_settings.Macro_micro_dict
        for number, command in enumerate(code_lines):
            if len(command.split('\t')) > 2:
                row_count = self.tableWidget_micro.rowCount()
                self.tableWidget_micro.insertRow(row_count)
                self.tableWidget_micro.setItem(row_count, 0, QtWidgets.QTableWidgetItem(command.split('\t')[1].upper()))
                try:
                    self.tableWidget_micro.setItem(
                        row_count, 1, QtWidgets.QTableWidgetItem(self.get_operand_type_micro
                                                                 (command.split('\t')[2].split(', ')[0].upper())))
                except IndexError:
                    self.tableWidget_micro.setItem(row_count, 1, QtWidgets.QTableWidgetItem('-'))
                try:
                    self.tableWidget_micro.setItem(row_count, 2,
                                                   QtWidgets.QTableWidgetItem(self.get_operand_type_micro
                                                                              (command.split('\t')[2].
                                                                               split(', ')[1].upper())))
                except IndexError:
                    self.tableWidget_micro.setItem(row_count, 2, QtWidgets.QTableWidgetItem('-'))
                current_op = [self.tableWidget_micro.item(row_count, 0),
                              self.tableWidget_micro.item(row_count, 1),
                              self.tableWidget_micro.item(row_count, 2),
                              row_count]
                op1 = current_op[1].text()
                op2 = current_op[2].text()
                if self.comboBox_arch.currentText() != 'Своя' and self.comboBox_arch.currentText() != 'Custom':
                    Current_Micro_dict = Micro_Dict[self.comboBox_arch.currentText()]
                else:
                    Current_Micro_dict = Micro_Dict[self.comboBox_arch_micro.currentText()]
                if current_op[0].text()[0] == 'J':
                    op = 'Mrk'
                    if op not in Current_Micro_dict[current_op[0].text()]:
                        Current_Micro_dict = Default_Micro_Dict
                    if op in Current_Micro_dict[current_op[0].text()]:
                        self.tableWidget_micro.setItem(row_count, 3, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['READ'])))
                        self.tableWidget_micro.setItem(row_count, 4, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['MODIFY'])))
                        self.tableWidget_micro.setItem(row_count, 5, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['ADDRESS'])))
                        self.tableWidget_micro.setItem(row_count, 6, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['WRITE'])))
                        self.tableWidget_micro.setItem(row_count, 7, QtWidgets.QTableWidgetItem(str(
                            int(self.tableWidget_micro.item(row_count, 3).text()) +
                            int(self.tableWidget_micro.item(row_count, 4).text()) +
                            int(self.tableWidget_micro.item(row_count, 5).text()) +
                            int(self.tableWidget_micro.item(row_count, 6).text()))))
                    else:
                        for x in range(3, 10):
                            self.tableWidget_micro.setItem(row_count, x, QtWidgets.QTableWidgetItem('-'))
                elif op1 != '-' and op2 != '-':
                    op = (op1 + '_' + op2,
                          op1 + '_' + op2[:-1],
                          op1[:-1] + '_' + op2[:-1],
                          op1 + '_' + op2[:3],
                          op1[:3] + '_' + op2,
                          op1[:3] + '_' + op2[:3],
                          op1[:-1] + '_' + op2)
                    if not list(set(Current_Micro_dict[current_op[0].text()]) & set(op)):
                        Current_Micro_dict = Default_Micro_Dict
                        op = list(set(Current_Micro_dict[current_op[0].text()]) & set(op))
                    else:
                        op = list(set(Current_Micro_dict[current_op[0].text()]) & set(op))
                    if op:
                        op = op[0]
                        self.tableWidget_micro.setItem(row_count, 3, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['READ'])))
                        self.tableWidget_micro.setItem(row_count, 4, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['MODIFY'])))
                        self.tableWidget_micro.setItem(row_count, 5, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['ADDRESS'])))
                        self.tableWidget_micro.setItem(row_count, 6, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['WRITE'])))
                        self.tableWidget_micro.setItem(row_count, 7, QtWidgets.QTableWidgetItem(str(
                            int(self.tableWidget_micro.item(row_count, 3).text()) +
                            int(self.tableWidget_micro.item(row_count, 4).text()) +
                            int(self.tableWidget_micro.item(row_count, 5).text()) +
                            int(self.tableWidget_micro.item(row_count, 6).text()))))
                    else:
                        for x in range(3, 10):
                            self.tableWidget_micro.setItem(row_count, x, QtWidgets.QTableWidgetItem('-'))
                elif op1 != '-' and op2 == '-':
                    op = (op1, op1[:-1], op1[:3])
                    if not list(set(Current_Micro_dict[current_op[0].text()]) & set(op)):
                        Current_Micro_dict = Default_Micro_Dict
                        op = list(set(Current_Micro_dict[current_op[0].text()]) & set(op))
                    else:
                        op = list(set(Current_Micro_dict[current_op[0].text()]) & set(op))
                    if op:
                        op = op[0]
                        self.tableWidget_micro.setItem(row_count, 3, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['READ'])))
                        self.tableWidget_micro.setItem(row_count, 4, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['MODIFY'])))
                        self.tableWidget_micro.setItem(row_count, 5, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['ADDRESS'])))
                        self.tableWidget_micro.setItem(row_count, 6, QtWidgets.QTableWidgetItem(
                            str(Current_Micro_dict[current_op[0].text()][op]['WRITE'])))
                        self.tableWidget_micro.setItem(row_count, 7, QtWidgets.QTableWidgetItem(str(
                            int(self.tableWidget_micro.item(row_count, 3).text()) +
                            int(self.tableWidget_micro.item(row_count, 4).text()) +
                            int(self.tableWidget_micro.item(row_count, 5).text()) +
                            int(self.tableWidget_micro.item(row_count, 6).text()))))
                    else:
                        for x in range(3, 10):
                            self.tableWidget_micro.setItem(row_count, x, QtWidgets.QTableWidgetItem('-'))
                else:
                    for x in range(3, 10):
                        self.tableWidget_micro.setItem(row_count, x, QtWidgets.QTableWidgetItem('-'))

                if self.checkBox_arch_micro.isChecked():
                    if self.tableWidget_micro.item(row_count, 7).text() == '1':
                        self.tableWidget_micro.setItem(row_count, 8, QtWidgets.QTableWidgetItem('1'))
                        self.tableWidget_micro.setItem(row_count, 9, QtWidgets.QTableWidgetItem('-'))
                    else:
                        self.perform_micro_fusion(settings, current_op)
                else:
                    self.tableWidget_micro.setItem(row_count, 8, QtWidgets.QTableWidgetItem(
                        self.tableWidget_micro.item(row_count, 7).text()))
                    self.tableWidget_micro.setItem(row_count, 9, QtWidgets.QTableWidgetItem('-'))

                if self.tableWidget_macro.item(current_op[3], 3).background() == QtGui.QColor(255, 255, 0):
                    if self.tableWidget_macro.item(current_op[3], 0).text()[0] == 'J':
                        self.tableWidget_micro.setItem(row_count, 7, QtWidgets.QTableWidgetItem('1'))
                        self.tableWidget_micro.setItem(row_count, 8, QtWidgets.QTableWidgetItem('1'))
                        self.tableWidget_micro.setItem(row_count, 9, QtWidgets.QTableWidgetItem('Macro fusion'))
                        for x in range(0, 10):
                            self.tableWidget_micro.item(row_count, x).setBackground(QtGui.QColor(255, 255, 0))
                    else:
                        self.tableWidget_micro.setItem(row_count, 7, QtWidgets.QTableWidgetItem('-'))
                        self.tableWidget_micro.setItem(row_count, 8, QtWidgets.QTableWidgetItem('-'))
                        self.tableWidget_micro.setItem(row_count, 9, QtWidgets.QTableWidgetItem('-'))
                        for x in range(0, 10):
                            self.tableWidget_micro.item(row_count, x).setBackground(QtGui.QColor(255, 255, 0))

        row_count = self.tableWidget_micro.rowCount()

        fused_domain_sum, unfused_domain_sum = 0, 0
        for x in range(row_count):
            if self.tableWidget_micro.item(x, 7).text() != '-':
                unfused_domain_sum += int(self.tableWidget_micro.item(x, 7).text())
            if self.tableWidget_micro.item(x, 8).text() != '-':
                fused_domain_sum += int(self.tableWidget_micro.item(x, 8).text())
        if unfused_domain_sum != 0 and fused_domain_sum != 0:
            self.tableWidget_micro.insertRow(row_count)
            self.tableWidget_micro.setItem(row_count, 7, QtWidgets.QTableWidgetItem(str(unfused_domain_sum)))
            self.tableWidget_micro.setItem(row_count, 8, QtWidgets.QTableWidgetItem(str(fused_domain_sum)))

    def perform_micro_fusion(self, fusion_settings, current_op):
        if current_op[1].text()[0] != '.' and \
                fusion_settings['Micro_Conditions']['Rip_Imm'] != 1 and \
                ((current_op[1].text()[:3] != 'RIP' and current_op[2].text()[:3] != 'Imm') or
                 (current_op[2].text()[:3] != 'RIP' and current_op[1].text()[:3] != 'Imm')) and \
                (current_op[1].text() == '-' or fusion_settings['Micro_Conditions'][current_op[1].text()[:3]]) and \
                (current_op[2].text() == '-' or fusion_settings['Micro_Conditions'][current_op[2].text()[:3]]):
            if fusion_settings['Micro_Conditions']['Combo'] and \
                    (self.tableWidget_micro.item(current_op[3], 3).text() != '-'
                     and int(self.tableWidget_micro.item(current_op[3], 3).text()) > 0) and \
                    (self.tableWidget_micro.item(current_op[3], 4).text() != '-'
                     and int(self.tableWidget_micro.item(current_op[3], 4).text()) > 0) and \
                    (self.tableWidget_micro.item(current_op[3], 6).text() != '-'
                     and int(self.tableWidget_micro.item(current_op[3], 6).text()) > 0):
                self.tableWidget_micro.setItem(
                    current_op[3], 8,
                    QtWidgets.QTableWidgetItem(str(int(self.tableWidget_micro.item(current_op[3], 7).text()) - 2)))
                self.tableWidget_micro.setItem(current_op[3], 9,
                                               QtWidgets.QTableWidgetItem('Read Modify Address Write'))
            elif fusion_settings['Micro_Pairs']['Address_Write'] and \
                    (self.tableWidget_micro.item(current_op[3], 5).text() != '-'
                     and int(self.tableWidget_micro.item(current_op[3], 5).text()) > 0) and \
                    (self.tableWidget_micro.item(current_op[3], 6).text() != '-'
                     and int(self.tableWidget_micro.item(current_op[3], 6).text()) > 0):
                self.tableWidget_micro.setItem(
                    current_op[3], 8,
                    QtWidgets.QTableWidgetItem(str(int(self.tableWidget_micro.item(current_op[3], 7).text()) - 1)))
                self.tableWidget_micro.setItem(current_op[3], 9, QtWidgets.QTableWidgetItem('Address Write'))
            elif fusion_settings['Micro_Pairs']['Read_Modify'] and \
                    (self.tableWidget_micro.item(current_op[3], 3).text() != '-'
                     and int(self.tableWidget_micro.item(current_op[3], 3).text()) > 0) and \
                    (self.tableWidget_micro.item(current_op[3], 4).text() != '-'
                     and int(self.tableWidget_micro.item(current_op[3], 4).text())) > 0:
                self.tableWidget_micro.setItem(
                    current_op[3], 8,
                    QtWidgets.QTableWidgetItem(str(int(self.tableWidget_micro.item(current_op[3], 7).text()) - 1)))
                self.tableWidget_micro.setItem(current_op[3], 9, QtWidgets.QTableWidgetItem('Read Modify'))
            else:
                self.tableWidget_micro.setItem(current_op[3], 8, QtWidgets.QTableWidgetItem(
                    str(self.tableWidget_micro.item(current_op[3], 7).text())))
                self.tableWidget_micro.setItem(current_op[3], 9, QtWidgets.QTableWidgetItem('-'))
        else:
            self.tableWidget_micro.setItem(current_op[3], 8, QtWidgets.QTableWidgetItem(
                str(self.tableWidget_micro.item(current_op[3], 7).text())))
            self.tableWidget_micro.setItem(current_op[3], 9, QtWidgets.QTableWidgetItem('-'))

    @staticmethod
    def get_operand_type_micro(op):
        result = ''
        if (op in app_settings.Register_dict['64_bit']
                or op in app_settings.Register_dict['32_bit']
                or op in app_settings.Register_dict['16_bit']
                or op in app_settings.Register_dict['8_bit_h']
                or op in app_settings.Register_dict['8_bit_l']):
            if op in app_settings.Register_dict['64_bit']:
                result += 'Reg64'
            elif op in app_settings.Register_dict['32_bit']:
                result += 'Reg32'
            elif op in app_settings.Register_dict['16_bit']:
                result += 'Reg16'
            elif op in app_settings.Register_dict['8_bit_h']:
                result += 'Reg8h'
            elif op in app_settings.Register_dict['8_bit_l']:
                result += 'Reg8l'
            else:
                result += 'Reg'
        elif op.isdigit():
            result += 'Imm'
        elif '[' in op:
            if 'BYTE' in op:
                result += 'Mem8'
            elif '*' in op:
                result += 'Mem128'
            elif 'QWORD' in op:
                result += 'Mem64'
            elif 'DWORD' in op:
                result += 'Mem32'
            elif 'WORD' in op:
                result += 'Mem16'
            else:
                result += 'Mem'
        elif 'RIP' in op:
            result += 'Rip'
        elif 'XMM' in op:
            result += 'Xmm'
        elif 'MM' in op:
            result += 'Mmx'
        else:
            return '-'
        return result


# Launch
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.setStyle('')
sys.exit(app.exec())
