import datetime
from datetime import  date


nome = input("Digite seu nome: ")
dia = int(input("Dia em que nasceu: "))
mes = int(input("Mes que nasceu: "))
ano = int(input("Ano que nasceu: "))

#diferencça

dataNasc = datetime.date(ano, mes, dia)
diferenca = (date.today() - dataNasc)

#resultado
result = (diferenca.days / 365.25)

print("%s tem %d" %(nome, result))
