import urllib.request
import re

# importing txt address

data = urllib.request.urlopen("https://isc.sans.edu/block.txt").readlines()

# changing data type as string

rexData = str(data)

# defining pattern

ip = re.findall("[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}", rexData)

# opening a txt file for writing the output

text_file = open("Output.txt", "w")

# writing the output

for i in ip:
    text_file.write(i + "\n")

text_file.close()
