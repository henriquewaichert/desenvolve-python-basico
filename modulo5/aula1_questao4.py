import datetime

data_hora_agora = datetime.datetime.now()

formatar_data = f"Data: {data_hora_agora.day:02d}/{data_hora_agora.month:02d}/{data_hora_agora.year}"
formatar_hora = f"Hora: {data_hora_agora.hour:02d}:{data_hora_agora.minute:02d}"

print(formatar_data)
print(formatar_hora)