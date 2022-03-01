import os
import datetime
import time

sekundes = int(input("Ievadi sekundes!"))
os.system('clear')
for x in range(sekundes):
  laiks = datetime.time(0, 0, sekundes)
  print(laiks)
  sekundes -= 1
  time.sleep(1)
  os.system('clear')
else:
  print("BOOOM!")
  