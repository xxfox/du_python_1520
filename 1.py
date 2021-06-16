duration = int(input("Введите количество секунд: "))
minute = 60
hour = 3600
day = 86400
if duration >= day:
    days = duration // day
    duration -= day * days
    hours = duration // hour
    duration -= hours * hour
    minutes = duration // minute
    sec = duration % minutes
    print(days, "д", hours, "час", minutes, "мин", sec, "сек")
elif duration >= hour:
    hours = duration // hour
    duration -= hours * hour
    minutes = duration // minute
    sec = duration - minutes * minute
    print(hours, "час", minutes, "мин", sec, "сек")
elif duration >= minute:
    minutes = duration // minute
    sec = duration - minutes
    print(minutes, "мин", sec, "сек")
else:
    print(duration, "сек")

