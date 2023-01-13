from time import sleep
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

servico = Service(EdgeChromiumDriverManager().install())

navegador = webdriver.Edge(service=servico)

navegador.get("https://docs.google.com/spreadsheets/d/16SIrhXr4mYiamfQrox9ScSrPhz3LI7RN/edit#gid=1018639743")
v = navegador.current_url
if "accounts.google" in v:
    navegador.find_element('xpath','//*[@id="identifierId"]').send_keys('marcosfgui2006@gmail.com')
    navegador.find_element('xpath','//*[@id="identifierNext"]/div/button/span').click()
    sleep(10)
