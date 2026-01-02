import os
import re

# === 这里填你现在的图片路径（相对路径） ===
dataset_dir = r"projects/HfutCaptcha/dataset"
# === 这里填你要测试的正则表达式 ===
regex_pattern = r"^[^_]+" 

print("-" * 30)
print(f"📂 正在检查文件夹: {os.path.abspath(dataset_dir)}")

if not os.path.exists(dataset_dir):
    print("❌ 错误：找不到这个文件夹！请检查路径是否正确。")
    print("   提示：请确认你是否在 D:\\captcha_trainer 目录下运行此脚本。")
else:
    files = os.listdir(dataset_dir)
    png_files = [f for f in files if f.endswith('.png')]
    print(f"📄 文件夹里共有 {len(files)} 个文件，其中 {len(png_files)} 张是 png 图片。")
    
    if len(png_files) == 0:
        print("❌ 警告：文件夹里没有 .png 图片！")
    else:
        print("\n🔍 开始测试正则提取（只显示前 5 个）：")
        print(f"   当前正则: {regex_pattern}")
        
        success_count = 0
        for i, f in enumerate(png_files):
            # 模拟 make_dataset.py 的提取逻辑
            match = re.search(regex_pattern, f)
            
            if match:
                label = match.group()
                print(f"   ✅ [第{i+1}张] 文件名: {f}  ->  提取标签: 【{label}】")
                success_count += 1
            else:
                print(f"   ❌ [第{i+1}张] 文件名: {f}  ->  提取失败！(正则不匹配)")
            
            if i >= 4: break # 只看前5个

        print("-" * 30)
        if success_count > 0:
            print("💡 结论：正则没问题，也能读到图片。")
            print("   如果这一步成功，说明问题出在写入权限或 TFRecords 生成部分。")
        else:
            print("💡 结论：正则匹配失败！")
            print("   请修改 model.yaml 里的 ExtractRegex 配置。")