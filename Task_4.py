#import libraries here

def main():
  il = int(input("Enter the year [ex. 2021]: "))
if il > 0:
    if abs(il - 2000) % 12 == 0:
        print(f"{il} is the year of the Dragon")
    elif abs(il - 2001) % 12 == 0:
        print(f"{il} is the year of the Snake")
    elif abs(il - 2002) % 12 == 0:
        print(f"{il} is the year of the Horse")
    elif abs(il - 2003) % 12 == 0:
        print(f"{il} is the year of the Sheep")
    elif abs(il - 2004) % 12 == 0:
        print(f"{il} is the year of the Monkey")
    elif abs(il - 2005) % 12 == 0:
        print(f"{il} is the year of the Rooster")
    elif abs(il - 2006) % 12 == 0:
        print(f"{il} is the year of the Dog")
    elif abs(il - 2007) % 12 == 0:
        print(f"{il} is the year of the Pig")
    elif abs(il - 2008) % 12 == 0:
        print(f"{il} is the year of the Rat")
    elif abs(il - 2009) % 12 == 0:
        print(f"{il} is the year of the Ox")
    elif abs(il - 2010) % 12 == 0:
        print(f"{il} is the year of the Tiger")
    elif abs(il - 2011) % 12 == 0:
        print(f"{il} is the year of the Hare")
else:
    print("Invalid year!")

  pass

if __name__ == "__main__":
  main()
