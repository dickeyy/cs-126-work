class Date:
    def __init__(self, m, d):
        self.month = m
        self.day = d

def add_to_month_twice(a, d):
    a = a + a
    d.month = a
    print(a, d.month)

def main():
    a = 7
    b = 9
    d1 = Date(2, 2)
    d2 = Date(2, 2)
    add_to_month_twice(a, d1)
    print(a, b, d1.month, d2.month)
    add_to_month_twice(b, d2)
    print(a, b, d1.month, d2.month)

main()