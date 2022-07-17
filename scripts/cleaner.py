import os
import re
import sys

patterns = [
	('/home/ma-user/work/wrc', '..')
]

if __name__ == '__main__':
	args = sys.argv
	if len(args) != 2:
		print('Usage: {} <path>'.format(args[0]))
		sys.exit(1)
	target_path = args[1]
	for path, _, file_list in os.walk(target_path):
		for file_name in file_list:
			if file_name.endswith('.py'):
				file_path = os.path.join(path, file_name)
				with open(file_path, 'r', encoding='utf-8') as f:
					data = f.read()
					for (p1, p2) in patterns:
						data = re.sub(p1, p2, data)
				with open(file_path, 'w', encoding='utf-8') as f:
					f.write(data)
