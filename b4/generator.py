def count_down(n):
    print("Start")
    m = 1
    while n > 0:
        print("Yielding", n)
        yield n
        n -= 1
        m+= 1
        print("M nè", m)
    print("Done")
gen = count_down(3) # khởi tạo interator với variable = 3
next(gen) # chạy lần đầu n = 3 => n = 2
next(gen) # chạy lần tiếp theo n = 2 => n = 1
next(gen)