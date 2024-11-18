#!/usr/bin/env python3
import os
import random
GREEN = "\033[92m"
RESET = "\033[0m"   # Reseta a cor para o padrão
CYAN = "\033[0;36m"


def list_tools():
    """Lista ferramentas e exploits disponíveis."""
    print("\nComandos disponíveis:")
    print("1. listar ferramentas")
    print("2. listar exploits")

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_ascii_arts(filename):
    """Carrega artes ASCII de um arquivo de texto."""
    with open(filename, 'r') as file:
        arts = file.read().strip().split('\n\n')  # Divide por duas quebras de linha
    return arts

def display_ascii_art(arts):
    """Exibe uma arte ASCII aleatória."""
    selected_art = random.choice(arts)  # Escolhe aleatoriamente de arts
    print(selected_art)

def banner():
    """Exibe um banner aleatório."""
    arts = load_ascii_arts('ascii_art.txt') 
    display_ascii_art(arts)
    display_intro()

def display_intro():
    """Exibe a introdução com informações do KittyKit."""
    print(f"+ -- --=[ {CYAN}KittyKit v1.0   {RESET}]")
    print("+ -- --=[ 1 ferramentas   ]")
    print(f"\nKittyKit Documentation: {GREEN}https://github.com/Machinh{RESET}")