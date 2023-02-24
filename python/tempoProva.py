hora = int(input("Horas: "))
minuto = int(input("Minutos: "))

horaMinuto = (hora * 60) + minuto
minutoSegundo = horaMinuto * 60

print(horaMinuto, " minutos ", "\n",
minutoSegundo, " segundos ")
