import platform

print(platform.architecture())  # ('64bit', 'ELF')    ('32bit', 'WindowsPE')
print(platform.machine())  # x86_64    AMD64
print(platform.node())  # acer    wsbd0297
print(platform.platform())  # Linux-4.4.0-45-generic-x86_64-with-Ubuntu-16.04-xenial    Windows-10-10.0.10586
print(platform.processor())  # x86_64    Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
print(platform.python_version())  # 3.5.2    2.7.12
print(platform.system())  # Linux    Windows
print(platform.version())  # 66-Ubuntu SMP Wed Oct 19 14:12:37 UTC 2016
print(platform.win32_ver())  # only under windows    ('10', '10.0.10586', '', u'Multiprocessor Free')
