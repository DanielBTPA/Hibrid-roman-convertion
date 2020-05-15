# -*- coding: utf-8 -*-
import os


# Função que limpa a tela do prompt de comando
# Linux e Mac = clear
# Windows = cls
clear_screen = lambda: os.system('clear' if os.name != 'nt' else 'cls') 

pause = lambda msg: input(msg)

roman_numbers = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5, 
    "IV": 4, 
    "I": 1
}

# Conversor hibrido (Converte tanto de decimal para romano e vice versa)
def roman_converter(value: any):
    if type(value) is int: # Se o tipo da vareavel 'value' for inteiro então faz a conversão de decimal para romano
        res = ""
        for rom in roman_numbers:
            val = roman_numbers.get(rom)
            while value >= val:
                value -= val
                res += rom
        return res
    elif type(value) is str: # Se o tipo da vareavel 'value' for uma string então faz a conversão de romano para inteiro
        res = 0
        i = 0
        while (i < len(value)): 
            s1 = roman_numbers[value[i]]
            if (i+1 < len(value)): 
                s2 = roman_numbers[value[i+1]] 
                if (s1 >= s2): 
                    res += s1
                    i += 1
                else: 
                    res += (s2 - s1) 
                    i += 2
            else: 
                res += s1 
                i = i + 1
        return str(res)
    else: # Se for outro tipo então é lançado uma exceção para ser tratada em outro trecho do codigo
        raise Exception()

def scr_main(): # Tela principal
    clear_screen()
    print("\t\tConversor numeros romanos.\n\n")
    op = input("Opção 1 para converter ou 2 para sair da conversão: ")

    if op == '1':
        value = input("\nDigite o valor a ser convertido (Pode ser tanto romano ou decimal): ")
        value = str.upper(value)
        try:
            print("\n[" + value + " = " + roman_converter(int(value)) + "]")
        except:
            try:
                print("\n[" + value + " = " + roman_converter(value) + "]")
            except:
                print("\nValor invalido.")

        input("\nPressione enter.")
    elif op == '2':
        global running
        running = False
    else: 
        input('\nPressione enter.')

# Controla a execução do loop.
running = True


def main():
    while running:
        scr_main()

    print("\n\nBye ;)")

if __name__ == '__main__':
    main()