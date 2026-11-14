import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, d = 34, 22, 15
for m in range(3):
    for j in range(3):
        hl = (m == 1 and j == 2)
        disc(ax, x0 + j*d, y0 + m*d, 5.2, 'varie' if hl else 'sujet', label=r'$a^mz$' if hl else None, size='s')
    text(ax, 10, y0 + m*d, f'm = {m}', 'sujet', 's')
text(ax, 10, y0 + 3*d - 5, r'$a^m$ :', 'sujet', 'm')
brace(ax, x0-6, x0+2*d+6, y0-8, 'fixe', label='z : 3 du centre')
text(ax, 44, 67, r'3 $\times$ 3 = 9 éléments', 'resultat', 'l')
save(fig, '49-284')
