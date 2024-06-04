from sympy import mod_inverse

def int_to_string(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def f(k):
    return k**11 - 8*k**10 + 26*k**9 - 408*k**8 + 451*k**7 + 10857*k**6 + 44899*k**5 - 158289*k**4 + 71123*k**3 - 9619896*k**2 - 2036532*k + 439623147

def binary_search(N, nbit=80):
    left = 0
    right = 2**nbit

    while left <= right:
        mid = (left + right) // 2
        mid_value = f(mid)

        if mid_value == N:
            return mid

        if mid_value < N:
            left = mid + 1
        else:
            right = mid - 1

    return None

N = 24671716616329429791501934120401986947906754762069027741103489695301393684913192968714393770506588974171119688004078255560092540876759761037785737486298735119250686595158517199167275161581367984820060098272828867789598314992199539669137605464550007399992348571
enc = 8708668393469727278778838158627673326859139312038572460295304871851740864405543976926208190311440529132718385828240461582019852900615915862789624823351491282779122037086425344420295176523983133369992810358802699128572770491607029762924369849408692830226944146


k = binary_search(N, 80)  
print(k)
p = k**6 + 7*k**4 - 40*k**3 + 12*k**2 - 114*k + 31377
q = k**5 - 8*k**4 + 19*k**3 - 312*k**2 - 14*k + 14011   

e = 65537

def gend (p, q, e):
    phi_n = (p - 1) * (q - 1)
    return mod_inverse(e, phi_n)

d = gend(p,q,e)

def decrypt(c, n, d):
  return pow(c, d, n)

m = decrypt(enc,N,d)
m1 = int_to_string(m)
print(m1)