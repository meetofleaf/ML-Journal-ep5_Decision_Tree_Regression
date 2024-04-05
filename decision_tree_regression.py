# Decision Tree Regression

#### Import Default Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#### Data Preparation
dataset = pd.read_csv("petrol_consumption.csv")

X = dataset.iloc[:,0:2].values     # Petrol tax, Average income
y = dataset.iloc[:,-1].values      # Petrol consumption
#plt.scatter(X,y)


#### Train the model
from sklearn.tree import DecisionTreeRegressor, plot_tree

# We train our model DecisionTreeRegressor class and fit method
regressor = DecisionTreeRegressor(random_state=0, max_depth=5)  # random_state adds a dash of randomness to how the decision tree is built, but it doesn't significantly affect the final predictions
                                                                # max_depth simply decides how tall the tree will be generated. The number of levels are excluding the parent level/node
                                                                # For more parameters explore: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
regressor.fit(X,y)


#### Predicting Results
# We define a simple function to predict the dependent variable for code reusability
def predict(model, inputs):
    return model.predict(inputs)

predict(regressor, [[15, 5500]])    # petrol_tax, average_income


#### Visualization
# The following code snippet visualizes the decision tree showing the tree's branches and nodes/leaves
plt.figure(figsize=(25,18))
plot_tree(regressor, fontsize=9, max_depth=3)
plt.show()

# If the model is trained on just 2 variables (1 dependent and 1 independent), then we'll be able to build a 2-D chart with the below given code snippet
'''
X_grid = np.arange(min(X), max(X), 0.1)
y_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X,y, color='red')
plt.plot(X_grid, regressor.predict(X_grid.reshape(-1, 1)), color='blue')
plt.xlabel('Average Income')
plt.ylabel('Petrol Consumption')
plt.show()
'''


