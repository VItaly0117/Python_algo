import numpy as np
import matplotlib.pyplot as plt

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='str')
spec = iris[:, 4]
quan_charact = iris[:, :4].astype(float)
fig, ax = plt.subplots(2, 2, figsize=(40, 20)) # Оставил твой figsize

# plot00(pie)
iris_types, quantity = np.unique(spec, return_counts=True)
ax[0][0].set_title("percentage of every iris type")
ax[0][0].pie(quantity, labels=iris_types)

# plot01(pizda)
sepal_charact = quan_charact[np.argsort(quan_charact[:, 0])]
sepal_length_points, sepal_width_points = sepal_charact[:, 0], sepal_charact[:, 1]

ax[0][1].set_title("relation of sepal length to its width")
ax[0][1].plot(sepal_length_points, sepal_width_points, color="black")
ax[0][1].scatter(sepal_length_points, sepal_width_points, marker="*", color="violet", joinstyle='round')
ax[0][1].set_xlabel("sepal length")
ax[0][1].set_ylabel("sepal width")

ax[0][1].grid()

# --- ВОТ ИСПРАВЛЕННЫЙ КУСОК В ТВОЕМ СТИЛЕ ---

# plot10(pediki)

# Фильтруем ЧИСЛА по названию 'Iris-setosa'
iris_setosa_data = quan_charact[spec == iris_types[0]]
# Сортируем отфильтрованные данные по 2-му столбцу (petal length)
iris_setosa = iris_setosa_data[np.argsort(iris_setosa_data[:, 2])]
# Берем столбцы
setosa_petal_lenght, setosa_petal_width = iris_setosa[:, 2], iris_setosa[:, 3]
ax[1][0].plot(setosa_petal_lenght, setosa_petal_width)

# То же самое для 'Iris-versicolor'
iris_versicolor_data = quan_charact[spec == iris_types[1]]
# Сортируем
iris_versicolor = iris_versicolor_data[np.argsort(iris_versicolor_data[:, 2])]
# Берем столбцы
versicolor_petal_lenght, versicolor_petal_width = iris_versicolor[:, 2], iris_versicolor[:, 3]
ax[1][0].plot(versicolor_petal_lenght, versicolor_petal_width)
print(iris_versicolor)

plt.show()