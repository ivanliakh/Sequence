albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lighning", "Metallica", 1984),
          ]

print(len(albums))


for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print()

for (name, artist, year) in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, lenght, width, height, price = table
# print(width * lenght)
