import torch
import sys

if __name__ == '__main__':
	args = sys.argv
	if len(args) != 3:
		print('Usage: {} <model_path> <save_file_name>'.format(args[0]))
		sys.exit(1)
	model_path = args[1]
	save_file_name = args[2]
	m = torch.load(model_path)
	del m['optimizer']
	torch.save(m, save_file_name, _use_new_zipfile_serialization=False)
