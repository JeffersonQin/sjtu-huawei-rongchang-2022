import os
import sys
import torch
import mmcv
import cv2
import numpy as np
from mmdet.apis import init_detector
from mmdet.apis import inference_detector
from mmdet.apis import show_result_pyplot
from mmdet.core import encode_mask_results


if __name__ == '__main__':
	args = sys.argv
	if len(args) != 4:
		print('Usage: {} <model_config> <model_weights> <coco_dataset_root>'.format(args[0]))
		sys.exit(1)

	model_config = args[1]
	model_weights = args[2]
	coco_dataset_root = args[3]

	device = "cuda" if torch.cuda.is_available() else "cpu"
	cfg = mmcv.Config.fromfile(model_config)
	model = init_detector(cfg, model_weights, device=device)

	file_list = os.listdir(os.path.join(coco_dataset_root, 'JPEGImages'))
	os.makedirs(os.path.join(coco_dataset_root, 'results'), exist_ok=True)

	for file_name in file_list:
		if file_name.endswith('.jpg'):
			print(f'Processing {file_name}')
			img = cv2.imread(os.path.join(coco_dataset_root, 'JPEGImages', file_name))
			res = inference_detector(model, img)
			img_res = model.show_result(img, res, score_thr=0.4, bbox_color=(72, 101, 241), text_color=(72, 101, 241))
			cv2.imwrite(os.path.join(coco_dataset_root, 'results', file_name), img_res)
