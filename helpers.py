from dataclasses import dataclass
from typing import Dict, Tuple, List
import pandas as pd
from pulp import *

#TODO add the ability to calculate the numbers of days as an integer
def find_days_since_last_chat(meeting_date) -> int:
    pass

@dataclass
class MIP_recipe:
    History_Dict_Cost: Dict[(str, str), int]
    Names_List: List[str]  
    Match_Dict: Dict[(str, str), LpVariable]