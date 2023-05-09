try:  
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
except:
  print(traceback)

for row in myStuff:
  print(row)