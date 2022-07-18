import sys


if __name__ == '__main__':
	args = sys.argv
	if len(args) != 2:
		print('Usage: {} <log_file>'.format(args[0]))
		sys.exit(1)
	log_file_path = args[1]

	keyword_list = [
		'bbox_mAP',
		'bbox_mAP_50',
		'bbox_mAP_75',
		'bbox_mAP_s',
		'bbox_mAP_m',
		'bbox_mAP_l',
		'bbox_mAP_copypaste',
		'segm_mAP',
		'segm_mAP_50',
		'segm_mAP_75',
		'segm_mAP_s',
		'segm_mAP_m',
		'segm_mAP_l',
		'segm_mAP_copypaste',
	]

	with open(log_file_path, 'r', encoding='gbk') as f:
		contents = f.read()

	lines = contents.split('\n')

	max_epoch = 0
	max_map = 0

	for line in lines:
		flag = False
		for keyword in keyword_list:
			if keyword not in line:
				flag = True
				break
		if flag:
			continue

		epoch = int(line.split('Epoch(val) [')[1].split(']')[0])
		segm_mAP = float(line.split('segm_mAP: ')[1].split(',')[0])

		if segm_mAP > max_map:
			max_epoch = epoch
			max_map = segm_mAP

		print('epoch: {} segm_mAP: {}'.format(epoch, segm_mAP))

	print('max_epoch: {} max_map: {}'.format(max_epoch, max_map))
