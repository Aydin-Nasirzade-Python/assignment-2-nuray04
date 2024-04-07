#import libraries here

def main():
 ay = input("Enter name of the month [ex. June]: ")
 gun = int(input("Enter the day [ex. 5]: "))
 if(ay == "March" and 20<=gun<=31) or (ay == "April" and 1 <= gun <= 30) or (ay == "May" and 1 <= gun <= 31) or (ay == "June" and 1 <= gun <= 20):
     print(f"{ay} {gun} is in Spring")
 elif(ay == "June" and 21 <= gun <= 30) or (ay == "July" and 1 <= gun <= 31) or (ay == "August" and 1 <= gun <= 31) or (ay == "September" and 1 <= gun <= 21):
     print(f"{ay} {gun} is in Summer")
 elif(ay == "September" and 22 <= gun <= 30) or (ay == "October" and 1 <= gun <= 31) or (ay == "November" and 1 <= gun <= 30) or (ay == "December" and 1 <= gun <= 20):
     print(f"{ay} {gun} is in Fall")
 else:
     print(f"{ay} {gun} is in Winter")
 
  pass

if __name__ == "__main__":
  main()
