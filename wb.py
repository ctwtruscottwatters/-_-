import numpy as np
import math as m
import datetime
import struct
from matplotlib import pyplot as plt
# Charles Truscott Watters on my Caterpillar Rugged Phone implementing numerical algorithms
# All my own work
"""
Linear Equation ordered pairs in [x, y] format:  [[0, 1993], [1, 2048], [2, 2103], [3, 2158], [4, 2213], [5, 2268], [6, 2323], [7, 2378], [8, 2433], [9, 2488], [10, 2543], [11, 2598], [12, 2653], [13, 2708], [14, 2763], [15, 2818], [16, 2873], [17, 2928], [18, 2983], [19, 3038], [20, 3093], [21, 3148], [22, 3203], [23, 3258], [24, 3313], [25, 3368], [26, 3423], [27, 3478], [28, 3533], [29, 3588], [30, 3643], [31, 3698], [32, 3753], [33, 3808], [34, 3863], [35, 3918], [36, 3973], [37, 4028], [38, 4083], [39, 4138], [40, 4193], [41, 4248], [42, 4303], [43, 4358], [44, 4413], [45, 4468], [46, 4523], [47, 4578], [48, 4633], [49, 4688], [50, 4743], [51, 4798], [52, 4853], [53, 4908], [54, 4963], [55, 5018], [56, 5073], [57, 5128], [58, 5183], [59, 5238], [60, 5293], [61, 5348], [62, 5403], [63, 5458], [64, 5513], [65, 5568], [66, 5623], [67, 5678], [68, 5733], [69, 5788], [70, 5843], [71, 5898], [72, 5953], [73, 6008], [74, 6063], [75, 6118], [76, 6173], [77, 6228], [78, 6283], [79, 6338], [80, 6393], [81, 6448], [82, 6503], [83, 6558], [84, 6613], [85, 6668], [86, 6723], [87, 6778], [88, 6833], [89, 6888], [90, 6943], [91, 6998], [92, 7053], [93, 7108], [94, 7163], [95, 7218], [96, 7273], [97, 7328], [98, 7383], [99, 7438]]
Quadratic Equation ordered pairs in [x, y] format:  [[0, 1990], [1, 5938], [2, 13796], [3, 25564], [4, 41242], [5, 60830], [6, 84328], [7, 111736], [8, 143054], [9, 178282], [10, 217420], [11, 260468], [12, 307426], [13, 358294], [14, 413072], [15, 471760], [16, 534358], [17, 600866], [18, 671284], [19, 745612], [20, 823850], [21, 905998], [22, 992056], [23, 1082024], [24, 1175902], [25, 1273690], [26, 1375388], [27, 1480996], [28, 1590514], [29, 1703942], [30, 1821280], [31, 1942528], [32, 2067686], [33, 2196754], [34, 2329732], [35, 2466620], [36, 2607418], [37, 2752126], [38, 2900744], [39, 3053272], [40, 3209710], [41, 3370058], [42, 3534316], [43, 3702484], [44, 3874562], [45, 4050550], [46, 4230448], [47, 4414256], [48, 4601974], [49, 4793602], [50, 4989140], [51, 5188588], [52, 5391946], [53, 5599214], [54, 5810392], [55, 6025480], [56, 6244478], [57, 6467386], [58, 6694204], [59, 6924932], [60, 7159570], [61, 7398118], [62, 7640576], [63, 7886944], [64, 8137222], [65, 8391410], [66, 8649508], [67, 8911516], [68, 9177434], [69, 9447262], [70, 9721000], [71, 9998648], [72, 10280206], [73, 10565674], [74, 10855052], [75, 11148340], [76, 11445538], [77, 11746646], [78, 12051664], [79, 12360592], [80, 12673430], [81, 12990178], [82, 13310836], [83, 13635404], [84, 13963882], [85, 14296270], [86, 14632568], [87, 14972776], [88, 15316894], [89, 15664922], [90, 16016860], [91, 16372708], [92, 16732466], [93, 17096134], [94, 17463712], [95, 17835200], [96, 18210598], [97, 18589906], [98, 18973124], [99, 19360252]]
Authored by CTW Truscott Watters. Love you Dad

[Program finished]
"""
class ReturnEquation(object):
    def __init__(self, linear=False, quadratic=False, logarithmic=False, exponential=False, rational=False, trigonometric=False, numerator=None, denominator=None, exponent=None, exp_rational=False, trig=["sin", "cos", "tan"], m=None, x=None, b=None, a=None, c=None, xyrange=[None, None], xy=[]):
        self.xyrange = xyrange
        self.linear = linear
        self.m = m
        self.x = x
        self.b = b
        self.quadratic = quadratic
        self.a = a
        self.c = c
        self.xy = xy
    def __str__(self):
        return str(self.xy)
    def save(self, filename, L):
        x = []
        y = []
        for a in range(len(L)):
            x.append(L[a][0])
        for b in range(len(L)):
            y.append(L[b][1])
        plt.title("Charles Truscott")
        plt.plot(x, y)
        plt.show()
        try:
            plt.savefig(str(filename))
        except IOError:
            print("Unable to save to harddisk.")
        x, y = [], []
        
    def returnLinearEquation(self):
        temp = []
        if (self.linear == True) and (self.xyrange[0] is not None and self.xyrange[1] is not None):
            for x in range(self.xyrange[0], self.xyrange[1], 1):
                temp.append([x, self.m * x + self.b])
        return temp
    def returnQuadraticEquation(self):
        temp = []
        if self.a is not None and self.b is not None and self.c is not None:
            if self.quadratic is not False and self.xyrange[0] is not None and self.xyrange[1] is not None:
                for x in range(self.xyrange[0], self.xyrange[1], 1):
                    temp.append([x, self.a * x ** 2 + self.b * x + self.c])
        return temp
    def returnLogarithmicEquation(self):
        pass
def main():
#    lineq = ReturnEquation(linear=True, m=55, b=1993, xyrange=[0,100])
#        evalLinear = lineq.returnLinearEquation()
#    lineq.save('linearequation_1.jpg', evalLinear)
#    
#    print("Linear Equation ordered pairs in [x, y] format: ", evalLinear)
    quadeq = ReturnEquation(quadratic=True, a=1955, xyrange=[0, 100], b=1993, c=1990)
    evalQuad = quadeq.returnQuadraticEquation()
    quadeq.save('quadraticequation_1.jpg', evalQuad)
    print("Quadratic Equation ordered pairs in [x, y] format: ", evalQuad)
    print("Authored by CTW Truscott Watters. Love you Dad")
    
# Last checked: Wed 11th Aug 2022. 1:27 a.m    . Prototyping. CTWTW

if __name__ == "__main__": main()