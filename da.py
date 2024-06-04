import random

/**
 * Преобразует строку в целое число.
 *
 * @param s Строка для преобразования.
 * @return Целое число, полученное преобразованием строки.
 */
def string_to_int(s):
    res = 0
    for c in s:
        res = res * 256 + ord(c)
    return res

/**
 * Преобразует целое число в строку.
 *
 * @param n Целое число для преобразования.
 * @return Строка, полученная преобразованием целого числа.
 */
def int_to_string(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

/**
 * Проверяет, является ли число простым.
 *
 * @param n Проверяемое число.
 * @param num_of_iter Количество итераций для проверки (по умолчанию 10).
 * @return True, если число простое; иначе False.
 */
def is_prime(n, num_of_iter=10):
    if n % 2 == 0:
        return False
    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1
    for _ in range(num_of_iter):
        a = random.randint(2, n - 1)
        if pow(a, t, n) == 1:
            continue
        i = 0
        while i < s:
            if pow(a, 2 ** i * t, n) == n - 1:
                break
            i += 1
        if i == s:
            return False
    return True

/**
 * Генерирует пару простых чисел для криптографии.
 *
 * @param nbit Количество бит в генерируемых числах (по умолчанию 80).
 * @return Пара простых чисел.
 */
def gen_primes(nbit=80):
    while True:
        k = random.getrandbits(nbit)
        p = k ** 6 + 7 * k ** 4 - 40 * k ** 3 + 12 * k ** 2 - 114 * k + 31377
        q = k ** 5 - 8 * k ** 4 + 19 * k ** 3 - 312 * k ** 2 - 14 * k + 14011
        if is_prime(p) and is_prime(q):
            return p, q

/**
 * Шифрует сообщение с использованием открытого ключа.
 *
 * @param msg Сообщение для шифрования.
 * @param n Модуль открытого ключа.
 * @param e Показатель открытого ключа (по умолчанию 65537).
 * @return Шифрованное сообщение.
 */
def encrypt(msg, n, e=65537):
    return pow(msg, e, n)

# Основная часть программы не требует документации в Doxygen,
# поскольку это исполнительный код, а не определение функции.

p, q = gen_primes()
n = p * q

inf = open("flag.txt", "rt")
flag = inf.read()
flag = string_to_int(flag)
inf.close()

enc = encrypt(flag, n)

outf = open("output.txt", "wt")
res = "N = " + str(n) + "\nenc = " + str(enc)
outf.write(res)
outf.close()