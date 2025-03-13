import colorgram
# Extract 6 colors from an image.
colors = colorgram.extract('HDcolor.jpg', 6)
Extracted_colors=[]
for color in colors:
    Extracted_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

print(Extracted_colors)
#[(254, 225, 6), (16, 254, 5), (252, 4, 145), (188, 3, 254), (9, 254, 243)]