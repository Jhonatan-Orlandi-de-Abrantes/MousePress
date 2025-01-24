from keyboard import on_press_key
from mouse import click
from time import sleep


condicao = False
min = 0
hora = 0


def calculo_tempo():
    global min, hora
    
    min += 1
    
    if min == 60:
        hora += 1
        min = 0
        
    print(f'{hora}h {min}min')

def toggle_condicao(e):
    global condicao
    
    condicao = not condicao
    print(f'Condicao = {condicao}')

def verificar_true():
    global min, hora
    
    while True:
        if condicao:
            click()
            print('*Click*')
            sleep(60)
            calculo_tempo()
        else:
            min = 0
            hora = 0
            sleep(0.1)

on_press_key('F4', toggle_condicao)
verificar_true()
