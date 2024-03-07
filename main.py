
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import sys
from usuario import Cliente
from Gui import Ui_mainWindow
from bot import Automacao

class Interface(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Interface, self).__init__(*args, **argvs)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
          # Criar uma instância da classe Cliente
        self.ui.pushButton.clicked.connect(self.button_action)
        self.ui.checkBox.stateChanged.connect(self.checar_box)
        self.ui.checkBox_2.stateChanged.connect(self.checar_box)
        self.ui.checkBox_3.stateChanged.connect(self.checar_box)
        self.ui.checkBox_4.stateChanged.connect(self.checar_box)
        self.ui.checkBox_5.stateChanged.connect(self.checar_box)
        self.ui.checkBox_6.stateChanged.connect(self.checar_box)
        self.ui.checkBox_7.stateChanged.connect(self.checar_box)
        self.ui.checkBox_8.stateChanged.connect(self.checar_box)
        self.ui.checkBox_9.stateChanged.connect(self.checar_box)
        self.ui.checkBox_10.stateChanged.connect(self.checar_box)

    def button_action(self):

        # Verifica se todos os campos de texto estão preenchidos
        if self.campos_preenchidos():
            automacao = Automacao()
            cliente = Cliente()  # Criar uma nova instância da classe Cliente
            cliente.nome_var = self.nome
            cliente.cpf_var = self.cpf
            cliente.cnpj_var = self.cnpj
            cliente.rg_var = self.rg
            cliente.email_var = self.email

            # Execute a automação apenas para as checkboxes marcadas
            if self.ui.checkBox.isChecked():
                automacao.site1_servicos_receita(cpf=self.cpf)
            if self.ui.checkBox_2.isChecked():
                automacao.site2_solucoes_receita(cpf=self.cpf)
            if self.ui.checkBox_3.isChecked():
                automacao.site3_tst_jus(cpf=self.cpf)
            # if self.ui.checkBox_4.isChecked():
            #     executar_automacao(self.cliente, "site2")
            # if self.ui.checkBox_5.isChecked():
            #     executar_automacao(self.cliente, "site2")
            # if self.ui.checkBox_6.isChecked():
            #     executar_automacao(self.cliente, "site2")
            # if self.ui.checkBox_7.isChecked():
            #     executar_automacao(self.cliente, "site2")
            # if self.ui.checkBox_8.isChecked():
            #     executar_automacao(self.cliente, "site2")
            # if self.ui.checkBox_9.isChecked():
            #     executar_automacao(self.cliente, "site2")
            # if self.ui.checkBox_10.isChecked():
            #     executar_automacao(self.cliente, "site2")
                
                
            # Execute a automação para as outras checkboxes da mesma maneira
        else:
            print("Erro: Preencha todos os campos de texto")
        
        
    
    def checar_box(self):
        pass

    def campos_preenchidos(self):
        self.nome = self.ui.lineEdit.text()
        self.cpf = self.ui.lineEdit_2.text()
        self.cnpj = self.ui.lineEdit_3.text()
        self.rg = self.ui.lineEdit_4.text()
        self.email = self.ui.lineEdit_5.text()

        if all([self.nome, self.cpf, self.cnpj, self.rg, self.email]):
            return True
            # Aqui você pode fazer o que desejar com a instância cliente,
            # como passá-la para outras funções ou realizar operações com ela
        else:
            print("Erro: Preencha todos os campos de texto")
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec())