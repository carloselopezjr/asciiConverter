from ascii_magic import AsciiArt
from PIL import ImageEnhance

imageAddress = input("Enter an image address: ")

image = AsciiArt.from_url(imageAddress)

image.to_terminal()