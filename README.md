# 上海交通大学人工智能百校行动·第三届交大荣昶杯人工智能大赛—线上赛

<div align="center"><del><b>搬砖任务</b></del></div>

* 比赛链接：https://competition.huaweicloud.com/information/1000041750/circumstance
* 说明：https://developer.huaweicloud.com/develop/aigallery/article/detail?id=d59fcb43-0d1e-4339-925f-cf39effc473a
* 数据和模型可能会发布在 release，但也可能不会，~~毕竟我懒~~

## 环境安装

```powershell
install.ps1
```

## 数据集制作

* 首先准备好 `labelme` 标注好的数据
* 使用脚本划分数据集，其中 `<dataset_foler>` 是数据集的路径，`<ratio>` 为划分比例，即多少张图片中抽一张作为 validation，目前只支持整数。输出 COCO 数据集文件夹为原来数据集下的 `train` 和 `val`
  ```
  python scripts/splitter.py <dataset_folder> <ratio>
  ```

最终的数据集路径看起来像这样：

```
<dataset_folder>
├─train
│  ├─JPEGImages
│  └─Visualization
└─val
    ├─JPEGImages
    └─Visualization
```

## 预训练权重下载

```bash
./scripts/download_weights.sh
```

## 训练

1. 在 `wrc/data/labeled` 下分别放置 COCO 格式的训练集 `train` 和测试集 `val`
2. 训练，其中 `wrc.py` 是配置文件
   ```
   cd wrc/mmdetection
   python tools/train.py configs/mask_rcnn/wrc.py --work-dir ../ckpt
   ```

## 模型选择

训练结束后可以使用模型选择脚本进行模型选择

```
python scripts/selector.py <log_file>
```

## 本地推理

模型训练以及选择完毕之后可以进行本地推理

```
python scripts/inference.py <model_config> <model_weights> <coco_dataset_root>
```

其中 `<coco_dataset_root>` 参数为 COCO 数据集的根目录，比方说可以选择 `wrc/data/labeled/val` 作为路径。脚本将在 `wrc/data/labeled/val/results` 下输出该数据集的推理预览。

## 模型转换

由于线上评测平台的 torch 版本极其古老，所以需要用老的格式。转换脚本：

```
python scripts/converter.py <model_path> <save_file_name>
```

## MISC

* `scripts/cleaner.py` 用于批量修改路径，对应 commit: https://github.com/JeffersonQin/sjtu-huawei-rongchang-2022/commit/d3d8d2bca3329d6288d7ffa3a3e9ba7ae8719f7f

## 关于线上评测

将 `upload.ipynb` 在华为云上运行。具体方法见官方文档。

## 训练记录

| Model | Scheduler | seg mAP | Note | Command |
| :-: | :-: | :-: | :-: | :-: |
| mask_rcnn_r50_fpn | 24e/step | 52.5% | bs=1, lr=0.02 | <details><summary>Command</summary><pre>python tools/train.py configs/mask_rcnn/wrc_resnet50_24e.py --work-dir ../ckpt</pre></details> |
| mask_rcnn_x101_32x8d_fpn_mstrain-poly_3x_coco | 20e/step | 65.96% | bs=1, lr=0.012 | <details><summary>Command</summary><pre>python tools/train.py configs/mask_rcnn/wrc_resnet101_20e.py --work-dir ../ckpt</pre></details> |
| mask_rcnn_x101_32x8d_fpn_mstrain-poly_3x_coco | 50e/step | 60.5% | bs=1, lr=0.012<br>+ aug | <details><summary>Command</summary><pre>python tools/train.py configs/mask_rcnn/wrc_resnet101_50e.py --work-dir ../ckpt</pre></details> |
| mask_rcnn_x101_32x8d_fpn_mstrain-poly_3x_coco | 75e/cosine | 66.34% | bs=1, lr=0.012<br>+ aug | <details><summary>Command</summary><pre>python tools/train.py configs/mask_rcnn/wrc_resnet101_cosine_75e.py --work-dir ../ckpt</pre></details> |
| mask_rcnn_x101_32x8d_fpn_mstrain-poly_3x_coco | 20e/cosine-s | **69.8%** | bs=3, lr=0.012<br>+ aug, data | <details><summary>Command</summary><pre>python tools/train.py configs/mask_rcnn/wrc_resnet101_cosine_20e_s.py --work-dir ../ckpt</pre></details> |
| mask_rcnn_x101_32x8d_fpn_mstrain-poly_3x_coco | 20e/cosine-l | 62.73% | bs=2, lr=0.02<br>+ aug, data | <details><summary>Command</summary><pre>python tools/train.py configs/mask_rcnn/wrc_resnet101_cosine_20e_l.py --work-dir ../ckpt</pre></details> |

总结：还是数据不过关。。。新数据还有很多脏数据，没法炼。
