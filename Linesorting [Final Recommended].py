""" Linesorting """

def main(num, data):
	""" Main Function """
	for _ in range(num):
		text = input()
		data.append(text)
		data.sort(key=len)
	for i in data:
		print(i)
main(int(input()), [])