from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
def plot(y_pred,y_test):
    plt.plot(y_test, y_pred, '.')#actual values of x and y
    plt.title('Bayesian Ridge Regression')
    plt.xlabel('Y_test')
    plt.ylabel('Y_pred')
    plt.show()
    
path='/scratch/Trainee_DATA/Juhi/cyclone_files/'
aa3=np.loadtxt(path+'mix_training_cyclone_set.txt',unpack=True)
data3=aa3.T   
x_train=np.squeeze(data3[:,4:])
y_train=np.squeeze(data3[:,3])
aa4=np.loadtxt(path+'mix_testing_cyclone_set.txt',unpack=True)
data4=aa4.T   
x_test=np.squeeze(data4[:,4:])
y_test=np.squeeze(data4[:,3])

reg=LogisticRegression(random_state=0).fit(x_train,y_train)
y_pred=reg.predict(x_test)

print(metrics.mean_absolute_error(y_test,y_pred))
print(metrics.mean_squared_error(y_test,y_pred))
print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

plot(y_pred,y_test)
