import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def row(x0, y, digits, role, start, end, curve, label, result):
    bx = lambda k: x0 + k * 12
    for i, d in enumerate(digits):
        box(ax, bx(i) + 0.5, y, 11, 12, role, label=d, size='l')
    disc(ax, bx(start), y, 1.1, 'fixe'); disc(ax, bx(end), y, 1.1, 'resultat')
    step = 1 if end > start else -1
    for k in range(start, end, step):
        a, b = bx(k) - 1 * step * -1 if False else bx(k) + step, bx(k + step) - step
        arrow(ax, (a, y + 16), (b, y + 16), 'varie', curve=curve)
    text(ax, 44, y + 25, label, 'varie', 'm')
    text(ax, 44, y - 7, result, 'encre', 'm')
row(26, 58, '981', 'sujet', 3, 1, 0.6, r'2 rangs à gauche : $e=2$', r'$981=9{,}81\times10^{2}$')
row(20, 15, '0027', 'autre', 1, 3, -0.6, r'2 rangs à droite : $e=-2$', r'$0{,}027=2{,}7\times10^{-2}$')
save(fig, '14-077')
