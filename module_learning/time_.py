import time

## gmtime
# like localtime but shows greenwich time
print("\ntime.gmtime:")
print(time.gmtime(1477293843.2737696))

## localtime
# seconds to struct
print("\ntime.localtime:")
print(time.localtime(1477293843.2737696))  # time.struct_time(tm_year=2016, tm_mon=10, tm_mday ...

## mktime
# struct to seconds
print("\ntime.mktime:")
print(time.mktime(time.struct_time(time.localtime())))

## sleep
time.sleep(1)

## strftime
# seconds to string
print("\ntime.strftime:")
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))  # Mon, 24 Oct 2016 07:22:35 +0000

## strptime
# string to string
print("\ntime.strptime:")
print(time.strptime("30 Nov 00", "%d %b %y"))  # time.struct_time(tm_year=2000, tm_mon=11, tm_mday ...

## time
# get seconds
print("\ntime.time:")
print(time.time())  # 1477293843.2737696
