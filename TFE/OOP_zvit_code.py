#str
text = "Python Programming"
print(text.lower())  # "python programming"
print(text.split())  # ['Python', 'Programming']
#list
numbers = [3, 1, 4, 1, 5]
numbers.sort()
numbers.append(9)
#dict
data = {'a': 1, 'b': 2}
data.update({'c': 3})
keys = data.keys()  # dict_keys view object
#numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())  # 3.0
print(arr.std())   # стандартне відхилення
reshaped = arr.reshape(5, 1)
#matlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Line Plot')
plt.show()