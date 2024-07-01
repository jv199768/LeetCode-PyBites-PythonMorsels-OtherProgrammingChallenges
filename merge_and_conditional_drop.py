import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    combined = pd.merge(employee, bonus, how='left', on= 'empId')
    combined = combined[['name', 'bonus']]
    combined = combined.drop(combined[combined.bonus >= 1000].index)
    return combined

    
