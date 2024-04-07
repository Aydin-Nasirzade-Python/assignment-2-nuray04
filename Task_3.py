#import libraries here

def main():
uzunluq=int(input("Enter the wavelength in nm: "))
if 380 <= uzunluq <= 750:
    if 380<=uzunluq<450:
        print("The relevant color is Violet")
    elif 450 <= uzunluq < 495:
        print("The relevant color is Blue")
    elif 495 <= uzunluq < 570:
        print("The relevant color is Green")
    elif 570 <= uzunluq < 590:
        print("The relevant color is Yellow")
    elif 590 <= uzunluq < 620:
        print("The relevant color is Orange")
    else:
        print("The relevant color is Red")
else:
    print("Invalid input!")
  pass

if __name__ == "__main__":
  main()
