from keyboard import on_press_key
from mouse import release, hold
from time import sleep

condicao = False

def toggle_condicao(e):
    global condicao
    
    condicao = not condicao
    print(f'Condicao = {condicao}')

def verificar_true():
    while True:
        if condicao:
            hold('left')
            while condicao == True:
                sleep(1)
        
        else:
            if condicao == False:
                release('left')
                while condicao == False:
                    sleep(1)
        
        sleep(0.1)

on_press_key('F4', toggle_condicao)
verificar_true()
