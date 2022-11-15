from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)
# make a t_distribution object for t with 20 degree of freedom
t_dist=stats.t(20)
#plot the pdf 
values=np.linspace(-4,4,1000)
plt.plot(values,t_dist.pdf(values))
plt.xlabel('value')
plt.ylabel('probability for value')
plt.title('pdf for distributio with df=20')
plt.show()