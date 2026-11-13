import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def classe(x0, x1, n, role, chiffres):
    box(ax, x0, 30, x1 - x0, 12, role)
    w = (x1 - x0) / n
    for i in range(1, n):
        line(ax, [(x0 + i * w, 31), (x0 + i * w, 41)], role, lw=0.5)
    for i, c in enumerate(chiffres):
        text(ax, x0 + (i + 0.5) * w + (n - len(chiffres)) * w, 36, c, role, 'l')
classe(10, 22, 2, 'sujet', '36')
classe(25, 43, 3, 'autre', '000')
classe(46, 64, 3, 'fixe', '000')
classe(67, 85, 3, 'fixe', '001')
for x, s, r in [(16, 'milliards', 'sujet'), (34, 'millions', 'autre'), (55, 'mille', 'fixe'), (76, 'unités', 'fixe')]:
    text(ax, x, 46, s, r, 's')
arrow(ax, (84, 51), (16, 51), 'varie')
text(ax, 50, 55, r'4$^{\mathrm{e}}$ classe depuis la droite', 'varie', 's')
text(ax, 16, 25, '1 000 000 000', 'sujet', 's')
text(ax, 34, 25, '1 000 000', 'autre', 's')
arrow(ax, (34, 22), (16, 22), 'varie', curve=-0.4)
text(ax, 25, 13, '× 1 000 = mille millions', 'varie', 's')
box(ax, 4, 30, 6, 12, 'limite', fill=False, dash=True)
line(ax, [(4, 30), (10, 42)], 'limite'); line(ax, [(4, 42), (10, 30)], 'limite')
text(ax, 50, 5, '« trente-six milliards un »', 'encre', 'm')
save(fig, '01-085')
