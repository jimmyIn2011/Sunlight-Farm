import random


def shengcheng_timu():
    timu = [str(random.randint(10, 1000)) + " " + random.choice(["+", "-", "*"]) + " " + str(random.randint(10, 1000)) +" = ?"]
    answer = random.choice(["A", "B", "C", "D"])
    answers = [timu[0]]
    for i in ["A", "B", "C", "D"]:
        if i != answer:
            append = eval(timu[0].strip(" = ?"))
            answers.append(i + "." + str(eval(str(append) + random.choice(["+", "-"]) + str(random.randint(1, 5)))))
        else:
            answers.append(i + "." + str(eval(timu[0].strip(" = ?"))))
    answers.append(answer)
    return answers


now = [1, 1, 1, 1, 1, 1, 1, 1, 1]
pos = [[0, 200], [170, 200], [340, 200],
       [0, 370], [170, 370], [340, 370],
       [0, 540], [170, 540], [340, 540]]
tian_money = [10, 25, 50, 60, 70, 90, 110, 135, 150]
k = 1000
b = 1000000
tian_poses = [[1, 2, 4], [2, 4, 8], [4, 8, 14], [15, 20, 50], [100, 200, 400], [360, 500, 760], [1.1*k, 1.3*k, 1.6*k],
              [2*k, 2.3*k, 2.5*k], [2.8*k, 3.1*k, 3.3*k]]
zuowu_lock = [[1, 2, 3], [2, 4, 8], [3, 10, 14], [6, 14, 25], [10, 30, 45], [15, 35, 50], [24, 75, 100], [40, 86, 136],
              [56, 100, 165]]
tian_coollect = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
tm_pos = [[0 + 32, 200 + 34], [170 + 32, 200 + 34], [340 + 32, 200 + 34],
          [0 + 32, 370 + 34], [170 + 32, 370 + 34], [340 + 32, 370 + 34],
          [0 + 32, 540 + 34], [170 + 32, 540 + 34], [340 + 32, 540 + 34]]
shop = ["加速剂", "阳光X2倍"]
sunlight = 10
tongguan_shuliang = {1: 1, 2: 20, 3: 48, 4: 60, 5: 100, 6: 200, 7: 350, 8: 500, 9: 780, 10: 1000,
                     11: 2500, 12: 4000, 13: 5000, 14: 7800, 15: 10000, 16: 12000, 17: 14588, 18: 17500, 19: 20000,
                     20: 22000, 21: 25000, 22: 27800, 23: 30000, 24: 32000, 25: 35000, 26: 38900, 27: 40000,
                     28: 42000, 29: 45000, 30: 49000, 31: 51000, 32: 53000, 33: 55000, 34: 57000, 35: 60090,
                     36: 62080, 37: 64900, 38: 68000, 39: 70000, 40: 72000, 41: 74500, 42: 77800, 43: 80000,
                     44: 82400, 45: 84800, 46: 87080, 47: 90000, 48: 92000, 49: 94000, 50: 97890, 51: 100000,
                     52: 102000, 53: 105670, 54: 108900, 55: 110400, 56: 116000, 57: 120500, 58: 129000,
                     59: 137000, 60: 146370, 61: 153060, 62: 168000, 63: 179000, 64: 190200, 65: 200000,
                     66: 210400, 67: 221050, 68: 234030, 69: 247400, 70: 257000, 71: 268900, 72: 280000,
                     73: 290000, 74: 300000, 75: 310300, 76: 100000, 77: 320600, 78: 338000, 79: 350000,
                     80: 360000, 81: 370300, 82: 381000, 83: 392500, 84: 405000, 85: 410000, 86: 410400,
                     87: 417900, 88: 420000, 89: 421000, 90: 422000, 91: 423000, 92: 430000, 93: 432000, 94: 435000,
                     95: 440000, 96: 443000, 97: 446660, 98: 448990, 99: 449000, 100: 450000, 101: 453000,
                     102: 456770, 103: 459000, 104: 460000, 105: 462530, 106: 465700, 107: 469000, 108: 470000,
                     109: 472560, 110: 477660, 111: 480000, 112: 483000, 113: 486000, 114: 490000, 115: 492000,
                     116: 495000, 117: 498000, 118: 500000, 119: 510000, 120: 520000}
now_guan = 1
guan = 0
renwu = ["打开一次", "做题"]
jiangli = ["", ""]
wc = [0, 0]
int_jiangli = [20, 30]
if __name__ == '__main__':
    print(shengcheng_timu())
