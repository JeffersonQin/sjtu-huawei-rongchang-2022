import os
import shutil
import sys


if __name__ == '__main__':
	args = sys.argv
	if len(args) != 3:
		print('Usage: {} <dataset_folder> <ratio>'.format(args[0]))
		sys.exit(1)
	dataset_folder = args[1]
	ratio = int(args[2])

	os.makedirs(os.path.join(dataset_folder, 'train_raw'), exist_ok=True)
	os.makedirs(os.path.join(dataset_folder, 'val_raw'), exist_ok=True)

	file_list = os.listdir(dataset_folder)
	pool = []
	for file_name in file_list:
		if file_name.endswith('.jpg'):
			pool.append(file_name[:-4])
	index = 0
	for i in range(len(pool)):
		if i % ratio == 0:
			shutil.move(
				os.path.join(dataset_folder, pool[i] + '.jpg'), 
				os.path.join(dataset_folder, 'val_raw', pool[i] + '.jpg'))
			shutil.move(
				os.path.join(dataset_folder, pool[i] + '.json'), 
				os.path.join(dataset_folder, 'val_raw', pool[i] + '.json'))
		else:
			shutil.move(
				os.path.join(dataset_folder, pool[i] + '.jpg'), 
				os.path.join(dataset_folder, 'train_raw', pool[i] + '.jpg'))
			shutil.move(
				os.path.join(dataset_folder, pool[i] + '.json'), 
				os.path.join(dataset_folder, 'train_raw', pool[i] + '.json'))

	convert_script_name = args[0].replace('splitter.py', 'labelme2coco.py')
	label_file_name = args[0].replace('splitter.py', 'labels.txt')

	os.system(f'python {convert_script_name} "{os.path.join(dataset_folder, "train_raw")}" "{os.path.join(dataset_folder, "train")}" --labels {label_file_name}')
	os.system(f'python {convert_script_name} "{os.path.join(dataset_folder, "val_raw")}" "{os.path.join(dataset_folder, "val")}" --labels {label_file_name}')
