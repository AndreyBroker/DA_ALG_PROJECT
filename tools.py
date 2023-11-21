import shutil
import os
import matplotlib.pyplot as plt

def print_center(text):
    terminal_size = shutil.get_terminal_size()
    
    horizontal_padding = (terminal_size.columns - len(text)) // 2
    vertical_padding = (terminal_size.lines - 3) // 2 

    print('\n' * vertical_padding)
    print(' ' * horizontal_padding + text)
    print('\n' * vertical_padding)

def print_center_x(text):
    terminal_size = shutil.get_terminal_size()    
    horizontal_padding = (terminal_size.columns - len(text)) // 2

    print(' ' * horizontal_padding + text)

def clean_terminal():
    os.system('cls')

def default_interface(text='', menu=False, page_title="TITLE"):
    
    menu_label = "SAIR [0]" 
    general_label = "Voltar [ENTER]"
    nav_label = menu_label if menu else general_label
    nav_sep_style = 48*"-"
    
    calc_seps = len(nav_sep_style) - ( len(page_title) + len(nav_label) )
    seps = calc_seps if calc_seps > 0 else 4

    while True:
        clean_terminal()
        
        print(nav_sep_style)
        print(page_title + " "*seps + nav_label)
        print(nav_sep_style)
        
        print(f"{text}")
        
        response = input("")
        
        return response
    
def list_choices_interface(page_title='', list_choices=[]):
    opcoes = "\n".join(f"[{i+1}] {choice}" for i, choice in enumerate(list_choices))
    response = default_interface(opcoes, page_title=page_title)
    
    match response:
        case "":
            return response
        case a if response.isdigit():
            number = int(response) - 1 
            if number <= len(list_choices) and number >= 0:
                return list_choices[number]
        case _:
            return False

def plot_two(df1, title1, df2, title2, tituloGeneral):
    fig, axs = plt.subplots(2, 1, figsize=(8, 6)) 

    axs[0].plot(df1["DATA"], df1["TEMP_AR"])
    axs[0].set_title(title1)

    axs[1].plot(df2["DATA"], df2["TEMP_AR"])
    axs[1].set_title(title2)

    fig.suptitle(tituloGeneral)

    plt.tight_layout()

    plt.show()
    
