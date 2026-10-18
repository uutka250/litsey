import random
import pandas as pd
data = {
    "col1": [random.randint(1,10),random.randint(1,10),random.randint(1,10)],
    "col2": [random.randint(1,10),random.randint(1,10),random.randint(1,10)],
    "col3": [random.randint(1,10),random.randint(1,10),random.randint(1,10)],
}

df = pd.DataFrame(data)

print(df.to_string(index=False))