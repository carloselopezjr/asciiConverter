from ascii_magic import AsciiArt
from PIL import ImageEnhance

imageAddress = input("Enter an image address: ")
columnAmount = int(input("\nColumn Amount: "))
if columnAmount <= 0:
    print("Column amount invalid, defaulting to 200")
    columnAmount = 200


monochromeValue = input("\nMonochrome? (y/n): ")
if monochromeValue == "y":
    monochromeValue = True
elif monochromeValue == "n":
    monochromeValue = False
else:
    print("Invalid, monochrome set to False")
    monochromeValue = False

asciiImg = AsciiArt.from_url(imageAddress)

print("\n\nNon-Color Enhancement Version\n\n")
asciiImg.to_terminal(columns=columnAmount, monochrome=monochromeValue)


# Add option to enable enhancements rather than hardcoded values
def colorEnhancementsPrint(asciiImg, columnAmount, monochromeValue):

    print("\n\nColor Enhancement Version\n\n")

    asciiImg.image = ImageEnhance.Contrast(asciiImg.image).enhance(2)
    asciiImg.image = ImageEnhance.Brightness(asciiImg.image).enhance(2.5)
    asciiImg.image = ImageEnhance.Color(asciiImg.image).enhance(0.1)

    asciiImg.to_terminal(columns=columnAmount, monochrome=monochromeValue)
    print("\n\n")

    return 

colorEnhancementsPrint(asciiImg, columnAmount, monochromeValue)

print("hello world");