#!/usr/bin/env python3
import sys
import os

from pathlib import Path
from simple_term_menu import TerminalMenu

current_file_path = Path(__file__).resolve()
current_dir = current_file_path.parent
sys.path.append(f"{current_dir}/../parser")

def try_int(potential_int):
    try:
        return int(potential_int)
    except:
        return None

# Importar el módulo
from hola import test
from parser import smcoid_parser, smcoid_interpreter


def sort_cmp(item):
    return item[-1]

def build_options(current_options):
    holder = []
    counter = 1
    for line in current_options:
        holder.append(f"{counter}   {line[0]}   {line[1]}")
        counter += 1
    return holder

#only supports numbers from [0,99]
def extract_numbers(lines, view_name_len):
    for line in lines:
        line.append(try_int(line[1][view_name_len:]))

def find_ordered(entries, target):
    for (index, entry) in enumerate(entries):
        if entry[2] == target:
            return index


def find_unordered(entries, target):
    if target >= len(entries):
        return None
    else:
        return target
    
def print_options(options):
    for entry in options:
        print(entry)

def main():
    
    options = {
        "interactive":False,
        "rac": True,
        "line": False,
        "instance": 4,
        "view_name": "hola1",
    }
    variable = '''
21231  hola121
11231  hola11
40897  hola12
30897  hola13
50612  hola15
    '''
    lista = variable.strip().splitlines()
    word_list = []
    for line in lista:
        word_list.append(line.split())
    extract_numbers(word_list, len(options["view_name"]))
    if options["line"]:
        sort_list = sorted(word_list, key=sort_cmp)
    else:
        sort_list = word_list

    menu_options = build_options(sort_list)
    if options["interactive"]:
        terminal_menu = TerminalMenu(menu_options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {menu_options[menu_entry_index]}!")
    else:
        print_options(menu_options)


if __name__ == "__main__":
    main()


