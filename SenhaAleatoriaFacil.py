#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Gerador de senhas aleatória fáceis de serem lembradas pelos usuários
"""

from random import randint
import easygui

def gerarSenha():
  """
  gerarSenha() -> senha: str

  Gera uma senha composta por um substantivo seguido de um adjetivo, ambos concordando em genêro, seguido também
  de um numero de dois a três digitos.
  """
  #gera aleatóriamente um indice de substantivo
  indexSubstantivo = randint(0,40)

  if (indexSubstantivo < 20):
    #caso o substantivo seja masculino, gera aleatóriamente um indice de adjetivo
    #em uma faixa em que ele será masculino ou neutro
    indexAdjetivo = randint(0,39)
  else:
    #caso o substantivo seja feminino, gera aleatóriamente um indice de adjetivo
    #em uma faixa em que ele será neutro ou feminino
    indexAdjetivo = randint(20,59)

  #gera aleatóriamente um número de dois ou três digitos
  numero = randint(0,999)
  strNum = str(numero) if (numero > 9) else '0'+str(numero)

  #abre o arquivo de substantivos e busca substantivo do indice desejado
  with open('ListaSubstantivos.txt','r') as arqSubstantivo:
    substantivo = arqSubstantivo.readlines()[indexSubstantivo].strip()

  #abre o arquivo de adjetivos e busca adjetivo do indice desejado
  with open('ListaAdjetivos.txt','r') as arqAdjetivo:
    adjetivo = arqAdjetivo.readlines()[indexAdjetivo].strip()

  #retorna a senha gerada
  return substantivo + adjetivo + strNum


def main():
  ### sem interface gráfica ###

  """
  #lê o número de senhas a serem geradas
  n = raw_input('Digite quantas senhas deseja gerar: ')
  while (not n.isdigit()):
    n = raw_input('Valor invalido. Digite novamente: ')

  #gera o número de senhas digitado pelo usuário
  for i in range(int(n)):
    print(gerarSenha())
  """

  ### com interface gráfica ###

  #lê o número de senhas a serem geradas
  n = easygui.integerbox(msg = 'Digite quantas senhas deseja gerar:', title = 'Gerador de senhas aleatórias', default = '', lowerbound = 1, upperbound = 10000)

  #gera o número de senhas digitado pelo usuário
  if n:
    senha = "\n".join(gerarSenha() for _ in range(n))
    easygui.textbox(msg = 'Senhas geradas:', title = 'Gerador de senhas aleatórias', text = senha)

  #encerra o programa
  return 0

if __name__ == '__main__':
	main()
