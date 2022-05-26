from pulp import *
from helpers import MIP_recipe

def add_max_one_meeting_constraint(mip_prob: LpProblem(), mip_recipe_one_on_one: MIP_recipe):
    names_list = mip_recipe_one_on_one.Names_List
    match_dict = mip_recipe_one_on_one.Match_Dict
    
    for i in range(0, len(names_list)+1):
        mip_prob += pulp.lp.Sum([match_dict(names_list[i], names_list[j]) if i < j else match_dict(names_list[j], names_list[i]) if i > j else 0 for j in range(0, len(names_list)+1)]) <= 1

