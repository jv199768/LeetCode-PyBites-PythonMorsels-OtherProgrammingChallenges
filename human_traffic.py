import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium.sort_values("id").query("people >= 100")
    stadium["row_nb"] = range(len(stadium))
    stadium["id_rownb_diff"] = stadium.id - stadium.row_nb
    stadium["size_of_consecutive_group"] = stadium.groupby("id_rownb_diff")["id"].transform("count")
    return stadium[stadium.size_of_consecutive_group >= 3][["id","visit_date","people"]]
