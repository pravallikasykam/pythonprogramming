def do_stuff(input):
	j, p = [int(j) for j in input.split(" ")]
	print(p-j)
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
