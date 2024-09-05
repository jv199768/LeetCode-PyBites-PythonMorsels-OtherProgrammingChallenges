import pandas as pd

df = pd.DataFrame({
    'fruits': pd.Categorical(['apple', 'kiwi', 'watermelon', 'kiwi', 'apple', 'kiwi']),
    'size': pd.Categorical(['small', 'large', 'large', 'small', 'large', 'small'])
})
df.info()