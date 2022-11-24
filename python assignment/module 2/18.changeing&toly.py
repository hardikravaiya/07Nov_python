text=input("Writte the text:")

if len(text)>=3:
	cutted_text=text[-3:]
	if not("ing" in cutted_text):
		if  not("ly" in cutted_text[:-2]):
			print("The word don't ends with -ing or -ly")
			text+="ing"
		else:
			print("The word already has -ly")
	else:
		print("The word ends width -ing")
		text=text[:-3]+"ly"

else:
	print("The word is less than 3 caracthers long")
print("")
print(text,"is the final result!")
input()
