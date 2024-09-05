import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['first'] = activity.groupby('player_id')['event_date'].transform(min)
    active_sec_day = activity.loc[activity['first'] + pd.DateOffset(1) == activity['event_date']]
    return pd.DataFrame([round(len(active_sec_day) / activity.player_id.nunique(),2)], columns=['fraction'])
    
