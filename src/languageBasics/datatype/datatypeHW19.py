color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
color1 = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
print(color1)

color1 = []
for i in range(len(color)):
    if i not in (0, 4, 5):
        color1.append(color[i])

print(color1)
