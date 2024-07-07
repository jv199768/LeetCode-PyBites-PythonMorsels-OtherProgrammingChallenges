
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
        df = pd.concat([request_accepted["requester_id"],request_accepted["accepter_id"]]).value_counts().reset_index().head(1).rename(columns={"index":"id","count":"num"})
        return df 
    
