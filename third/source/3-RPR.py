import numpy as np
import matplotlib.pyplot as plt

# ===== 中文字体 =====
plt.rcParams['font.sans-serif'] = ['PingFang HK']
plt.rcParams['axes.unicode_minus'] = False

# ===== 参数 =====
R_base = 5
R_platform = 2
theta_offset = np.pi / 6

theta = np.array([0, 2*np.pi/3, 4*np.pi/3])

# ===== 基座 =====
A = np.vstack((R_base * np.cos(theta),
               R_base * np.sin(theta)))

# ===== 动平台 =====
B = np.vstack((R_platform * np.cos(theta + theta_offset),
               R_platform * np.sin(theta + theta_offset)))

# ===== P副（滑块位置：用比例参数表示，不再取中点！）=====
s = np.array([0.35, 0.55, 0.75])  # 每条支链不同滑动位置（关键修正）

C = A + (B - A) * s   # 沿支链方向滑动

# ===== 绘图 =====
plt.figure()
ax = plt.gca()
ax.set_aspect('equal')

# ===== 机架 =====
A_close = np.hstack((A, A[:, [0]]))
plt.fill(A_close[0], A_close[1], alpha=0.2, label='机架（定平台）')

# ===== 动平台 =====
B_close = np.hstack((B, B[:, [0]]))
plt.fill(B_close[0], B_close[1], alpha=0.2, label='动平台')

# ===== 支链 =====
for i in range(3):
    # R → P（定平台到滑块）
    plt.plot([A[0, i], C[0, i]],
             [A[1, i], C[1, i]],
             'k-', linewidth=2)

    # P → R（滑块到动平台）
    plt.plot([C[0, i], B[0, i]],
             [C[1, i], B[1, i]],
             'k-', linewidth=2)

    # ===== P副滑动方向（关键表达）=====
    direction = B[:, i] - A[:, i]
    direction = direction / np.linalg.norm(direction)

    plt.arrow(C[0, i], C[1, i],
              0.6*direction[0], 0.6*direction[1],
              head_width=0.15, color='blue')

# ===== 关节 =====
plt.plot(A[0], A[1], 'ro', label='R副（定平台）')
plt.plot(C[0], C[1], 'bo', label='P副（移动副/滑块）')
plt.plot(B[0], B[1], 'go', label='R副（动平台）')

# ===== 标注 =====
for i in range(3):
    plt.text(A[0, i], A[1, i], f'A{i+1}')
    plt.text(B[0, i], B[1, i], f'B{i+1}')

# ===== 图形 =====
plt.title('3-RPR 平面并联机构简图')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()