from PIL import Image

afbeelding = Image.open("Markiplier.jpg")

afbeelding.show()

breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)

helf_breedte = afbeelding.wigth // 2
helf_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helf_breedte, helf_hoogte)

kleiner_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleiner_afbeelding.save('Markiplier_klein.jpg')