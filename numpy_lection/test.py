import numpy as np

grades = np.array([
    [67, 80, 90, 75, 88],
    [92, 81, 76, 95, 89],
    [63, 75, 64, 65, 72],
    [52, 67, 54, 65, 61]
])

# 1. Середній бал студентів (по рядках)
student_avg = grades.mean(axis=1)
print("Середній бал студентів:")
print("   ".join(f"{x:.2f}" for x in student_avg))

# 2. Середній бал предметів (по стовпцях)
subject_avg = grades.mean(axis=0)
print("\nСередній бал предметів:")
print("   ".join(f"{x:.2f}" for x in subject_avg))

# 3. Кращий студент
best_index = np.argmax(student_avg)
print("\nКращий студент:")
print(f"{student_avg[best_index]:.2f}")

# 4. Найнижча успішність предмету
worst_index = np.argmin(subject_avg)
print("\nНайнижча успішність предмету:")
print(f"{subject_avg[worst_index]:.2f}")
