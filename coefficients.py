from pulp import *
from helpers import find_days_since_last_chat
from typing import Dict, Tuple, List

def create_history_cost_dict(names_list, history_df) -> Tuple[List, Dict[(str, str), int]]:
    history_dict = {}
    #TODO figure out how to make this less messy
    for i in range(0, len(names_list)+1):
        for j in range(i+1, len(names_list)+1):
            history_dict[names_list[i], names_list[i]]=10000

    for index, row in history_df.iterrows():
        days_since_last_chat = find_days_since_last_chat(row['Date'])
        if days_since_last_chat < history_dict[row['A_Name'], row['Z_Name']]:
            history_dict[row['A_Name'], row['Z_Name']] = days_since_last_chat
    
    return history_dict