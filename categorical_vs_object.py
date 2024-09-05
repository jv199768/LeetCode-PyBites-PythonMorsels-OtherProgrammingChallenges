
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np
import pandas as pd

n = 100000

df_object = pd.DataFrame({
    'fruit': np.random.choice(['apple', 'banana', 'orange'], size=n)
})

print('Memory usage with object type:')
print(df_object['fruit'].memory_usage(deep=True))


df_category = pd.DataFrame({
    'fruit': pd.Categorical(np.random.choice(['apple', 'banana', 'orange'], size=n))
})

print('Memory usage with categorical type:')
print(df_category['fruit'].memory_usage(deep=True))
