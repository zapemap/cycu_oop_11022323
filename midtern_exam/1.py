import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# 定義參數
mu = 1.5
sigma = 0.4

# 計算對數常態分布的尺度和形狀參數
shape = sigma
scale = np.exp(mu)

# 定義 x 範圍
x = np.linspace(0.01, 10, 500)

# 計算累積分布函數 (CDF)
cdf = lognorm.cdf(x, shape, scale=scale)

# 繪製圖形
plt.figure(figsize=(8, 5))
plt.plot(x, cdf, label='Lognormal CDF', color='blue')
plt.title('Lognormal Cumulative Distribution Function (CDF)')
plt.xlabel('x')
plt.ylabel('CDF')
plt.grid(True)
plt.legend()
plt.show()
