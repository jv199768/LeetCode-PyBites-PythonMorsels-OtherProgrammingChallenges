import pandas as pd
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
  new_df = person.merge(address[["state", "city", "personId"]], how='left', on= 'personId')
  new_df.drop(['personId'], axis=1, inplace=True)
return new_df
