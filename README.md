## 环境安装

```powershell
install.ps1
```

## 数据集制作

* 首先准备好 `labelme` 标注好的数据
* 使用脚本划分数据集，其中 `<dataset_foler>` 是数据集的路径，`<ratio>` 为划分比例，即多少张图片中抽一张作为 validation，目前只支持整数。输出 COCO 数据集文件夹为原来数据集下的 `train` 和 `val`
  ```python
  python scripts/splitter.py <dataset_folder> <ratio>
  ```

## 训练

1. 在 `wrc/data/labeled` 下分别放置 COCO 格式的训练集 `train` 和测试集 `val`
2. 训练
   ```
   cd wrc/mmdetection
   python tools/train.py configs/mask_rcnn/wrc.py --work-dir ../ckpt
   ```

## 模型转换

由于线上评测平台的 torch 版本极其古老，所以需要用老的格式。转换脚本：

```
python scripts/converter.py <model_path> <save_file_name>
```

## MISC

* `scripts/cleaner.py` 用于批量修改路径，对应 commit: https://github.com/JeffersonQin/sjtu-huawei-rongchang-2022/commit/d3d8d2bca3329d6288d7ffa3a3e9ba7ae8719f7f
