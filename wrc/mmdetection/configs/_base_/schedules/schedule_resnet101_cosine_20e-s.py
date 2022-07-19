# optimizer
optimizer = dict(type='SGD', lr=0.012, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='CosineAnnealing',
    warmup='linear',
    warmup_iters=1000,
    # init warmup = lr * warmup_ratio
    warmup_ratio=0.001,
    # cosine end = lr * min_lr_ratio
    min_lr_ratio=1e-5)
runner = dict(type='EpochBasedRunner', max_epochs=20)
