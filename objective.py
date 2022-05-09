from pulp import *

def add_objective(mip_prob, match_dict, history_dict):
    mip_prob.setObjective(lpSum(match_dict[a_name, z_name] * history_dict[a_name, z_name] for a_name, z_name in match_dict.keys()))