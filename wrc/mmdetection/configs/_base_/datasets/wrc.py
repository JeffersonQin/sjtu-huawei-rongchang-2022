# dataset settings
dataset_type = 'wrc'
data_root_train = '../data/labeled/train/'
data_root_val = '../data/labeled/val/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='RandomCrop', crop_size=(0.7, 0.7), crop_type='relative_range'),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Albu', 
        transforms=[
            dict(type='MultiplicativeNoise', multiplier=[0.5, 1.5], elementwise=True, p=0.3),
            dict(type='ImageCompression', quality_lower=0, quality_upper=20, p=0.5),
            dict(type='PixelDropout', dropout_prob=0.08, per_channel=False, drop_value=0, mask_drop_value=None, p=0.4),
            dict(type='RandomBrightnessContrast', brightness_limit=[-0.2, 0.2], contrast_limit=[-0.2, 0.2], p=0.3),
            dict(
                type='OneOf',
                transforms=[
                    dict(type='Blur', blur_limit=3, p=1.0),
                    dict(type='MedianBlur', blur_limit=3, p=1.0),
                ],
                p=0.3
            ),
        ],
        bbox_params=dict(
            type='BboxParams',
            format='pascal_voc',
            label_fields=['gt_labels'],
            min_visibility=0.0,
            filter_lost_elements=True),
        keymap={
            'img': 'image',
            'gt_masks': 'masks',
            'gt_bboxes': 'bboxes'
        },
    ),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='RandomCrop', crop_size=(0.7, 0.7), crop_type='relative_range'),
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Albu', 
                transforms=[
                    dict(type='MultiplicativeNoise', multiplier=[0.5, 1.5], elementwise=True, p=0.3),
                    dict(type='ImageCompression', quality_lower=0, quality_upper=20, p=0.5),
                    dict(type='PixelDropout', dropout_prob=0.08, per_channel=False, drop_value=0, mask_drop_value=None, p=0.4),
                    dict(type='RandomBrightnessContrast', brightness_limit=[-0.2, 0.2], contrast_limit=[-0.2, 0.2], p=0.3),
                    dict(
                        type='OneOf',
                        transforms=[
                            dict(type='Blur', blur_limit=3, p=1.0),
                            dict(type='MedianBlur', blur_limit=3, p=1.0),
                        ],
                        p=0.3
                    ),
                ],
                bbox_params=dict(
                    type='BboxParams',
                    format='pascal_voc',
                    label_fields=['gt_labels'],
                    min_visibility=0.0,
                    filter_lost_elements=True),
                keymap={
                    'img': 'image',
                    'gt_masks': 'masks',
                    'gt_bboxes': 'bboxes'
                },
            ),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        ann_file=data_root_train + 'annotations.json',
        img_prefix=data_root_train,
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root_val + 'annotations.json',
        img_prefix=data_root_val,
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root_val + 'annotations.json',
        img_prefix=data_root_val,
        pipeline=test_pipeline))
evaluation = dict(metric=['bbox', 'segm'])
