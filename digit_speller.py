def Zeroout(string):

    x = 0
    if string == "":
        return None
    elif len(string) == 1:
        return string
    while x < len(string):
        if string[x] == '0':
            x += 1
            continue
        else:
            return string[x::]
    return '0'


def Convert(num):

    global cursor, out
    leng = len(num)
    #print(num, leng, cursor, out)

    if leng == 0:
        return ""
    
    if leng == 1:
        num = Zeroout(num)
        num = int(num)
        if num == 0:
            if cursor == 2:
                out += "тысяч "
            elif cursor == 1:
                out += ""
            else:
                out += base_whole.get(cursor) + "ов "         
        else:
            if cursor == 2:
                if num == 1:
                    out += "одна тысяча "
                else:
                    curr = base_ths.get(num)
                    if (num == 2) or (num == 3) or (num == 4):
                        out += curr + " тысячи "
                    else:
                        out += curr + " тысяч "    
            elif cursor == 1:
                out += base_ord.get(num)
            else:
                if num == 1:
                    out += "один " + base_whole.get(cursor) + " "
                else:
                    curr = base_ord.get(num)
                    if (num == 2) or (num == 3) or (num == 4):
                        out += curr + " " + base_whole.get(cursor) + "а "
                    else:
                        out += curr + " " + base_whole.get(cursor) + "ов "

    if leng == 2:
        num = Zeroout(num)
        num = int(num)
        if num == 10:
            if cursor == 2:
                out += "десять тысяч "
            elif cursor == 1:
                out += "десять"
            else:
                out += "десять " + base_whole.get(cursor) + "ов "
        elif (num//10) == 1:
            curr = base_comp.get(num%10)
            if cursor == 2:
                out += curr + "надцать тысяч "
            elif cursor == 1:
                out += curr + "надцать"
            else:
                out += curr + "надцать " + base_whole.get(cursor) + "ов "
        elif ((num//10) == 2) or ((num//10) == 3):
            curr = base_ord.get(num//10)
            out += curr + "дцать "
            return Convert(str(num%10))
        elif (num//10) == 4:
            out += "сорок "
            return Convert(str(num%10))
        elif (num//10) == 9:
            out += "девяносто "
            return Convert(str(num%10))
        else:
            curr = base_ord.get(num//10)
            out += curr + "десят "
            return Convert(str(num%10))

    if leng == 3:
        if num == "000":
            pass
        else:
            num = int(num)
            if (num//100) == 0:
                return Convert(str(num%100))
            elif (num//100) == 1:
                out += "сто "
                return Convert(str(num%100))
            elif (num//100) == 2:
                out += "двести "
                return Convert(str(num%100))
            else:
                curr = base_ord.get(num//100)
                if ((num//100) == 3) or ((num//100) == 4):
                    out += curr + "ста "
                    return Convert(str(num%100))
                else:
                    out += curr + "сот "
                    return Convert(str(num%100))

    #print('||', out)

while 1:
    inp = Zeroout(input("Value: "))
    if not inp:
        break
    inp = ''.join(inp.split())
    if not inp.isdigit():
        break
    else:
        quot = len(inp) // 3
        rem = len(inp) % 3
        base_whole = {1: "", 2: "тысяч", 3: "миллион", 4: "миллиард",
                      5: "триллион", 6: "квадриллион", 7: "квинтиллион",
                      8: "секстиллион", 9: "септиллион", 10: "октиллион",
                      11: "нониллион", 12: "дециллион"}
        base_ths = {1: "одна", 2: "две", 3: "три", 4: "четыре",
                    5: "пять", 6: "шесть", 7: "семь", 8: "восемь",
                    9: "девять"}
        base_ord = {1: "один", 2: "два", 3: "три", 4: "четыре",
                    5: "пять", 6: "шесть", 7: "семь", 8: "восемь",
                    9: "девять"}
        base_comp = {1: "один", 2: "две", 3: "три", 4: "четыр", 5: "пят",
                     6: "шест", 7: "сем", 8: "восем", 9: "девят"}

        if rem:
            aux = 1
        else:
            aux = 0

        out = ""
        cursor = quot + aux
        if aux:
            Convert(inp[:rem:])
            cursor -= 1

        while cursor:
            Convert(inp[rem:rem+3:])
            rem += 3
            cursor -= 1

        print(out.capitalize())

