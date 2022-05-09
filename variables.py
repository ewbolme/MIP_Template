from pulp import *

def create_match_variables(names_list):
    match_dict = {}
    for i in range (0, len(names_list)+1):
        for j in range (0, len(names_list)+1):
            if j <= i:
                pass
            else:
                match_dict[names_list[i], names_list[j]] = LpVariable(f'match_bool_{names_list[i]}_{names_list[j]}', cat='Binary')
                match_dict[names_list[i], names_list[j]].setInitialValue(0)
                pass
    return(match_dict)
