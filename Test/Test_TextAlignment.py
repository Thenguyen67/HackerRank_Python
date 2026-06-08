ip = 5
c00 = 'V'
c01 = 'U'

for i in range(ip):
    print((c00*(ip-1)).center(ip*2) + (c01*(ip-2)).center(ip*1))