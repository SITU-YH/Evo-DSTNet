import os
import glob

# ================= 配置 =================
# 你的数据集根目录
dataset_root = '/root/autodl-tmp/DSTNet-plus/datasets/GoPro'
# =======================================

def shift_filenames_to_zero_based(root_path):
    print(f"开始扫描并修正索引 (1-based -> 0-based): {root_path}")
    
    # 遍历所有子目录
    for dirpath, dirnames, filenames in os.walk(root_path):
        # 找到所有 png 图片
        png_files = [f for f in filenames if f.endswith('.png')]
        
        if not png_files:
            continue
            
        # 排序确保按顺序处理
        png_files.sort()
        
        # 检查是否需要处理：
        # 如果第一张图已经是 000000.png，说明已经是 0-based，跳过
        if png_files[0] == '000000.png':
            continue
            
        # 如果第一张图是 000001.png，说明是 1-based，需要减 1
        if png_files[0] == '000001.png':
            print(f"⚡ 正在修正: {os.path.basename(dirpath)} (000001 -> 000000)")
            
            # 必须按顺序处理！
            for filename in png_files:
                # 解析当前的数字
                current_idx = int(os.path.splitext(filename)[0])
                # 新的数字 = 当前数字 - 1
                new_idx = current_idx - 1
                
                old_path = os.path.join(dirpath, filename)
                new_name = f"{new_idx:06d}.png"
                new_path = os.path.join(dirpath, new_name)
                
                # 重命名
                os.rename(old_path, new_path)
        else:
            # 如果既不是 000000 也不是 000001 开头，可能文件名比较乱，提示一下
            print(f"⚠️ 跳过异常文件夹: {os.path.basename(dirpath)} (起始文件: {png_files[0]})")

    print("\n✅ 所有文件索引已修正为从 0 开始！")

if __name__ == '__main__':
    shift_filenames_to_zero_based(dataset_root)