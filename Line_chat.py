def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as i:
		for line in i:
			word = line.strip()
			chat.append(word)
	return chat	

def convert(chat):
	allen_say = 0
	viki_say = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image = 0
	viki_image = 0
	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		#print(s)
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image += 1
			else:
				for w in s[2:]:
					allen_say += len(w)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image += 1
			else:
				for w in s[2:]:
					viki_say += len(w)
	print('Allen說了', allen_say, '個字')
	print('Allen說了', allen_sticker_count, '個貼圖')
	print('Allen用了', allen_image, '個圖片')
	print('Viki說了', viki_say, '個字')
	print('Viki說了', viki_sticker_count, '個貼圖')
	print('Viki用了', viki_image, '個圖片')


def write_file(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('LINE-Viki.txt')
	chat = convert(chat)
	

main()