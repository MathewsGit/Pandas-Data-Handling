import pandas as pd
import numpy as np
import matplotlib as mp

name = pd.Series(['Mathews', 'Dhanesh'])
grade = pd.Series([12,12])
division = pd.Series(['M', 'M'])
regid = pd.Series([7882,12093])

df = pd.DataFrame({'reg_id': regid, 'name': name, 'grade': grade, 'division': division})
print(df)

Mathews = df[(df['grade'] == 12) & (df['name'] == 'Mathews')]
class_12M = df[(df['grade'] == 12) & (df['division'] == 'M')]

seniors = df.nlargest(3, 'grade')

print(len(df['reg_id']))

nreg = 6377
nname = 'Kid'
ngrade = 8,
ndiv = 'L'

df.loc[len(df['reg_id'])] = {'reg_id': nreg, 'name': nname, 'grade': ngrade, 'division': ndiv}

print(name.index.tolist())

print(seniors)
