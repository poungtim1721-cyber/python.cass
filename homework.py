import math
import scipy.stats as stats

n1 = 100  # จำนวนตัวอย่างกลุ่มที่ 1 (โยคะ)
n2 = 100  # จำนวนตัวอย่างกลุ่มที่ 2 (รับประทานยา)
x1 = 30   # ผู้ที่ลดน้ำหนักได้ผลดีจากวิธีโยคะ
x2 = 20   # ผู้ที่ลดน้ำหนักได้ผลจากวิธีรับประทานยา
D0 = 0.50 # ผลต่างของสัดส่วนที่ต้องการทดสอบ (50%)
alpha = 0.05 # ระดับนัยสำคัญ

# คำนวณสัดส่วนของแต่ละกลุ่ม
p1 = x1 / n1
p2 = x2 / n2

# คำนวณค่าสถิติทดสอบ (Z-calculated)
numerator = (p1 - p2) - D0
denominator = math.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
z_cal = numerator / denominator

# คำนวณค่าวิกฤต (Z-critical) สำหรับการทดสอบหางขวา (Right-tailed test)
z_crit = stats.norm.ppf(1 - alpha)

# แสดงผลลัพธ์
print(f"H0: pi_1 - pi_2 <= 0.50")
print(f"H1: pi_1 - pi_2 > 0.50\n")
print(f"Z_cal = {z_cal:.3f}")
print(f"Z_0.95 = {z_crit:.3f}")

# สรุปผลการทดสอบ
if z_cal > z_crit:
    print(f"ผลลัพธ์: Reject H0 -> วิธีโยคะให้ผลดีกว่าเกิน 50%")
else:
    print(f"ผลลัพธ์: Accept H0 -> วิธีโยคะให้ผลดีกว่าไม่เกิน 50% (pi_1 - pi_2 <= 0.50)")