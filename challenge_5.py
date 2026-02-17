n = input("enter your favourite number: ")
if n.isdigit():
    m = int(input())
    data = [0] * m
    for i in range(m):
        data[i] = int(input())
        very_light = [0]*m
        normal_load = [0]*m
        heavy_load =[0]*m
        overload = [0]*m
        invalid_entries = [0]*m
        vl = nl = hl = ol = inv = 0
        for i in range(m):
            if data[i] < 0:
                invalid_entries[inv] = data[i]
                inv += 1
            elif 0 <= data[i] <= 5:
                very_light[vl] = data[i]
                vl += 1
            elif 6 <= data[i] <= 25:
                normal_load[nl] = data[i]
                nl += 1
            elif 26 <= data[i] <= 60:
                heavy_load[hl] = data[i]
                hl += 1
            else:
                overload[ol] = data[i]
                ol += 1
                l = "ALURU GANESH"
                PLI=(len(l) - l.count(" ")) % 3
    if (PLI == 2):
        apli = (inv+ vl + ol)
        print("Total valid weights",len(data)-inv)
        print("count of affected items due to PLI:", apli)
        print("length and PLI", len(l), PLI)
        print("normal:", normal_load[:nl])
        print("heavy:", heavy_load[:hl])

else:
    print("invalid number")
