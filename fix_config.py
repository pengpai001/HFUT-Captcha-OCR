import os
import yaml

# 这是一个完整的、健康的配置文件结构
config_content = {
    # 1. 补回丢失的系统配置 (System)
    "System": {
        "Version": "1.0",
        "MemoryUsage": 0.7,
        "Language": "CN"
    },
    # 2. 修复模型配置 (Model)
    "Model": {
        "Sites": ["HfutCaptcha"],
        "ModelName": "HfutCaptcha",
        "ModelType": "CTC",
        "CharSet": "ALPHANUMERIC",
        "CharExclude": "",
        "CharReplace": {},
        "ImageWidth": 128,
        "ImageHeight": 64,
        "Channel": 1,
        "CNNNetwork": "CNNX",
        "RecurrentNetwork": "GRU",
        "UnitsNum": 64,
        "Optimizer": "RAdam",
        "LearningRate": 0.001,
        # 3. 补上刚才报错缺失的标签来源 (LabelFrom)
        "LabelFrom": "FileName", 
        "CompileModelPath": "./projects/HfutCaptcha/out/graph/HfutCaptcha.pb",
        "Trains": {
            "EndAccuracy": 0.95,
            "EndCost": 0.5,
            "EndEpochs": 2,
            "BatchSize": 64,
            "ValidationBatchSize": 32,
            "SavedStep": 100 
        },
        "Dataset": {
            "TrainPath": "./projects/HfutCaptcha/dataset_train",
            "ValidationPath": "./projects/HfutCaptcha/dataset_val",
            "TestPath": ""
        }
    }
}

# 目标文件路径
target_file = r"D:\captcha_trainer\projects\HfutCaptcha\model.yaml"

print(f"[-] 正在全面修复配置文件: {target_file}")

try:
    with open(target_file, 'w', encoding='utf-8') as f:
        yaml.dump(config_content, f, default_flow_style=False, sort_keys=False)
    print("✅ 配置文件已完美重建！(System + LabelFrom 已修复)")
except Exception as e:
    print(f"❌ 修复失败: {e}")

print("👉 现在请直接运行 python start.py，然后点击 Compile 即可！")