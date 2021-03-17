# write a python program to convert seconds to day,hour,minute and seconds.
...

second=int(input("enter the value for seconds: "))

day=(((second//60//24)))
print(f"total day for given seconds:{day}")

hour=((second//60)//60)
print(f"total hours for given seconds: {hour}")

minute=(second//60)
print(f"total minute for given seconds:{minute}")
