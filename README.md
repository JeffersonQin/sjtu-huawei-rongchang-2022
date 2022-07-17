## 环境安装

```powershell
install.ps1
```

## 训练

1. 在 `wrc/data/labeled` 下放置 COCO 格式的数据集
2. 训练
   ```
   cd wrc/mmdetection
   python tools/train.py configs/mask_rcnn/wrc.py --work-dir ../ckpt
   ```

## MISC

* `scripts/cleaner.py` 用于批量修改路径，对应 commit: https://github.com/JeffersonQin/sjtu-huawei-rongchang-2022/commit/d3d8d2bca3329d6288d7ffa3a3e9ba7ae8719f7f
