firstday = 3
actualday = 5
day = 1
while actualday - firstday > 0:
    firstday = firstday + (firstday * 0.1)
    day +=1
print("За" , day,  "день спорстмен пробежал более" , actualday , "км")