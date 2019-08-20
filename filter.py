# logcat use of input() 
logcat = input ("PlzInput: ")

result = logcat.replace("V: │ ","")
result = result.replace("I: │ ","")
result = result.replace("V: └─","")
result = result.replace("I: └─","")
result = result.replace("─","")
result = result.strip(" ")
result = result.strip("\n")

text_file = open("logcatResult.txt","w")
text_file.write(result)
text_file.close()
