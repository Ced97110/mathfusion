import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grp(ax, x, y, u, n, role, label=None, h=8):
    box(ax, x, y, n * u, h, role, label=label)
    for i in range(1, n):
        xx = x + i * u
        line(ax, [(xx, y), (xx, y + 1.6)], role, lw=0.6); line(ax, [(xx, y + h - 1.6), (xx, y + h)], role, lw=0.6)

fig, ax = canvas(50)
u, x0, y = 12, 14, 24
grp(ax, x0, y, u, 2, 'sujet', label='a = 2', h=10); grp(ax, x0 + 2 * u, y, u, 3, 'varie', label='n − a = 3', h=10)
brace(ax, x0, x0 + 5 * u, y + 10.5, 'fixe', label='n = 5', down=False)
text(ax, 44, 14, 'a + (n − a) = n ≡ 0', 'resultat', 'l')
text(ax, 44, 6, '2 + 3 = 5 ≡ 0 (mod 5)', 'resultat', 'm')
save(fig, '44-159')
