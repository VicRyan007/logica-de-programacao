def dozeHoras(n):
    hours_twelve = {'13':'1' , '14':'2', '15':'3', '16':'4' , '17':'5', '18':'6', '19':'7', '20':'8', '21':'9', '22':'10', '23':'11' ,'00':'12' }
    h = n.split(':')
    if h[0] in hours_twelve:
        return hours_twelve[h[0]]+":"+h[1]+ " P.M."


print(dozeHoras("15:25"))