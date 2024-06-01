import json

# Open JSON file
with open('data.json') as f:
    data = json.load(f)

# Print first ID in string format
print(str(data[0]['id']))

import numpy  as np
a=np.array([1,2,3])
print( a)
