file = open("devices.txt", "r")
content = file.read()
content_line = content.splitlines()
file.close()
print("Questo è l'array di partenza")
print(content_line)
print("\n")
for lines in content_line:
    line = lines.split(",")
    ip = line[0]
    hostname = line[1]
    os = line[2]
    print("L'indirizzo IP del device è: ", ip)
    print("L'hostname del device è: ", hostname)
    print("Il sistema operativo del device è: ", os)
    print("\n\n")

# TEST SYNC