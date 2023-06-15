from math import sqrt
from ecpy.curves import Curve, Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.ecdsa import ECDSA


# Задание 1.1
print("\nЗадание 1.1")
for x in range(551, 585):
    y = sqrt((x ** 3 - x + 1) % 751)
    print(f"{x}; {y}")


# Задание 1.2
print("\nЗадание 1.2")
ec = Curve.get_curve('secp256k1')
ec._domain['a'] = -1
ec._domain['b'] = 1
ec._domain['field'] = 751
G = Point(0, 1, ec)
ec._domain['generator'] = G
# print(ec._domain)

P = Point(210, 31, ec)
Q = Point(106, 24, ec)
R = Point(159, 13, ec)
k = 11
l = 3

result = ec.mul_point(k, P)
print(f"k*P:\t\t({result.x}, {result.y})")

result = ec.add_point(P, Q)
print(f"P+Q:\t\t({result.x}, {result.y})")

result = ec.sub_point(ec.add_point(ec.mul_point(k, P), ec.mul_point(l, Q)), R)
print(f"k*P+l*Q-R:\t({result.x}, {result.y})")

result = ec.add_point(ec.sub_point(P, Q), R)
print(f"P-Q+R:\t\t({result.x}, {result.y})")




# Задание 2
print("\nЗадание 2")
ALPHABET_POINTS  = {
    'А': Point(189, 297, ec), 'Р': Point(206, 106, ec),
    'Б': Point(189, 454, ec), 'С': Point(206, 645, ec),
    'В': Point(192, 32, ec), 'Т': Point(209, 82, ec),
    'Г': Point(192, 719, ec), 'У': Point(209, 669, ec),
    'Д': Point(194, 205, ec), 'Ф': Point(210, 31, ec),
    'Е': Point(194, 546, ec), 'Х': Point(210, 720, ec),
    'Ж': Point(197, 145, ec), 'Ц': Point(215, 247, ec),
    'З': Point(197, 606, ec), 'Ч': Point(215, 504, ec),
    'И': Point(198, 224, ec), 'Ш': Point(218, 150, ec),
    'Й': Point(198, 527, ec), 'Щ': Point(218, 601, ec),
    'К': Point(200, 30, ec), 'Ъ': Point(221, 138, ec),
    'Л': Point(200, 721, ec), 'Ы': Point(221, 613, ec),
    'М': Point(203, 324, ec), 'Ь': Point(226, 9, ec),
    'Н': Point(203, 427, ec), 'Э': Point(226, 742, ec),
    'О': Point(205, 372, ec), 'Ю': Point(227, 299, ec),
    'П': Point(205, 379, ec), 'Я': Point(227, 452, ec)
}
message = "ВАЛЕРИЯ"
print(f"Сообщение: {message}")
d = 18
Q = ec.mul_point(d, G)
print(f"Открытый ключ: ({Q.x}, {Q.y})")

# Зашифрование
c1 = ec.mul_point(k, G)
print(f"C1: ({c1.x}, {c1.y})")
cipher = []
for m in message:
    c2 = ec.add_point(ALPHABET_POINTS[m], ec.mul_point(k, Q))
    cipher.append((c1, c2))
print("\nШифр:")
for tup in cipher:
    print(f"C1 :({tup[0].x}, {tup[0].y}); C2: ({tup[1].x}, {tup[1].y})")

# Расшифрование
decipher = ""
for tup in cipher:
    p = ec.sub_point(tup[1], ec.mul_point(d, tup[0]))
    decipher += [k for k, v in ALPHABET_POINTS.items() if v == p][0]
print(f"\nРасшифрованное сообщение: {decipher}")




# Задание 3
print("\nЗадание 3")

ec = Curve.get_curve('secp256k1')
ec._domain['a'] = -1
ec._domain['b'] = 1
ec._domain['field'] = 751
G = Point(416, 55, ec)
ec._domain['generator'] = G
ec._domain['order'] = 13

d = 18
Q = ec.mul_point(d, G)
print(f"Открытый ключ: ({Q.x}, {Q.y})")
print(f"Тайный ключ: {d}")

message = b"VALERIA"

signer = ECDSA()
public_key = ECPublicKey(Q)
private_key = ECPrivateKey(d, ec)
sig = signer.sign(message, private_key)
print(f"Проверка подписи: {signer.verify(message, sig, public_key)}")
