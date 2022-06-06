file_name = input("Input the filename: ")
file_split = file_name.split(".")
file_ext=file_split[1]
if file_ext=="py":
  print ("The extension is: Python")
if file_ext=="c":
  print("The extension is: C")
elif file_ext=="java":
  print("The extension is: Java")
else
print("Extension is : " + file_ext)
