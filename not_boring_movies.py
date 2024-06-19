import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    new_cinema=cinema.loc[(cinema['id']%2==1) & (~cinema['description'].str.contains('boring'))]
    df=new_cinema[['id','movie','description','rating']]
    df=df.sort_values(by='rating',ascending=False)
    return df
    
    
    
    
