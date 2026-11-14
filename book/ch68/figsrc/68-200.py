import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

REM = ['1', 'x', 'x²', '1 + x', 'x + x²', '1 + x + x²', '1 + x²']   # restes de x^i, calculés en 68-198
fig, ax = canvas(106)
C, R, r = (44, 54), 32.0, 9.6
text(ax, 44, 101, 'x³ = 1 + x et α³ = α + 1', 'varie', 'm')
P = []
for i in range(7):
    a = math.radians(90 - i * 360 / 7)
    P.append((C[0] + R * math.cos(a), C[1] + R * math.sin(a)))
for i in range(7):
    p, q = P[i], P[(i + 1) % 7]
    d = math.hypot(q[0] - p[0], q[1] - p[1]); k = (r + 1.0) / d
    arrow(ax, (p[0] + (q[0] - p[0]) * k, p[1] + (q[1] - p[1]) * k), (q[0] - (q[0] - p[0]) * k, q[1] - (q[1] - p[1]) * k), 'fixe', lw=0.8)
for i, (x, y) in enumerate(P):
    disc(ax, x, y, r, 'resultat', label=f'α{"⁰¹²³⁴⁵⁶"[i]}\n{REM[i]}', size='s')
disc(ax, C[0], C[1], 5, 'fixe', label='0', size='m')
text(ax, 44, 12, 'flèche : multiplier par α', 'fixe', 's')
text(ax, 44, 5, r'les 7 éléments non nuls de $\mathbb{F}_8$', 'resultat', 's')
save(fig, '68-200')
