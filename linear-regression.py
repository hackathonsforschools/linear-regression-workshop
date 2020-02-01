xVals = [-100, -10, -3, 0, 1, 2, 3, 4 , 10, 100]
yVals = [9901, 91, 7, 1, 3,7, 13, 21, 111, 10101]

epochs = 100000

w0 = 0
w1 = 0
w2 = 0
# these are the weights for each component of the equation for the line

alpha = 0.00000001 # this is the learning rate

for i in range(0, epochs):
    cost = 0

    for j in range(0, len(xVals)):
        prediction = w0 + (w1 * xVals[j]) + (w2 * xVals[j] * xVals[j])
        difference = yVals[j] - prediction

        w0 += alpha * difference
        w1 += alpha * difference * xVals[j]
        w2 += alpha * difference * xVals[j] * xVals[j]

print("Equation: hw(x) = " + str(w2) +"*x^2 + " + str(w1) + "*x + " + str(w0))