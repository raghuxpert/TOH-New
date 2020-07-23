import math as m

def TowerofHanoi(discs):
   return m.pow(2,discs) - 1

print(int(TowerofHanoi(5)))