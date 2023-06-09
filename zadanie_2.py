# Задача 2. Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
import scipy.stats as stats

x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
s = np.sqrt(np.std(x, ddof=1))
t = stats.t.ppf(1 - (1 - 0.95)/2, len(x) - 1)
print(f'Доверительный интервал:[{np.mean(x) - t * s/np.sqrt(len(x))}; {np.mean(x) + t * s/np.sqrt(len(x))}]')