import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

# restes de x^i (i = 0..6) sous la règle x^3 = 1 + x, comme (coef. de 1, de x, de x^2)
def mulx(v):
    a, b, c = v
    return (c, a ^ c, b)
rem = [(1, 0, 0)]
for _ in range(6): rem.append(mulx(rem[-1]))
assert len(set(rem)) == 7 and (0, 0, 0) not in rem
fig, ax = canvas(76)
text(ax, 44, 70, 'les 8 triplets possibles du reste', 'sujet', 'm')
text(ax, 44, 63, 'chiffres : coef. de 1, de x, de x²', 'fixe', 's')
W, H, G = 19.0, 15.0, 2.6
x0 = (88 - (4 * W + 3 * G)) / 2
for n in range(8):
    col, row = n % 4, n // 4
    x = x0 + col * (W + G); y = 40 - row * (H + G)
    if n < 7:
        box(ax, x, y, W, H, 'resultat', label=''.join(map(str, rem[n])) + f'\nreste de x{"⁰¹²³⁴⁵⁶"[n]}', size='s')
    else:
        box(ax, x, y, W, H, 'fixe', fill=False, dash=True, label='000\naucun i', size='s')
text(ax, 44, 12, 'sept restes, tous différents', 'resultat', 'm')
text(ax, 44, 5, 'et aucun n’est nul', 'resultat', 'm')
save(fig, '68-199')
