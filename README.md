
# Evo-DSTNet: 演进型时空视频去模糊与图像恢复网络


**Evo-DSTNet** 是一个先进的视频去模糊和图像恢复框架。本项目在 DSTNet-plus 的基础上进行了深度重构与演进，引入了类似 EVSSM 的架构优化思路，进一步增强了时空特征提取能力以及基于 Haar 小波变换的图像恢复效果。

## 🚀 核心特性

* **进化的网络架构**：深度融合 Haar 小波分解与优化的时空注意力机制，实现高效且高精度的视频去模糊。
* **基于 BasicSR 框架**：全面兼容稳定强大的 BasicSR 框架，代码结构清晰，易于配置、训练和二次开发。
* **全面的评估指标**：内置对 PSNR, SSIM, NIQE 和 FID 等主流图像质量评估指标的支持。
* **多数据集支持**：提供开箱即用的数据加载器，支持 GoPro, DVD, REDS, Vimeo90K 等经典图像恢复数据集。

## 🛠️ 安装指南

克隆本仓库并安装所需的依赖环境：

```bash
# 克隆仓库
git clone [https://github.com/STYH-3524/Evo-DSTNet.git](https://github.com/STYH-3524/Evo-DSTNet.git)
cd Evo-DSTNet

# 安装依赖 (推荐使用 Python >= 3.8 和对应的 PyTorch 版本)
pip install -r requirements.txt

# 编译并安装 (BasicSR标准安装方式)
python setup.py develop
```

## 📂 数据集准备

Evo-DSTNet 支持多种用于训练和评估的数据集。对于视频去模糊任务，我们强烈推荐从 **GoPro** 数据集开始。

关于如何下载、组织和预处理数据，请参考详细文档：[docs/DatasetPreparation_CN.md](https://www.google.com/search?q=docs/DatasetPreparation_CN.md)。

## 💻 模型训练

你可以通过指定 YAML 配置文件来训练 Evo-DSTNet 模型。在我们的实验中，通常需要训练 60,000 次迭代 (iterations) 才能达到最佳的 PSNR/SSIM 表现。

```bash
# 使用 GoPro 数据集训练 Evo-DSTNet 的单卡/多卡示例命令
python basicsr/train.py -opt options/train/EvoDSTNet/train_EvoDSTNet_GoPro.yml

```

*注：所有的训练配置和流程都由 `basicsr/train.py` 脚本统一管理。*

## 📊 测试与评估

使用以下命令及相应的测试配置文件，对训练好的模型进行质量评估：

```bash
# 测试示例命令
python basicsr/test.py -opt options/test/EvoDSTNet/test_EvoDSTNet_GoPro.yml

```

## 📜 致谢

本项目的实现离不开以下优秀的开源工作：

* [BasicSR](https://github.com/XPixelGroup/BasicSR) - 开源的图像与视频恢复底层工具箱。
* 原先的 [DSTNet-plus](https://github.com/sunny2109/DSTNet-plus) 仓库。

同时，感谢 [EVSSM](https://github.com/kkkls/EVSSM) 相关前沿工作在架构演进思路上提供的灵感。


