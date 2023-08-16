import datetime

date = datetime.datetime.now()

fecha = date.strftime("%d %m %Y").replace(" ", "/")

print(fecha)
