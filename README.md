# HFUT-Captcha-OCR
```
# HFUT-Captcha-Recognition (合工大验证码识别训练框架)

> 基于深度学习的合肥工业大学教务系统验证码识别方案 | Research on Deep Learning for HFUT Captcha

![TensorFlow](https://img.shields.io/badge/TensorFlow-1.14%2F2.x-orange)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 项目简介 (Introduction)

本项目是针对 **合肥工业大学 (HFUT)** 教务系统及统一认证平台（CAS）验证码设计的深度学习训练框架。

项目基于开源项目 **captcha_trainer** 进行二次开发与深度适配，针对校内特有的“字符粘连”与“干扰线”验证码进行了定向采集与模型调优。本项目旨在探索 CNN+RNN+CTC 架构在特定低分辨率验证码识别场景下的应用性能。

> **注意**：本项目仅包含**模型训练框架**与**识别接口**，不包含任何自动登录、选课脚本或业务逻辑代码。

---

## 🛠️ 技术特性 (Features)

本项目在原框架基础上进行了以下 **特定场景适配**：

1.  **专用数据集适配**：
    * 针对 `HfutCaptcha` 场景构建了专用配置文件 `model.yaml`。
    * 优化了 CNNX (卷积层) + GRU (循环层) 的参数组合，适应 128x64 分辨率输入。
2.  **高精度收敛**：
    * 在 400 steps 训练周期内，CTC Loss 成功收敛至 0.02。
    * 验证集 (Validation Set) 准确率超过 98%。
3.  **兼容性修复**：
    * 内置 `start.py` 启动脚本，修复了原框架在 TensorFlow 2.x 环境下的兼容性问题。
    * 修复了 YAML 配置文件解析异常问题。

---

## 🤝 致谢与版权声明 (Credits)

本项目核心训练框架源自 **[kerlomz/captcha_trainer](https://github.com/kerlomz/captcha_trainer)**。

* **原作者**：[kerlomz](https://github.com/kerlomz)
* **核心算法**：本项目沿用了原作者设计的端到端网络架构 (CNN + RNN + CTC) 及数据打包流程。
* **工作说明**：本仓库仅包含针对 HFUT 场景的配置文件、特定数据集接口及环境适配脚本，底层核心算法版权归原作者所有。

*在此向所有开源贡献者致敬！*

---

## 📂 目录结构

```text
HFUT-Captcha-Recognition/
├── start.py             # [新增] 兼容性启动脚本 (推荐入口)
├── fix_config.py        # [工具] 配置文件修复工具
├── app.py               # [核心] 训练可视化控制台 (源自 captcha_trainer)
├── projects/            # [配置] 项目文件
│   └── HfutCaptcha/     # 针对 HFUT 的模型配置 (model.yaml)
├── network/             # [底层] 神经网络结构定义
├── optimizer/           # [底层] 优化器实现
└── ...
```

## 🚀 使用说明 (Usage)

### 1. 环境安装

Bash

```
pip install -r requirements.txt
```

### 2. 启动训练控制台

本项目已内置 TF 2.x 兼容补丁，请务必通过以下命令启动：

Bash

```
python start.py
```

### 3. 编译模型

在弹出的界面中：

1. 选择项目 `HfutCaptcha`。
2. 点击 **Compile** 按钮。
3. 生成的 `.pb` 模型文件将位于 `projects/HfutCaptcha/out/graph/` 目录下。

------

## ⚠️ 免责声明 (Disclaimer)

**使用本项目即代表您已接受以下条款：**

1. **仅供科研与学习**：本项目仅用于 **深度学习图像识别技术交流**、**Python 编程教学** 以及 **验证码安全性研究**。
2. **严禁非法用途**：任何个人或组织不得利用本项目生成的模型进行 **恶意攻击教务系统、批量注册、暴力破解** 等违反学校规定或国家法律法规的行为。
3. **无业务代码**：本项目纯属技术研究，**不提供** 也不支持任何形式的抢课、刷课脚本。
4. **免责条款**：作者不对因使用本技术造成的任何直接或间接后果（如账号风险、法律责任）承担责任。

**技术本无罪，请由使用者坚守道德底线。**

------

Copyright © 2026 HFUT-Student-Dev. All Rights Reserved.
