class regr:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        return

    def equ(self, x):
        return self.a*x + self.b

    def add(self, variable):
        addi = 0
        x = self.x
        y = self.y
        r = self.r
        if variable == 'x':
            for i in range(r):
                addi += x[i]
        elif variable == 'y':
            for i in range(r):
                addi += y[i]
        elif variable == 'xy':
            for i in range(r):
                res = x[i] * y[i]
                addi += res
        else:
            for i in range(r):
                squared = x[i] * x[i]
                addi += squared
        return addi

    def findslp(self):
        r = self.r
        return (r*self.add('xy') - self.add('x')*self.add('y')) \
            / (r*self.add('x^2') - self.add('x')*self.add('x'))

    def findintercept(self):
        r = self.r
        return (self.add('x^2')*self.add('y') - self.add('xy')*self.add('x')) \
            / (r*self.add('x^2') - self.add('x')*self.add('x'))

    def setslp(self, a):
        self.a = a

    def setint(self, b):
        self.b = b

    def SSE(self):
        addi = 0
        x = self.x
        y = self.y
        r = self.r
        a = self.a
        b = self.b
        for i in range(r):
            addi += (y[i] - a*x[i] + b) ** 2
        return addi

    def SST(self):
        r = self.r
        y = self.y
        y_avg = self.add('y') / r
        addi = 0
        for i in range(r):
            addi += (y[i] - y_avg) ** 2
        return addi

    def SSR(self):
        return self.SST() - self.SSE()

    def R2(self):
        return 1 - (self.SSE() / self.SST())


def main():
    x = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
         74, 75, 76, 77, 78, 79, 80]
    y = [132, 136, 141, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195,
         201, 206, 212, 218, 223, 229, 234]
    linRegr = regr(x, y, min(len(x), len(y)))
    linRegr.setslp(linRegr.findslp())
    linRegr.setint(linRegr.findintercept())
    print("SSE: {}".format(linRegr.SSE()))
    print("SST: {}".format(linRegr.SST()))
    print("SSR: {}".format(linRegr.SSR()))
    print("R2: {}".format(linRegr.R2()))
    height = input("Calculate weight on: ")
    print("If your height is {} inches, you weigh {} pounds".format(height, linRegr.equ(int(height))))

main()