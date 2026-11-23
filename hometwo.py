import math
import numpy as np
from scipy import stats

before = np.array([68, 78, 71, 86, 80, 72, 81, 71])
after = np.array([70, 82, 76, 90, 87, 75, 86, 78])

d = after - before

n = len(d)  # จำนวนตัวอย่าง (n = 8)
mean_d = np.mean(d)  # ค่าเฉลี่ยผลต่าง (d_bar)
std_d = np.std(d, ddof=1)  # ส่วนเบี่ยงเบนมาตรฐาน (S_d) ใช้ ddof=1 สำหรับ Sample SD

confidence_level = 0.90
alpha = 1 - confidence_level

df = n - 1
t_critical = stats.t.ppf(1 - alpha / 2, df)

margin_of_error = t_critical * (std_d / math.sqrt(n))

L = mean_d - margin_of_error
U = mean_d + margin_of_error

print(f"ค่าเฉลี่ยผลต่าง (mean_d): {mean_d:.4f}")
print(f"ส่วนเบี่ยงเบนมาตรฐาน (std_d): {std_d:.4f}")
print(f"ช่วงความเชื่อมั่น 90% ของ μd คือ: ({L:.4f}, {U:.4f})")
print(f"หรือรูปแบบ L < μd < U: {L:.4f} < μd < {U:.4f}") 
