import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
k = 3.0
for ox, swap in ((9, False), (53, True)):
    O = (ox, 14); P1 = (ox + 6 * k, 14); P2 = (ox + 5 * k, 14 + 4 * k)
    poly(ax, [O, P1, P2], 'sujet' if not swap else 'autre')
    a, b = (P1, P2) if not swap else (P2, P1)
    text(ax, a[0] + 3, a[1] - (2.5 if a == P1 else -3), '1', 'varie', 'm'); text(ax, b[0] + 3, b[1] - (2.5 if b == P1 else -3), '2', 'varie', 'm')
    text(ax, ox + 9, 8, 'aire 12', 'fixe', 's')
    text(ax, ox + 11, 36, '6 × 4 − 5 × 0 = 24' if not swap else '5 × 0 − 6 × 4 = −24', 'resultat' if not swap else 'varie', 's')
arrow(ax, (34, 18), (49, 18), 'varie', both=False); text(ax, 41.5, 22, 'échange', 'varie', 's')
save(fig, '37-138')
