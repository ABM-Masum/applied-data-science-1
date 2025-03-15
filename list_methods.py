capitals = ["Amsterdam", "Tokyo", "London", "Cape Town"]

print(capitals)
print(capitals[0])

capitals.append("Paris")
print(capitals)
print(capitals[1:3])

capitals.reverse()
print(capitals)

capitals.append("Cape Town")
print(capitals)

city_count = capitals.count("Cape Town")
print(city_count)

capitals.remove("Cape Town")
print(capitals)
print(len(capitals))

capitals.insert(0, 100)
print(capitals)

capitals[0] = "Washington"
print(capitals)