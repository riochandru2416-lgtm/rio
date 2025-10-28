#1
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
#2
# import common libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Configure visualization style
sns.set(style='whitegrid', palette='pastel', font_scale=1.1)
plt.rcParams['figure.figsize'] = [10, 6]

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
#3
# Loading... the dataset:
df = pd.read_csv('/kaggle/input/students-performance-in-exams/StudentsPerformance.csv')

# Display the top five rows of dataset.
df.head()

#4
# Shape 
print(df.shape)

#5
# data types 
print(df.info())

#6
# BaSic /// STATISTICS \\\
df.describe()

#7
# I usualy like to convert columns in a Snake case (means in lower abc with underscore.)
df.columns = [col.strip().lower().replace(r' ', '_') for col in df.columns]
df.columns = [col.strip().lower().replace(r'/', '_') for col in df.columns]

#8
# Small overview after customizing column names (looking good not!!?)
df.head(2)

#9
## Score Distributions.
import warnings
warnings.filterwarnings("ignore", message="use_inf_as_na option is deprecated")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.histplot(df['math_score'], kde=True, ax=axes[0], color='skyblue')
sns.histplot(df['reading_score'], kde=True, ax=axes[1], color='lightgreen')
sns.histplot(df['writing_score'], kde=True, ax=axes[2], color='salmon')

axes[0].set_title('Math Score Distribution')
axes[2].set_title('Writing Score Arrangement')
axes[1].set_title('Reading Score Spread')

plt.tight_layout()
plt.show()

#10
## Gender vs Average Scores 

score_cols = ['math_score', 'reading_score', 'writing_score']
df_melt = df.melt(id_vars='gender', value_vars=score_cols, var_name='Subject', value_name='Score')

#11
sns.barplot(data=df_melt, x='Subject', y='Score', hue='gender', errorbar=None, palette='mako')
plt.title('Average Scores by Gender')
plt.show()

