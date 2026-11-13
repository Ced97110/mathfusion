import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 14, 48, r'$\mathbb{Z}$', 'sujet', 22)
text(ax, 54, 48, 'tous les entiers relatifs', 'sujet', 'm')
yl = 24
f = numberline(ax, 6, 76, yl, -4, 6, 1, labels=False)
for v in range(-4, 7):
    disc(ax, f(v), yl, 1.3, 'sujet')
for v in (-3, 0, 5):
    text(ax, f(v), yl + 5, f'{v}'.replace('-', '−'), 'sujet', 'm', weight='bold')
disc(ax, f(0.5), yl, 1.1, 'limite', fill=False, lw=1.0)
text(ax, f(0.5), 38, r'$\frac{1}{2}$ : pas un entier', 'limite', 's')
arrow(ax, (f(0.5), 35.3), (f(0.5), yl + 2.2), 'limite')
brace(ax, f(-4), f(-1), yl - 2.2, 'sujet', 'négatifs')
brace(ax, f(1), f(6), yl - 2.2, 'sujet', 'positifs')
save(fig, '05-178')
