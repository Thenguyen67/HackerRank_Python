F = int(input()) # input = 5
c = 'H'

for i in range(F):
    print((c*i).rjust(F-1) + c + (c*i).ljust(F-1))

for i in range(F+1):
    print((c*F).center(F*2) + (c*F).center(F*6))

for i in range((F+1)//2):
    print((c*F*5).center(F*6))    

for i in range(F+1):
    print((c*F).center(F*2) + (c*F).center(F*6))    

for i in range(F):
    print(((c*(F-i-1)).rjust(F) + c + (c*(F-i-1)).ljust(F)).rjust(F*6))