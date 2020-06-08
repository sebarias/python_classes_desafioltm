import pandas as pd
import numpy as np

primera = np.arange(50)
#print(primera)
segunda = primera[10:20]

segunda[2] = "100"
print(segunda)
print(primera)