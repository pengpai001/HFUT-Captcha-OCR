import os
import sys
# 假装我们是 make_dataset.py，读取一样的配置
from config import ModelConfig, DatasetType

# 指定你的项目名
project_name = "HfutCaptcha"

print("=" * 50)
print("🕵️‍♂️ 侦探脚本正在运行...")
print(f"当前工作目录 (CWD): {os.getcwd()}")

try:
    # 1. 加载配置
    conf = ModelConfig(project_name)
    
    # 2. 获取程序计算出的【真实写入路径】
    # 这里的逻辑和 make_dataset.py 一模一样
    raw_path = conf.trains_path[DatasetType.TFRecords]
    
    # 兼容处理：如果配置返回的是列表，取第一个
    if isinstance(raw_path, list):
        target_path = raw_path[0]
    else:
        target_path = raw_path
        
    # 3. 打印真相
    print(f"\n👉 配置文件里写的路径是: {target_path}")
    abs_path = os.path.abspath(target_path)
    print(f"👉 Python 最终写入的【绝对路径】是:\n   {abs_path}")
    
    print("-" * 30)
    
    # 4. 现场验证文件是否存在
    if os.path.exists(abs_path):
        size = os.path.getsize(abs_path)
        print(f"✅ 找到了！文件确实就在这里！")
        print(f"📄 文件大小: {size / 1024 / 1024:.2f} MB")
        if size == 0:
            print("⚠️ 警告：文件是空的 (0 KB)！可能之前生成失败了。")
    else:
        print("❌ 奇怪，这个路径下居然没有文件！")
        # 检查父文件夹是否存在
        parent_dir = os.path.dirname(abs_path)
        if os.path.exists(parent_dir):
            print(f"   (但是文件夹 {parent_dir} 是存在的)")
            print(f"   请检查此文件夹下是否有名字类似的文件？")
            print(f"   文件夹内容: {os.listdir(parent_dir)}")
        else:
            print(f"   (连文件夹 {parent_dir} 都不存在！)")

except Exception as e:
    print(f"\n❌ 读取配置报错: {e}")
    print("可能原因：model.yaml 格式写错了，或者项目名不对。")

print("=" * 50)