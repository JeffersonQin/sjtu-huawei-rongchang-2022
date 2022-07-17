checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=5,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = "/home/ma-user/work/wrc/data/mask_rcnn_r50_fpn_1x_coco_20200205-d4b0c5d6.pth"  
resume_from = None
workflow = [('train', 1)]
