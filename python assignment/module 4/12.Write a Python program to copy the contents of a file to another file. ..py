# open both files
with open('test.txt','r') as firstfile, open('tested.txt','a') as secondfile:
	
	# read content from first file
	for line in firstfile:
			
			# append content to second file
			secondfile.write(line)
