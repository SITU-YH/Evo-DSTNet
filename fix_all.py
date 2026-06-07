import os
import glob

# ================= 配置 =================
# 数据集根目录
dataset_root = '/root/autodl-tmp/DSTNet-plus/datasets/GoPro'
# 指定需要扫描的子文件夹名称（根据你的实际情况）
target_subfolders = ['blur', 'sharp'] 
# =======================================

def rename_files_recursive(root_path):
    print(f"开始扫描根目录: {root_path}")
    
    # 遍历 train 和 test (如果有)
    for split in ['train', 'test']:
        split_path = os.path.join(root_path, split)
        if not os.path.exists(split_path):
            continue
            
        # 遍历 blur 和 sharp
        for sub in target_subfolders:
            # 拼凑出 .../train/sharp
            current_section = os.path.join(split_path, sub)
            if not os.path.exists(current_section):
                print(f"  [跳过] 找不到文件夹: {current_section}")
                continue
            
            print(f"📂 正在处理: {current_section}")
            
            # 获取下面的视频文件夹 (例如 GOPR0384_11_03)
            video_folders = sorted(os.listdir(current_section))
            
            for video in video_folders:
                video_path = os.path.join(current_section, video)
                if not os.path.isdir(video_path):
                    continue
                
                # 获取所有 png 图片
                files = sorted(glob.glob(os.path.join(video_path, '*.png')))
                if not files:
                    continue
                
                # 如果第一张已经是 000001.png，说明改过了
                if os.path.basename(files[0]) == '000001.png':
                    continue

                # print(f"    -> 重命名 {video} 中的 {len(files)} 张图片...")
                
                # 批量重命名: 002101.png -> 000001.png
                for i, file_path in enumerate(files):
                    new_name = f"{i+1:06d}.png"
                    os.rename(file_path, os.path.join(video_path, new_name))

    print("\n✅ 所有文件名已修正为标准格式 (000001.png...)")

if __name__ == '__main__':
    rename_files_recursive(dataset_root)