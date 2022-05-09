from typing import Dict, Tuple, List
import click
import cli_utils
from pulp import *
from openpyxl import load_workbook
import datetime
import pandas as pd
from objective import add_objective
from variables import create_match_variables
from coefficients import create_history_cost_dict
from constraints import add_max_one_meeting_constraint

def process_sheet(excel_sheet) -> pd.DataFrame:
    excel_data = excel_sheet.values
    excel_columns = next(excel_data)[0:]
    df = pd.DataFrame(excel_data, columns=excel_columns)
    return(df)

def load_parameters_file(file_in) -> Tuple[List, Dict[(str, str), int]]:
    wb = load_workbook(filename=file_in)
    name_sheet = wb['Name_List']
    history_sheet = wb['History_List']
    names_df = process_sheet(name_sheet)
    history_df = process_sheet(history_sheet)
    names_df = names_df.iloc[names_df.name.str.lower().argsort()]
    names_list = names_df.name.tolist()
    history_dict = create_history_cost_dict(names_list, history_df)
    return(names_list, history_dict)

@click.command()
@click.argument('file_in', type=click.Path(exists=True))
def run_optimizer(filename=file_in):
    mip_prob = LpProblem("Create Roulette Matches", LpMaximize)
    names_list, history_dict = load_parameters_file(filename)
    match_dict = create_match_variables(names_list)
    add_objective(mip_prob, match_dict, history_dict)
    add_max_one_meeting_constraint(mip_prob, names_list, match_dict)

cli

if __name__ == '__main__':
    cli()
