def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as i:
		for line in i:
			word = line.strip()
			chat.append(word)
	return chat	

def convert(chat):
	new = []
	person = None #先定義person為None無值,以避免檔案的開頭沒有人名,會當掉
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值
			new.append(person + ': ' + line)
	return new

def write_file(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('input.txt')
	chat = convert(chat)
	write_file('output.csv', chat)
	

main()