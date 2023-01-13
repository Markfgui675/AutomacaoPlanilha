from time import sleep
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

servico = Service(EdgeChromiumDriverManager().install())

navegador = webdriver.Edge(service=servico)
