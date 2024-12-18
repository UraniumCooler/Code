axelSold = 15
petraSold = 8
axelEarn = 7 * axelSold
petraEarn = 13 * petraSold
if axelEarn > petraEarn:
    print(f"Axel kännar mäst på testdatan, hen kännade {axelEarn}")
elif axelEarn < petraEarn:
    print(f"Petra kännar mäst på testdatan, hen kännade {petraEarn}")
else:
    print(f"Båda kännar lika mycket på testdatan, dem kännade {axelEarn} och {petraEarn}")