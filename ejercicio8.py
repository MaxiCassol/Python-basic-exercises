f = open('ejercicio8.txt', 'w')

f.write("Vamos Open Bootcamp!!!\n")

f.close()

f = open('ejercicio8.txt', 'r+')
f.readline()
f.write("Saludos desde Argentina!!!\n")

f.seek(0)
print(f.read())
f.close()
