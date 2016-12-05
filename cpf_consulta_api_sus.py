#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,json,sys

# Script simples para consulta de dados na base dados nacional do SUS utilizando um CPF.
# Jhonathan Davi A.K.A jh00nbr / Insightl4b lab.insightsecurity.com.br
# Blog: lab.insightsecurity.com.br
# Github: github.com/jh00nbr
# Twitter @jh00nbr

config = {'api_sus':'http://dabsistemas.saude.gov.br/sistemas/sadab/js/buscar_cpf_dbpessoa.json.php?cpf=', 'cpf':sys.argv[1]}
req = requests.get(config['api_sus']+config['cpf'])
dados = json.loads(req.content)

# Retorna os dados no formato<nome_pessoa> / <numero_cpf> / <data_nascimento> / <nome_mae>"

print dados['NO_PESSOA_FISICA'], "/", dados['NU_CPF'], "/", dados['DT_NASCIMENTO'], "/", dados['NO_MAE']

# NU_CPF, NO_PESSOA_FISICA, DT_NASCIMENTO, CO_SEXO, NO_MAE, DS_SEXO
