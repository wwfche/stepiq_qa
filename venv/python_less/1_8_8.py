x = int(input())
h = int(input())
m = int(input())

minute = int ( (m + x)  % 60 )
hour = int (h + (x + m)/60)
print (hour)
print (minute)