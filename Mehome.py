import pandas as pd

# ข้อมูลปริมาณการใช้ RAM (GB) ทั้งหมด 34 ค่า จากภาพ
data = [
    8.0, 8.2, 7.9, 8.1, 8.3, 8.1, 8.0, 8.2, 8.1, 8.0, 8.6, 8.2, 7.5,
    8.0, 9.1, 8.5, 7.6, 8.2, 7.1, 8.1, 8.3, 8.7, 7.8, 8.7, 8.5, 8.4,
    8.4, 7.9, 8.8, 7.2, 8.1, 7.8, 8.2, 7.7
]

# นำข้อมูลเข้าสู่ Pandas Series เพื่อง่ายต่อการคำนวณ
df = pd.Series(data)

print("--- ผลการประมวลผลทางสถิติ ---")

# 4.1 ค่าเฉลี่ยเลขคณิต มัธยฐาน และฐานนิยม
mean_val = df.mean()
median_val = df.median()
mode_val = df.mode().tolist() # อาจมีฐานนิยมมากกว่า 1 ค่า
print(f"4.1 ค่าเฉลี่ยเลขคณิต (Mean): {mean_val:.3f} GB")
print(f"    มัธยฐาน (Median): {median_val:.3f} GB")
print(f"    ฐานนิยม (Mode): {mode_val} GB")

# 4.2 ความแปรปรวนและส่วนเบี่ยงเบนมาตรฐาน (ใช้กลุ่มตัวอย่าง ddof=1)
var_val = df.var(ddof=1)
std_val = df.std(ddof=1)
print(f"4.2 ความแปรปรวน (Variance): {var_val:.4f}")
print(f"    ส่วนเบี่ยงเบนมาตรฐาน (Std Dev): {std_val:.4f} GB")

# การหาตำแหน่งใช้ Interpolation แบบ Linear (ค่าเริ่มต้นของ Pandas)
# 4.3 ควอไทล์ที่ 1 และ 3
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
print(f"4.3 ควอไทล์ที่ 1 (Q1): {q1:.3f} GB")
print(f"    ควอไทล์ที่ 3 (Q3): {q3:.3f} GB")

# 4.4 เดไซล์ที่ 4 และ 7
d4 = df.quantile(0.40)
d7 = df.quantile(0.70)
print(f"4.4 เดไซล์ที่ 4 (D4): {d4:.3f} GB")
print(f"    เดไซล์ที่ 7 (D7): {d7:.3f} GB")

# 4.5 เปอร์เซ็นไทล์ที่ 30 และ 80
p30 = df.quantile(0.30)
p80 = df.quantile(0.80)
print(f"4.5 เปอร์เซ็นไทล์ที่ 30 (P30): {p30:.3f} GB")
print(f"    เปอร์เซ็นไทล์ที่ 80 (P80): {p80:.3f} GB")

# 4.6 สัมประสิทธิ์ความเบ้ (Skewness)
skewness = df.skew()
print(f"4.6 สัมประสิทธิ์ความเบ้ (Skewness): {skewness:.4f}")

# 4.7 สัมประสิทธิ์ความโด่ง (Kurtosis)
kurtosis_val = df.kurtosis()
print(f"4.7 สัมประสิทธิ์ความโด่ง (Kurtosis): {kurtosis_val:.4f}")