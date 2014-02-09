#! /usr/bin/python

import sys

def main(fileName):

    fsvm = open(fileName , 'r')
    lines = fsvm.readlines()
    fsvm.close()

    arffName = fileName + ".arff"    
    farff = open(arffName , 'w')

    farff.writelines("@relation reviews\n")

    line = lines[0].split(" ")
    linelen = len(line)
    for x in range(1 , linelen):
        farff.writelines("@attribute 'word%d' {0 , 1}\n" % (x))
    farff.writelines("@attribute 'class' {-1 , 1}\n")

    farff.writelines("@data\n")

    lineslen = len(lines)
    for y in range(0 , lineslen):
        line = lines[y].split(" ")
        for x in range(1 , linelen):
            val = line[x].rstrip().split(":")
            farff.write("%s," % (val[1]))
        farff.write("%s\n" % (line[0]))
    farff.close()
    

if __name__ == "__main__":
    main(sys.argv[1])
