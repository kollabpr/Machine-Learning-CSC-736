# Linear Regression

## Objective:

• Learn and demonstrate knowledge of Linear Regression. 

• Visualize the learning process of regression.

A linear regressor is able to predict values with given inputs based on provided training dataset. In this assignment, you are required to develop a program that is able to:

1. Generate points in the training set.

&emsp; • Arbitrarily define a line y = wx + b (eg. y = 2x+3) as your ground truth line;
  
&emsp; • Generate 20 random data points (randomly select 20 x and calculate 20 y accordingly) from the line defined above. The y value on each point needs to randomly add or minus a noise with the range of 10% ∗ y. For example, assuming your line is y = 2x+3. Your first point is x = 10, y = 23+rand(23∗0.1) or y = 23 − rand(23 ∗ 0.1).
  
&emsp; • Visualize the line in green and the 20 points (filled circles) on a graphic user interface similar to the attached figure.

2. Implement a linear regression with the gradient descent learning algorithm.

&emsp; • Randomly initialize the weight and bias to a double within (0, 1).

&emsp; • Set your learning rate η = 0.000001

&emsp; • Train your linear regressor by the gradient descent learning algorithm with the provided training data generated from the previous step.

&emsp; &emsp; – Define “epoch” as one iteration of training all 20 points one time. 

&emsp; &emsp; – For each epoch, iterating through 20 training points (xˆ , yˆ ):

&emsp; &emsp; &emsp; ∗ Use your linear model to calculate y = wxˆ + b

&emsp; &emsp; &emsp; ∗ Calculate the accumulated error for bias: err = 1/m (Σ(yˆ − y ) 

&emsp; &emsp; &emsp; ∗ Calculate the accumulated error for weight: err = 1/m Σ[(yˆ − y ) ∗ xˆ ] 

&emsp; &emsp; – Using this formula to update the bias: b = b + η × Bias_error

&emsp; &emsp; – Using this formula to update the weight: w = w + η × Weight_error

&emsp; • Visualize the line represented by the current weights at the end of each epoch on GUI. (like an animation.)

&emsp; • Output the number of mean square error (mse = 1/m Σ(yˆ − y )^2) on the training data at the end of each epoch.

&emsp; • Train your linear regression model for at least 500 epochs.
