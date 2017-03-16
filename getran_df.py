#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script de consulta simples no banco de dados da Banca de Direção do Detran DF / By Jhonathan Davi A.K.A jh00nbr 
# jdavi@insightsecurity.com.br
# Insightl4b - http://lab.insightsecurity.com.br 
# Blog: lab.insightsecurity.com.br
# Github: http://github.com/jh00nbr
# jhonathandavi.com.br
# Twitter @jh00nbr

import requests,sys,re

__author__ =  "Jhonathan Davi A.K.A jh00nbr"

dados = {'nome':'','renach':'','cpf':'','dataNascimento':'','local':'','cfc':'','resultado':'', 'data':'','hora':''}

def get_dados(contents): # Regex das tags XML
    nome = re.search('<nome>(.*)</nome>',contents).group(0).replace('<nome>','').replace('</nome>','')
    renach = re.search('<renach>(.*)</renach>',contents).group(0).replace('<renach>','').replace('</renach>','')
    cpf = re.search('<cpf>(.*)</cpf>',contents).group(0).replace('<cpf>','').replace('</cpf>','')
    dataNascimento = re.search('<dataNascimento>(.*)</dataNascimento>',contents).group(0).replace('<dataNascimento>','').replace('</dataNascimento>','')
    local = re.search('<local>(.*)</local>',contents).group(0).replace('<local>','').replace('</local>','')
    cfc = re.search('<cfc>(.*)</cfc>',contents).group(0).replace('<cfc>','').replace('</cfc>','')
    resultado = re.search('<resultado>(.*)</resultado>',contents).group(0).replace('<resultado>','').replace('</resultado>','')
    data = re.search('<data>(.*)</data>',contents).group(0).replace('<data>','').replace('</data>','')
    hora = re.search('<hora>(.*)</hora>',contents).group(0).replace('<hora>','').replace('</hora>','')
    dados['nome'],dados['renach'],dados['cpf'],dados['dataNascimento'],dados['local'],dados['cfc'],dados['resultado'],dados['data'],dados['hora'] = nome,renach,cpf,dataNascimento,local,cfc,resultado,data,hora

if __name__ == "__main__":
    if len(sys.argv) > 1:          
        configs = {'api_getran':'http://getran.detran.df.gov.br/getranServicos/ConsultaHabilitacaoWS?wsdl','cpf':sys.argv[1],'token':'TKN832JHGSI2937MNGHSJ9987','user_agent':'ksoap2-android/2.6.0+'}
        data = '<v:Envelope xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns:d="http://www.w3.org/2001/XMLSchema" xmlns:c="http://schemas.xmlsoap.org/soap/encoding/" xmlns:v="http://schemas.xmlsoap.org/soap/envelope/">'
        data += '<v:Header /><v:Body><n0:consultarBanca id="o0" c:root="1" xmlns:n0="http://ws.habilitacao.site.servicos.getran.searchtecnologia.com.br/">'
        data += '<cpf i:type="d:string">'+configs['cpf']+'</cpf>'
        data += '<token i:type="d:string">'+configs['token']+'</token>'
        data += '</n0:consultarBanca></v:Body></v:Envelope>'
        headers = {'User-Agent':configs['user_agent'],'SOAPAction':'http://getran.detran.df.gov.br/getranServicos/','Content-Type':'text/xml;charset=utf-8'}
        req = requests.post(configs['api_getran'],data=data,headers=headers)
        get_dados(req.content) # Chama a função get_dados e retorna os dados solicitados.
        print ' Nome completo:',dados['nome']
        print ' CPF:',dados['cpf']
        print ' Renach:',dados['renach']
        print ' Data de nascimento:', dados['dataNascimento']
        print ' CFC:',dados['cfc']
        print ' Data:',dados['data'],'Hora:',dados['hora']
        print ' Resultado:',dados['resultado']
    else:
        print "[ ! ] Executar o script junto com o cpf:  ./getran.py <cpf>  | ./getran.py 1234567890"
