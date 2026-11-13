import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def grid(x0, n, y0=22, d=7.5):
    for i in range(n):
        for j in range(n):
            disc(ax, x0 + i*d, y0 + j*d, 2.7, 'sujet')
grid(18, 2); grid(58.5, 3)
box(ax, 10, 14, 17, 25, 'sujet', fill=False, dash=True) if False else None
text(ax, 22, 52, r'$p=2$', 'sujet', 'l')
text(ax, 66, 52, r'$p=3$', 'sujet', 'l')
text(ax, 22, 44, r'4 = 2 $\times$ 2', 'sujet', 'm')
text(ax, 66, 44, r'9 = 3 $\times$ 3', 'sujet', 'm')
box(ax, 5, 5, 34, 9, 'resultat', label='commutatif')
box(ax, 49, 5, 34, 9, 'resultat', label='commutatif')
text(ax, 44, 60, r'ordre $p^2$', 'sujet', 'l')
save(fig, '49-280')
