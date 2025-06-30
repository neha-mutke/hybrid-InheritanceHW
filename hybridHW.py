class A:
    def m1(self):
        print("class A")

class B(A):
    def m2(self):
        print("class B")

class C(A):
    def m3(self):
        print("class c")

class D():
    def m4(self):
        print("class d")        

class E(B):
    def m5(self):
        print("class E")        

class F(C,D):
    def m6(self):
        print("class F")

jay = E()
jay.m1()
jay.m2()
jay.m5()

viru = F()
viru.m1()
viru.m3()
viru.m4()
viru.m6()

       