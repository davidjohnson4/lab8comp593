from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info
import os
import sys

def main():
    root = Tk()
    root.title("Pokemon info Viewer")
    root.iconbitmap(os.path.join(sys.path[0], "Master-Ball.ico"))
    root.geometry('400x400')

    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2)

    frm_info = ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=1, column=0)

    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=1, column=1)

    lbl_name = ttk.Label(frm_user_input, text="Pokemon Name:")
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=0, column=1, pady=10)

    def btn_get_info_click():
        pokemon_name = ent_name.get()
        poke_dict = get_pokemon_info(pokemon_name)
        if poke_dict:
            lbl_height_val["text"] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + ' hg'
            types_list = (t['type']['name']for t in poke_dict['types'])
            lbl_type_val['text'] = ','.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defense['value'] = poke_dict['stats'][2]['base_stat']
            prg_S_attack['value'] = poke_dict['stats'][3]['base_stat']
            prg_S_defense['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']

    btn_get_info = ttk.Button(frm_user_input, text="Get Info", command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)

    lbl_height = ttk.Label(frm_info, text="Height:")
    lbl_height.grid(row=100, column=100)
    lbl_height_val = ttk.Label(frm_info, text="tbd")
    lbl_height_val.grid(row=100, column=200)

    lbl_weight = ttk.Label(frm_info, text="Weight:")
    lbl_weight.grid(row=200, column=100)
    lbl_weight_val = ttk.Label(frm_info, text="tbd")
    lbl_weight_val.grid(row=200, column=200)


    lbl_type = ttk.Label(frm_info, text="Type:")
    lbl_type.grid(row=300, column=100)
    lbl_type_val = ttk.Label(frm_info, text="tbd")
    lbl_type_val.grid(row=300, column=200)

    lbl_hp = ttk.Label(frm_stats, text="HP")
    lbl_hp.grid(row=100, column=100)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_hp.grid(row=100, column=200)

    lbl_attack = ttk.Label(frm_stats, text="Attack")
    lbl_attack.grid(row=200, column=100)
    prg_attack = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_attack.grid(row=200, column=200)

    lbl_defense = ttk.Label(frm_stats, text="Defense")
    lbl_defense.grid(row=300, column=100)
    prg_defense = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_defense.grid(row=300, column=200)

    lbl_S_attack = ttk.Label(frm_stats, text="Speical Attack")
    lbl_S_attack.grid(row=400, column=100)
    prg_S_attack = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_S_attack.grid(row=400, column=200)

    lbl_S_defense = ttk.Label(frm_stats, text="Speical Defense")
    lbl_S_defense.grid(row=500, column=100)
    prg_S_defense = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_S_defense.grid(row=500, column=200)

    lbl_speed = ttk.Label(frm_stats, text="Speed")
    lbl_speed.grid(row=600, column=100)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_speed.grid(row=600, column=200)

    root.mainloop()
   
    
main()