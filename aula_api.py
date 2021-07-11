#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#instalar bibliteca requests


# In[1]:


get_ipython().system(' pip install requests')


# In[ ]:


#importar a biblioteca requests


# In[2]:


import requests


# In[ ]:


#(url=) definição da URL a ser requisitada
#(requests.get) uso da requisição get
#(print(req.status_code)) exibe o código de status


# In[3]:


url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)

print(req.status_code)


# In[ ]:


#(dados = req.json()) recuperar os dados da requisição usando o metódo json
#(print(dados)) exibe os dados requeridos


# In[4]:


dados = req.json()

print(dados)


# In[ ]:


#(valor_reais = float(input()) onde o usuario insere o valor a ser convertido 
#(cotacao = dados['rates']['BRL']) recupera o valor dos dados da cotação através do [rates] na moeda Real[BRL]
#(print(f'R${valor_reais} em dólar valem US${(valor_reais/cotacao):.2f}')) exibe o valor convertido


# In[8]:


valor_reais = float(input('Informe o valor em R$ a ser convertido\n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valem US${(valor_reais/cotacao):.2f}')


# In[ ]:




