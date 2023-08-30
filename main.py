import time
t = time.strftime('%H: %M: %S')
print(t)
if t >= '00:00:00' and t <= '10:00:00':
    print("Good morning")
elif t >= '10:00:01' and t <= '16:00:00':
    print("Good Evening")
elif t >= '16:00:01' and t <= '20:00:00':
    print("After noon")
elif t >= '20:00:01' and t <= '24:00:00':
    print(" Good Night")