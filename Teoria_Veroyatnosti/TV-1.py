import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# --- ВХІДНІ ---
x = [6, 5, 6, 9, 8, 7, 10, 5, 4, 9, 7, 6, 5, 8, 7, 9, 6, 9, 11, 6]
n = len(x)

# --- ВАРІАЦІЙНИЙ РЯД ---
x_sort = np.sort(x)
print(f"n = {n}")
print(f"Варіаційний ряд: {x_sort}")

# --- ЧАСТОТИ ---
freq = Counter(x_sort)
vals = sorted(freq.keys())
cnts = [freq[v] for v in vals]

print("\n--- Частоти ---")
print(f"{'xi':<5} | {'ni':<5}")
print("-" * 15)
for v, c in zip(vals, cnts):
    print(f"{v:<5} | {c:<5}")

# --- ХАРАКТЕРИСТИКИ ---
x_mean = np.mean(x)                    # 1
var_n = np.var(x, ddof=0)              # 2
var_n1 = np.var(x, ddof=1)             # 3
std_n = np.std(x, ddof=0)              # 4
std_n1 = np.std(x, ddof=1)             # 5
x_range = np.max(x) - np.min(x)        # 6
x_med = np.median(x)                   # 7
x_mode = max(freq, key=freq.get)       # 8
Q1 = x_sort[4]
Q3 = x_sort[14]
Q = (Q3 - Q1) / 2                      # 9
cv = (std_n1 / x_mean) * 100           # 10

# 11-12
d = x - x_mean
m3 = np.mean(d**3)
m4 = np.mean(d**4)
A = m3 / (std_n**3)
E = (m4 / (std_n**4)) - 3

print(f"\n1)  x̄ = {x_mean}")
print(f"2)  D = {var_n:.4f}")
print(f"3)  s² = {var_n1:.4f}")
print(f"4)  σ = {std_n:.4f}")
print(f"5)  s = {std_n1:.4f}")
print(f"6)  R = {x_range}")
print(f"7)  Me = {x_med}")
print(f"8)  Mo = {x_mode} ({freq[x_mode]} разів)")
print(f"9)  Q = {Q} (Q₁={Q1}, Q₃={Q3})")
print(f"10) V = {cv:.2f}%")
print(f"11) A = {A:.4f}")
print(f"12) E = {E:.4f}")

# --- ГРАФІКИ ---
plt.figure(figsize=(12, 5))

# Гістограма
plt.subplot(1, 2, 1)
plt.hist(x, bins=range(min(x), max(x)+2),
         edgecolor='black', align='left', rwidth=0.8)
plt.title('Гістограма частот')
plt.xlabel('xi')
plt.ylabel('ni')
plt.grid(axis='y', alpha=0.5)
plt.xticks(vals)

# Емпірична функція
plt.subplot(1, 2, 2)
x_cdf = np.sort(x)
y_cdf = np.arange(1, n+1) / n
plt.step(x_cdf, y_cdf, where='post')
plt.title('Емпірична функція розподілу')
plt.xlabel('x')
plt.ylabel('Fn(x)')
plt.grid(True)
plt.yticks(np.arange(0, 1.1, 0.1))

plt.tight_layout()
plt.show()