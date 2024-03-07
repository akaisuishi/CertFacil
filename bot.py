from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Automacao():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pr-BR')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--enable-extesions')
        chrome_options.add_argument('--profile-directory=Default')
        self.driver = webdriver.Chrome(options=chrome_options)
    def site1_servicos_receita(self, cpf, url="https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp"):
        self.driver.get(url)
        time.sleep(5)
        cpf_path = "//input[@id='txtCPF']"
        self.driver.find_element(By.XPATH, cpf_path).send_keys(cpf)
        time.sleep(5)
        data_nasc_path = "//input[@id='txtDataNascimento']"
        self.driver.find_element(By.XPATH, data_nasc_path).send_keys()
        emitir_path = "//input[@id='id_submit']"
        self.driver.find_element(By.XPATH, emitir_path).click()
    def site2_solucoes_receita(self, cpf, url="https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PF/Emitir"):
        self.driver.get(url)
        time.sleep(5)
        cpf_path = "//input[@id='NI']"
        self.driver.find_element(By.XPATH, cpf_path).send_keys(cpf)
        emitir_path = "//input[@id='validar']"
        self.driver.find_element(By.XPATH, emitir_path).click()
        time.sleep(5)

    def site3_tst_jus(self, cpf, url="https://www.tst.jus.br/certidao1"):
        self.driver.get(url)
        time.sleep(5)
        cpf_path = "//input[@id='gerarCertidaoForm:cpfCnpj']"
        self.driver.find_element(By.XPATH, cpf_path).send_keys(cpf)
        emitir_path = "//input[@id='gerarCertidaoForm:btnEmitirCertidao']"
        self.driver.find_element(By.XPATH, emitir_path).click()