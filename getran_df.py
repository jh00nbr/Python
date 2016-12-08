#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script de consulta simples no banco de dados da Banca de Direção do Detran DF / By Jhonathan Davi A.K.A jh00nbr_ / 
# Insightl4b - http://lab.insightsecurity.com.br

__author__ =  "Jhonathan Davi"
__credits__ = ["Jhonathan Davi A.K.A jh00nbr_"]

import requests,sys,re

if __name__ == "__main__":
    if len(sys.argv) > 1:
    	cpf = sys.argv[1]
    	url = "http://getran.detran.df.gov.br/getranServicos/ConsultaHabilitacaoWS?wsdl"
        data = '<v:Envelope xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns:d="http://www.w3.org/2001/XMLSchema" xmlns:c="http://schemas.xmlsoap.org/soap/encoding/" xmlns:v="http://schemas.xmlsoap.org/soap/envelope/">'
        data += '<v:Header /><v:Body><n0:consultarBanca id="o0" c:root="1" xmlns:n0="http://ws.habilitacao.site.servicos.getran.searchtecnologia.com.br/">'
        data += '<cpf i:type="d:string">'+cpf+'</cpf>'
        data += '<token i:type="d:string">TKN832JHGSI2937MNGHSJ9987</token>'
        data += '</n0:consultarBanca></v:Body></v:Envelope>'
        headers = {'User-Agent':'ksoap2-android/2.6.0+','SOAPAction':'http://getran.detran.df.gov.br/getranServicos/','Content-Type':'text/xml;charset=utf-8'}
        req = requests.post(url,data=data,headers=headers)
        
        # Regex das tags XML   
        nome = re.search('<nome>(.*)</nome>',req.content).group(0).replace('<nome>','').replace('</nome>','')
        renach = re.search('<renach>(.*)</renach>',req.content).group(0).replace('<renach>','').replace('</renach>','')
        cpf = re.search('<cpf>(.*)</cpf>',req.content).group(0).replace('<cpf>','').replace('</cpf>','')
        dataNascimento = re.search('<dataNascimento>(.*)</dataNascimento>',req.content).group(0).replace('<dataNascimento>','').replace('</dataNascimento>','')
        local = re.search('<local>(.*)</local>',req.content).group(0).replace('<local>','').replace('</local>','')
        cfc = re.search('<cfc>(.*)</cfc>',req.content).group(0).replace('<cfc>','').replace('</cfc>','')
        resultado = re.search('<resultado>(.*)</resultado>',req.content).group(0).replace('<resultado>','').replace('</resultado>','')
        data = re.search('<data>(.*)</data>',req.content).group(0).replace('<data>','').replace('</data>','')
        hora = re.search('<hora>(.*)</hora>',req.content).group(0).replace('<hora>','').replace('</hora>','')     
       
        print ' Nome completo:',nome
        print ' CPF:',cpf
        print ' Renach:',renach
        print ' Data de nascimento:', dataNascimento
        print ' CFC:',cfc
        print ' Data:',data,'Hora:',hora
        print ' Resultado:',resultado
    else:
        print "[ ! ] Executar o script junto com o cpf:  ./getran.py <cpf>  | ./getran.py 1234567890"
