import matplotlib.pyplot as myPlot

myFile = open("D:graph.txt","w")

print("Enter 5 coordinates in the x axis with a space between them and 5 coordinates of the y axis in new line.\n")
x = list(map(int,input().split()))
y = list(map(int,input().split()))

i = 0


myFile.write("Coordinates of x axis.\n")
for i in range(5):
    myFile.write(str(x[i]))
    myFile.write(" ")

myFile.write("\n")
myFile.write("Coordinates of y axis.\n")
for i in range(5):
    myFile.write(str(y[i]))
    myFile.write(" ")


myFile.close()

