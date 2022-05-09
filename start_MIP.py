from typing import Dict, Tuple, List
import click
from pulp import *
from openpyxl import load_workbook
import datetime
import pandas as pd
from objective import add_objective
from variables import create_match_variables
from coefficients import create_history_cost_dict
from constraints import add_max_one_meeting_constraint
from helpers import MIP_recipe

def process_sheet(excel_sheet) -> pd.DataFrame:
    excel_data = excel_sheet.values
    excel_columns = next(excel_data)[0:]
    df = pd.DataFrame(excel_data, columns=excel_columns)
    return(df)

def load_parameters_file(file_in) -> Tuple[List, Dict[(str, str), int]]:
    wb = load_workbook(filename=file_in)

    # turn the information in each excel sheet into a Pandas dataframe - note it would be faster to directly convert the information in each dataframe into the desired object but as the data we are dealing with is small its a negligable gain in performance
    names_df = process_sheet(wb['Name_List'])
    history_df = process_sheet(wb['History_List'])
    vacation_df = process_sheet(wb['Vacations'])
    names_df = names_df.iloc[names_df.name.str.lower().argsort()]
    names_list = []
    for row in names_df.iterrows():
        if row.Names in vacation_df.Names:
            pass
        else:
            names_list.append(row.Names.value)

    if len(names_list) % 2 == 1:
            names_list.append('ZZZ_UNMATCHED')
    history_dict_cost = create_history_cost_dict(names_list, history_df)
    return(names_list, history_dict_cost)

@click.command()
@click.argument('file_in', type=click.Path(exists=True))
def run_optimizer(filename):
    names_list, history_dict_cost = load_parameters_file(filename)
    match_dict = create_match_variables(names_list)
    mip_recipe_one_on_one = MIP_recipe(
        History_Dict_Cost=history_dict_cost,
        Names_List=history_dict_cost,
        Match_Dict=match_dict
    )
    mip_prob = LpProblem("Create Roulette Matches", LpMaximize)
    add_objective(mip_prob, mip_recipe_one_on_one)
    add_max_one_meeting_constraint(mip_prob, mip_recipe_one_on_one)

click.cli.add_command(run_optimizer)

if __name__ == '__main__':
    click.cli()
