n=int(input("n="))

def read_last_lines(filename, no_of_lines=1):
	file = open(filename,'r')
	lines = file.readlines()
	last_lines = lines[-no_of_lines:]
	for line in last_lines:
		print(line)
	file.close()

if __name__ == "__main__":
	filename = "file.txt"
	read_last_lines(filename, n)
