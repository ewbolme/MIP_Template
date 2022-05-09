from pulp import *
from helpers import MIP_recipe
from typing import Dict, Tuple, List

def add_objective(mip_prob: LpProblem(), mip_recipe_one_on_one: MIP_recipe):
    history_dict_cost = mip_recipe_one_on_one.History_Dict_Cost
    match_dict = mip_recipe_one_on_one.Match_Dict
    mip_prob.setObjective(lpSum(match_dict[a_name, z_name] * history_dict_cost[a_name, z_name] for a_name, z_name in match_dict.keys()))