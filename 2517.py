f = open('2517.txt')
a = f.readline()
a = a.replace("D"," ")
a = a.replace("C"," ")
a = a.replace("A","-")
a = a.replace("B","-")
a = a.replace("E","-")
a = a.replace("F","-")
a = a.split(" ")
print(len(max(a)))