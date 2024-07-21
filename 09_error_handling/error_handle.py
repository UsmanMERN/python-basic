file = open("youtube.txt", "w")

try:
    file.write("learning pyton")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("learning python")
