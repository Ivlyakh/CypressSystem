import csv
import os

proxy = "sample.csv"
with open(proxy, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if line[2] != "none" and line[2] is not None:
            print("Running container with proxy HTTP="+line[2])
            proxy = line[2]
            os.system('docker run -e HTTPS_PROXY=%s renniks/cypress:0.81' % proxy)
            print(" Done")
        else:
            print("Proxy on", line, "set to", line[2])
            os.system('docker run renniks/cypress:0.81')

