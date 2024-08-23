def main():
    x = int
    def Sub1():
        print(x)
    def Sub2():
        x = int
        x = 10
        Sub1()
    x = 5
    Sub2()
