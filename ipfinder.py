import urllib.request
import re

# deciding file or url

chooser = str(input("URL of File?: (U/F)  "))

if chooser == "U":

    # getting url from user. Ex: https://isc.sans.edu/block.txt

    inputURL = str(input("Input URL: "))

    # getting data from url with urllib

    inputFile = str(urllib.request.urlopen(inputURL).readlines())

    # opening a file for writing the output

    outputFile = str(input("Output File Name: "))
    text_file = open(outputFile, "w")

    # defining pattern

    ip = re.findall("[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}", inputFile)

    # writing the output to the file

    for i in ip:
        text_file.write(i + "\n")

    text_file.close()

elif chooser == "F":

    # opening the file that contains data. Ex: log.txt

    inputFile = str(input("Input File Name: "))
    infile = open(inputFile, "r")

    # opening a file for writing the output

    outputFile = str(input("Output File Name: "))
    text_file = open(outputFile, "w")

    for line in infile:
        line = line.strip()

        # defining pattern

        ip = re.findall("[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}", line)

        # writing the output to the file

        for i in ip:
            text_file.write(i + "\n")

    text_file.close()

else:
    print("Wrong Input")
