with open("devices.txt", "r") as data:
    content = data.read()
    content_line = content.splitlines()
    for lines in content_line:
        line = lines.split(",")
        ip = line[0]
        hostname = line[1]
        os = line[2]
        print(f'L\'indirizzo IP del device è: {ip}\nL\'hostname del device è: {hostname}\nIl sistema operativo del device è: {os}\n\n')