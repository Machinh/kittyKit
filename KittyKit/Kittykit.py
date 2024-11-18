# By mach1n3
from kittykit_commands import list_tools, clear_screen, load_ascii_arts, banner, display_ascii_art,display_intro

def get_help_commands():
    """Retorna um dicionário de comandos e suas descrições."""
    return {
        'help': 'Menu de ajuda',
        'banner': 'Randomiza um banner do KittyKit',
        'ferramentas': 'Menu de ferramentas',
    }

def main():
    """Função principal para iniciar a ferramenta."""
    clear_screen()
    
    ascii_arts = load_ascii_arts('ascii_art.txt')  # Carrega artes do arquivo
    display_ascii_art(ascii_arts)
    
    display_intro()

    while True:
        command = input("\nKKF > ").strip().lower()

        if command == 'ferramentas':
            list_tools()
        elif command == 'help':
            commands = get_help_commands()
            print(f"{'Comando':<20} {'Descrição'}")
            print(f"{'-'*20} {'-'*35}")
            
            for cmd, description in commands.items():
                print(f"{cmd:<20} {description}")
        elif command == 'banner':
            banner()
        elif command == 'clear':
            clear_screen()
        elif command == 'exit':
            print("Saindo do programa...")
            break
        else:
            print("Comando não reconhecido Meow. Digite 'help' para ver a lista de comandos.")

if __name__ == "__main__":
    main()