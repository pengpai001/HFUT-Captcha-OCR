import os
import random
import shutil

# === 配置路径 ===
project_root = r"D:\captcha_trainer\projects\HfutCaptcha"
source_dir = os.path.join(project_root, "dataset")  # 原来的图片库
train_dir = os.path.join(project_root, "dataset_train") # 新的训练集文件夹
val_dir = os.path.join(project_root, "dataset_val")     # 新的验证集文件夹

# === 比例配置 (0.1 代表 10% 做验证集) ===
val_ratio = 0.1

print("-" * 30)
print("🚀 开始划分数据集...")

# 1. 检查源文件夹
if not os.path.exists(source_dir):
    print(f"❌ 找不到源文件夹: {source_dir}")
    exit()

# 2. 获取所有 png 图片
images = [f for f in os.listdir(source_dir) if f.endswith(".png")]
total_count = len(images)
print(f"📄 共发现图片: {total_count} 张")

if total_count == 0:
    print("❌ 文件夹是空的！可能你已经分过类了？请检查 dataset_train 文件夹。")
    exit()

# 3. 随机打乱
random.shuffle(images)

# 4. 计算切割点
val_count = int(total_count * val_ratio)
train_count = total_count - val_count

print(f"📊 计划划分: 训练集 {train_count} 张, 验证集 {val_count} 张")

# 5. 创建目标文件夹
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# 6. 开始移动文件
# 移动到验证集
for img in images[:val_count]:
    src = os.path.join(source_dir, img)
    dst = os.path.join(val_dir, img)
    shutil.move(src, dst)

# 移动到训练集
for img in images[val_count:]:
    src = os.path.join(source_dir, img)
    dst = os.path.join(train_dir, img)
    shutil.move(src, dst)

print("✅ 划分完成！")
print(f"   -> 训练集路径: {train_dir}")
print(f"   -> 验证集路径: {val_dir}")
print("-" * 30)