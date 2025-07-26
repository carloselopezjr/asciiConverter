from ascii_magic import AsciiArt
from PIL import ImageEnhance

imageAddress = input("Enter an image address: ")
columnAmount = int(input("\n Column Amount:"))

asciiImg = AsciiArt.from_url(imageAddress)

asciiImg.to_terminal(columns=columnAmount)

def colorEnhancements(asciiImg, columnAmount):

    print("\n\nColor Enhancement Version\n\n")

    asciiImg.image = ImageEnhance.Contrast(asciiImg.image).enhance(2)
    asciiImg.image = ImageEnhance.Brightness(asciiImg.image).enhance(2.5)
    asciiImg.image = ImageEnhance.Color(asciiImg.image).enhance(0.1)

    asciiImg.to_terminal(columns=columnAmount)
    print("\n\n")

    return 

colorEnhancements(asciiImg, columnAmount)
