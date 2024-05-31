import barcode
from barcode.writer import ImageWriter

# Create the barcode object
ean = barcode.get('ean13', '123456789102', writer=ImageWriter())

# Save the barcode to an image file
filename = ean.save('ean13_barcode')

print(f"Barcode saved as {filename}.")