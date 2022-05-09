from pulp import *

def add_max_one_meeting_constraint(mip_prob, names_list, match_dict):
    for i in range(0, len(names_list)+1):
        mip_prob += lp.Sum([match_dict(names_list[i], names_list[j]) if i < j else match_dict(names_list[j], names_list[i]) if i > j else 0 for j in range(0, len(names_list)+1)]) <= 1

