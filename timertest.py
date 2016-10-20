import time
def timer():
   now = time.localtime(time.time())
   return now[5]


run = raw_input("Start? > ")
while run == "start":
   
