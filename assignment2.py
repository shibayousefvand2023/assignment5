import sunau


My_favorite_flowers = [[sunau , rose , golden], 
                        [Anthurium , Dahlia , orchid],
                        [Narges, mikhak, zanbagh],
                        [Strelitzia, Lilium, Glyol]]
print(My_favorite_flowers)

print(My_favorite_flowers[1][2])

for row in My_favorite_flowers:
    print(row)

    for col in My_favorite_flowers:
        print(col)

for i in range (len(My_favorite_flowers)):
    for j in range(len(My_favorite_flowers[i])):
        if i == j:
            print(My_favorite_flowers[i][j])

