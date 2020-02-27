import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

df_appl = pd.read_csv(r"AAPL.csv")
df_jnj = pd.read_csv(r"JNJ.csv")
df_ba = pd.read_csv(r"BA.csv")
df_wmt = pd.read_csv(r"WMT.csv")

corr_appl = df_appl['Adj_Close_DJI'].corr(df_appl['Adj_Close'])
corr_jnj = df_jnj['Adj_Close_DJI'].corr(df_jnj['Adj_Close'])
corr_ba = df_ba['Adj_Close_DJI'].corr(df_ba['Adj_Close'])
corr_wmt = df_wmt['Adj_Close_DJI'].corr(df_wmt['Adj_Close'])

print("Correlation value for APPL: ", corr_appl)
print("Correlation value for JNJ: ", corr_jnj)
print("Correlation value for BA: ", corr_ba)
print("Correlation value for WMT: ", corr_wmt)

Y = df_jnj['Adj_Close']
X = df_jnj['Adj_Close_DJI']

X = X.values.reshape(len(X), 1)
Y = Y.values.reshape(len(Y), 1)

print(X)
# print(Y)

plt.scatter(X, Y, color='black')
plt.title('Johnson and Johnson Data Regression')
plt.xlabel('Down Jones Industrial Average')
plt.ylabel('JNJ')


# Create linear regression object
regr = linear_model.LinearRegression()
 
# Train the model using the training sets
regr.fit(X, Y)

intr = regr.intercept_
print("Intercept", intr)

slp = regr.coef_
print("Slope: ", slp)

print("R2: ", regr.score(X, Y))
 
# Plot outputs
plt.plot(X, regr.predict(X), color='red', linewidth=3)

# plt.show()


def pred_stock_value(dji_index):
    pred_y = 0.0064174*dji_index - 22.21509844
    print("Predicted value of stock: ", pred_y)


while True:
    dji_index = float(input("Please enter DJI value: "))
    type(dji_index)
    pred_stock_value(dji_index)
