import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


x=pd.read_csv("2019players.csv")
country=x.iloc(:,28)
