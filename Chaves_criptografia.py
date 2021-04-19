from collections import Counter

def converteHexaToBin(text):
    resultado_bin = ''
    for character in text:
        resultado_bin += "{0:04b}".format(int(character, 16))
    return resultado_bin

def monobit_test(text):
    checkUm = 0
    for bit in text:
        if bit == '1':
            checkUm += 1
    if (checkUm > 9654) and (checkUm < 10346):
        return True
    else:
        return False

def poker_test(text):
    segmentoContinuo = [text[i:i+4] for i in range(0, len(text), 4)]
    count = Counter(segmentoContinuo)

    f_i = 0
    for string, qtd in count.items():
        f_i += qtd*qtd
    x = ((16/5000) * f_i) - 5000

    if (x > 1.03) and (x < 57.4):
        return True
    else:
        return False

def runs_test(text):
    count = 1
    repetitions = []
    counter_0 = [0, 0, 0, 0, 0, 0]
    counter_1 = [0, 0, 0, 0, 0, 0]
    if len(text) > 1:
        for i in range(1, len(text)):
            if text[i - 1] == text[i]:
                count += 1
            else:
                repetitions.append([text[i - 1], count])
                count = 1
        repetitions.append([text[i], count])

    for rep in repetitions:
        if rep[0] == '0':
            if rep[1] >= 6:
                counter_0[5] += 1
            else:
                counter_0[rep[1]-1] += 1
        if rep[0] == '1':
            if rep[1] >= 6:
                counter_1[5] += 1
            else:
                counter_1[rep[1]-1] += 1

    zero_ok = False
    one_ok = False
    if (counter_0[0] > 2267) and (counter_0[0] < 2733) and (counter_0[1] > 1079) and (counter_0[1] < 1421) and \
        (counter_0[2] > 502) and (counter_0[2] < 748) and (counter_0[3] > 223) and (counter_0[3] < 402) and \
        (counter_0[4] > 90) and (counter_0[4] < 223) and (counter_0[5] > 90) and (counter_0[5] < 223):
        zero_ok = True

    if (counter_1[0] > 2267) and (counter_1[0] < 2733) and (counter_1[1] > 1079) and (counter_1[1] < 1421) and \
        (counter_1[2] > 502) and (counter_1[2] < 748) and (counter_1[3] > 223) and (counter_1[3] < 402) and \
        (counter_1[4] > 90) and (counter_1[4] < 223) and (counter_1[5] > 90) and (counter_1[5] < 223):
        one_ok = True

    if zero_ok and one_ok:
        return True
    else:
        return False

def long_run(text):
    count = 1
    if len(text) > 1:
        for i in range(1, len(text)):
            if text[i - 1] == text[i]:
                count += 1
            else:
                if count >= 34:
                    return False
                count = 1
    return True

chaves = open('chaves.txt', 'r')
chavesFiltradas = []
ChavesBin = []

for chave in chaves:
    temp = chave[1:]
    temp = temp[:-2]
    a = len(temp)
    chavesFiltradas.append(temp)
    ChavesBin.append(converteHexaToBin(temp))

num_bin = 1
for binary in ChavesBin:
    monobit = monobit_test(binary)
    poker = poker_test(binary)
    runs = runs_test(binary)
    long = long_run(binary)
    
    if monobit and poker and runs and long:
        print("Chave " + str(num_bin) + ": Aprovada!")
        
    else:
        print("Chave " + str(num_bin) + ": Reprovada!" + " Monobit Test: " + str(monobit) + ". Poker Test: " +
              str(poker) + ". Runs Test: " + str(runs) + ". Long Run Test: " + str(long))
    num_bin += 1