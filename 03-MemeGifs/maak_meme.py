from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("Markiplier.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("impact.ttf", 22)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "You do you, and I'll do me,\nand we won't do each other, probably."
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=221" + str(tekst_breedte) + ", tekst_hoogte=37" + str(tekst_hoogte))
x = (breedte - tekst_breedte) // 1
y = (hoogte - tekst_hoogte) // 1 
tekengebied.multiline_text((x-2,y-2), tekst, font=lettertype, fill=(250,7,53))

achtergrond.show()

achtergrond.save("meme_met_tekst.jpg")
