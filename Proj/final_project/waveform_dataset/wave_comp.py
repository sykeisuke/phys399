import numpy as np
import matplotlib.pyplot as plt

# ------------ 1. データ読み込み ------------
wf0 = np.load('waveform_data_0.npy')   # shape: (10000, 104)
wf1 = np.load('waveform_data_1.npy')

# ------------ 2. 先頭4列を除外 ------------
wf0_trim = wf0[:, 4:]                 # shape: (10000, 100)
wf1_trim = wf1[:, 4:]

assert wf0_trim.shape[1] == wf1_trim.shape[1], "Waveform lengths differ after trimming!"

# ------------ 3. 平均波形計算 ------------
avg0 = wf0_trim.mean(axis=0)          # shape: (100,)
avg1 = wf1_trim.mean(axis=0)

# ------------ 4. プロット ------------
t = np.arange(avg0.size)              # サンプル番号（100 点）

plt.figure(figsize=(9,4.5))
plt.plot(t, avg0, label='Average – dataset 0 (cols 4–103)')
plt.plot(t, avg1, label='Average – dataset 1 (cols 4–103)')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.title('Comparison of average waveforms (first 4 columns excluded)')
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()

# ------------ 5. 差分評価 ------------
diff  = avg0 - avg1
rmse  = np.sqrt(np.mean(diff**2))
print(f'RMSE between trimmed average waveforms: {rmse:.3f}')

# 差分波形をプロットしたい場合は以下を有効化
plt.figure(figsize=(9,3))
plt.plot(t, diff, color='purple')
plt.xlabel('Sample index')
plt.ylabel('Amplitude difference (0 – 1)')
plt.title('Difference between average waveforms')
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
