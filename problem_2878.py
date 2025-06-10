import pandas as pd
from typing import List
import numpy as np

#df = pd.DataFrame(np.random.rand(10,5),columns=['col1','col2','col3','col4','col5'])

def getDataframeSize(players: pd.DataFrame) -> List[int]:
      return list(players.shape)

#print(getDataframeSize(df))
