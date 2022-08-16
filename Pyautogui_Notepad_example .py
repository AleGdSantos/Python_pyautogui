#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Execute para instalar o pyatuogui pela primeira vez

get_ipython().system('pip install pyautogui # instala o pyautogui ')


# In[4]:


# Importa a biblioteca pyautogui
import pyautogui as Mouse
# Importa a biblioteca pandas
import pandas as pd


# In[6]:


# Criando um dataframe com o data set concrete_data
# disponível em : https://www.kaggle.com/c/dat300-2018-concrete/data
df = pd.read_csv('concrete_data.csv') # Importa dados


# In[15]:


#Exibe as colunas disponíveis
df.columns


# In[22]:


# Exibe as últimas 5 linhas do dataset
df.tail()


# In[24]:


# Cria uma variável y e adiciona a ela todos os valores da coluna 'Cement'
y = df['Cement']
print(len(y))# Exibe quantos valores estão dentro de y 


# In[23]:


# A partir desse ponto começam as movimentações no hardware 
# O objetivo será abrir um notepad e digitar os valores presentes na coluna df['Cement']
# Para não prolongar muito iremos digitar apenas os 30 últimos valores, para digitar todos troque o valor de z por 0 
# Obs: dar um tempo entre cada movimentação, no meu caso, dei um tempo longo entre cada transição por conta do processamento
# do meu computador, para computadores melhores recomente reduzir, mas lembre-se sempre de deixar um tempo entre cada passo.

Mouse.sleep(2) # Aguardar 2 segundos  
Mouse.hotkey('win','r')# chama a função executar (windows + r)
Mouse.sleep(1)# Aguardar 1 segundo
Mouse.typewrite('notepad') # A função escreve o que deseja-se abrir no executar, no caso, Notepad
Mouse.sleep(1)# Aguardar 2 segundo
Mouse.press('enter')# Aguardar 1 segundo
Mouse.sleep(2) # Aguardar 2 segundos
z = 1000# Cria uma variável chamada z que inicia com o valor 1000, com isso serão digitados apenas os 30 últimnos valores do dataset
# Nesse for iremos coletar um a um dos valores presentes em y, no caso, será os valores presentes na coluna Cement do nosso df,
# cada valor será digitado no notepad com um intervalo de 0.5 segundos
for i in y:
    if z < len(y):
        Mouse.typewrite(str(y[z]), interval=0.005)
        Mouse.press('enter')
        z+=1
        print(i,z)
Mouse.sleep(1)# Aguardar 1 segundo
Mouse.typewrite('----Fim-----') # A função escreve fim, para sinalizar o termino da execução do programa


# In[ ]:




