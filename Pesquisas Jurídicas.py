#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importaçaõ das bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
import time
import os

# Abrindo o navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Criando o caminho para o site e entrando no mesmo
caminho = os.getcwd()
arquivo = caminho + r"\Pesquisa.html"
navegador.get(arquivo)


# In[2]:


# Importando tabela com os dados
tabela_processos = pd.read_excel('Processos.xlsx')
display(tabela_processos)
tabela_processos = tabela_processos.drop(['Status'], axis = 1)
display(tabela_processos)


# In[3]:


# Definindo algumas variáveis usadas abaixo
encontrado = 0
nao_encontrado = 0
cont = 0

# Repetição para cada pessoa
for linha in tabela_processos.index:

    cont += 1
    
    #Movendo o mouse para o botão de escolha
    esc_estado = navegador.find_element(By.XPATH, '/html/body/div/div/button')
    ActionChains(navegador).move_to_element(esc_estado).perform()
    estado = str(tabela_processos.loc[linha, 'Cidade'])
    navegador.find_element(By.LINK_TEXT, estado).click()

    #Mudando de aba
    esc_estado = navegador.window_handles[0]
    pesquisa_estado = navegador.window_handles[cont]
    navegador.switch_to.window(pesquisa_estado)

    #Preenchendo as informações sobre o processo e pesquisando
    navegador.find_element(By.ID, 'nome').send_keys(tabela_processos.loc[linha, 'Nome'])
    navegador.find_element(By.ID, 'advogado').send_keys(tabela_processos.loc[linha, 'Advogado'])
    navegador.find_element(By.ID, 'numero').send_keys(str(tabela_processos.loc[linha, 'Processo']))
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/button').click()

    #Aceitando o alerta
    alerta = navegador.switch_to.alert
    alerta.accept()
    
    while True:
        try:
            alerta = navegador.switch_to.alert
            break
        except:
            time.sleep(1)
    
    #Contando resultados
    resultado = alerta.text
    alerta.accept()

    if 'Processo encontrado com sucesso!' in resultado:
        encontrado += 1
    else:
        nao_encontrado += 1
        
    #Mudando para a aba de escolha dos estados
    navegador.switch_to.window(esc_estado)

#Mostrando o resultado dos processos
print(f'''{encontrado} processos foram encontrados.
{nao_encontrado} processos não foram encontrados.''')

