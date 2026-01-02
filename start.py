import os
import sys

# === 1. 强力兼容性补丁 (Patch) ===
print("[-] 正在应用 TensorFlow 2.x 兼容补丁...")
try:
    import tensorflow as tf
    import tensorflow.keras.backend as K
    
    tf.compat.v1.disable_eager_execution()
    
    def set_session(session):
        tf.compat.v1.keras.backend.set_session(session)
    if not hasattr(K, 'set_session'):
        K.set_session = set_session
    
    if hasattr(tf.keras, 'backend') and not hasattr(tf.keras.backend, 'set_session'):
        tf.keras.backend.set_session = set_session
        
    print("✅ 补丁应用成功！")
except Exception as e:
    print(f"⚠️ 补丁应用出现小问题 (可能不影响): {e}")

print("🚀 正在启动 Eve-DL Trainer...")
try:
    with open("app.py", "r", encoding='utf-8') as f:
        code = f.read()
    global_vars = globals().copy()
    global_vars['__name__'] = "__main__"
    exec(code, global_vars)
except Exception as e:
    print(f"❌ 启动失败: {e}")
    input("按回车键退出...")