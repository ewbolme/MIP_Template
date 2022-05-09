from dataclasses import dataclass
from typing import Dict, Tuple, List
import pandas as pd

def find_days_since_last_chat(meeting_date) -> int:
    pass

@dataclass
class MIP_recipie:
    History_Cost: Dict[(str, str), int]
    Vacation_List: Dict[str, bool]