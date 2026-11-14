import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(52)
text(ax, 44, 47, r'multiplier par $\cos x$ en haut et en bas', 'varie', 's')
for y, a, b, na, nb, rb in ((26, r'$\frac{1}{\sin x}$', r'$\cot x$', '2 à 30°', r'$1{,}7321$', 'resultat'), (5, r'$\frac{1}{\cos x}$', '$1$', r'$1{,}1547$', '1', 'resultat')):
    lbox(ax, 4, y, 24, 14, 'sujet', a, size='l'); text(ax, 16, y - 2.5, na, 'sujet', 's')
    arrow(ax, (31, y + 7), (55, y + 7), 'varie'); text(ax, 43, y + 11, r'$\times\cos x$', 'varie', 's')
    lbox(ax, 58, y, 24, 14, rb, b, size='l'); text(ax, 70, y - 2.5, nb if y > 10 else '1', rb, 's')
save(fig, '31-135')
