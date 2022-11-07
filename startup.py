from colors import color
import plotext
import math

cols = ['fc0099', 'ffcc00', '00a651', 'ff6e14', 'ff98b4', 'ff002f', '0019ff', '7700ff', '80002f', 'ff8a75', '00ffbb', '8f8f8f', '22aeff', '9200ff', 'fff800', '9bff0f', 'ff0084', 'ff7fa4', '729ba1', 'ffe3e2']

print("\n")

def sq(num):
    for x in range(divmod(len(cols), 12)[0]+1):
        string = ''
        ln = 0
        for col in cols[x*12:(x+1)*12]:
            space = num*"  "
            bl = num*"██"
            string += color(f'{space}{bl}', f'#{col}')
            ln += 2
        for x in range(num):
            print(string)
        for x in range(num):
            print("")

sq(math.floor(plotext.tw()/50))
