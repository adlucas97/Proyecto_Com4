import numpy as np
from scipy import signal
#import pandas as pd
import statsmodels.api as sm
#import oct2py

#datos = {'col1':[37,247,301,266,233,198,299,469,514,605,597,671,540,165,377,370,181,147,47],
#'col2': [93,263,86,213,250,338,284,145,168,12,474,491,468,588,535,509,243,181,258],
#'col3': [45,187,219,149,59,225,458,234,179,233,80,161,271,223,364,279,274,206,23]}
#df=pd.DataFrame(data=datos,dtype=np.int16)
#print(df)
#print(df.corr())

x1 = np.array([37,247,301,266,233,198,299,469,514,605,597,671,540,165,377,370,181,147,47])
x2 = np.array([93,263,86,213,250,338,284,145,168,12,474,491,468,588,535,509,243,181,258,28,77,36])
corr_x1_x2 =signal.correlate(x1[0:19],x2[0:19])
print(np.max(corr_x1_x2))
delay = np.argmax(corr_x1_x2)-int(len(corr_x1_x2)/2)
rms = np.sqrt(sum(x1[0:19]**2)/(len(x1)-np.abs(delay)))*np.sqrt(sum(x2[0:19]**2)/(len(x1)-np.abs(delay)))
coeff = corr_x1_x2/((len(x1)-np.abs(delay))*rms)
print(np.max(coeff))
delay = np.argmax(corr_x1_x2)-int(len(corr_x1_x2)/2)
print(delay)
print(corr_x1_x2)
