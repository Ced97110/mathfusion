import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
Y = 33
def pts(cx, ns, step):
    n = len(ns); xs = [cx + (k - (n - 1) / 2) * step for k in range(n)]
    for x, v in zip(xs, ns): disc(ax, x, Y, 2.5, 'fixe', label=str(v), size='s')
    return xs
def sw(xa, xb, role, up):
    arrow(ax, (xa + 1.2, Y + (2.6 if up else -2.6)), (xb - 1.2, Y + (2.6 if up else -2.6)), role,
          curve=-0.9 if up else 0.9, both=True)
x = pts(15, [1, 2], 12); sw(x[0], x[1], 'varie', True); sw(x[0], x[1], 'sujet', False)
x = pts(44, [1, 2, 3, 4], 8.5); sw(x[0], x[1], 'varie', True); sw(x[2], x[3], 'sujet', False)
x = pts(73, [1, 2, 3], 9); sw(x[0], x[1], 'varie', True); sw(x[0], x[2], 'sujet', False)
for cx, cap in ((15, '2 en commun\nvaut l’identité'), (44, '0 en commun\ns’écrit avec\n2 cycles de 3'), (73, '1 en commun\ns’écrit avec\n1 cycle de 3')):
    text(ax, cx, 12, cap, 'resultat', 's')
text(ax, 44, 49, 'deux échanges : orange et bleu', 'encre', 's')
save(fig, '64-114')
