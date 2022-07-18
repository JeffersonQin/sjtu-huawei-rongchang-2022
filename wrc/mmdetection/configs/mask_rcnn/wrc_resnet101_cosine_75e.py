_base_ = [
    '../_base_/models/mask_rcnn_x101_32x8d_fpn_mstrain-poly_1x_coco.py',
    '../_base_/datasets/wrc.py',
    '../_base_/schedules/schedule_resnet101_cosine_75e.py', '../_base_/runtime_resnet101.py'
]
