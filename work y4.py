#hw 01
#problem 3
#204111 sec 001
millisec=(float)(input("millisec:"))
secord=int(millisec/1000)
minute=int(secord/60)
hour=int(minute/60)
day=int(hour/24)

ho=millisec-(1000*secord)
bo=(millisec/1000)-(60*minute)
co=int(millisec/60000) -(60*hour)
io=int(millisec/3600000) -(24*day)

print('day %.0f'%day,'hour %.0f'%io,'minute %.0f'%co,'secord %.0f'%bo,'millisec %.0f'%ho)
