print("Microscope Specimen Size Calculator")
specimenSize = float(input("Enter the image size of the maginfied specimen in mm: "))
magnification = int(input("Enter the maginifaction of the object: "))
acutalSize = (specimenSize/magnification) * 1000
print(f"The actual size of the speciment: {acutalSize:.2f} µm")