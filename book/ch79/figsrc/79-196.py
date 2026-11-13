import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'la partie $Y$', 'sujet', 'm')
ys = [(13, 2), (34, 3), (54, 4), (75, 6)]
for cx, n in ys:
    box(ax, cx - 8, 48, 16, 12, 'sujet', label=str(n), size='l')
for xc, n, role, t in [(15, 2, 'limite', '2 ne divise\npas 3'), (44, 3, 'limite', '3 ne divise\npas 2'), (73, 1, 'resultat', '1 divise\n2, 3, 4 et 6')]:
    box(ax, xc - 10, 25, 20, 12, role, label=str(n), size='l', lw=1.8 if n == 1 else 0.8)
    text(ax, xc, 17, t, role, 's')
for cx, n in ys:
    arrow(ax, (73, 37.5), (cx, 47.5), 'resultat', lw=0.9)
text(ax, 44, 5, r'$\inf Y=1=\mathrm{PGCD}(2,3,4,6)$', 'resultat', 'm')
save(fig, '79-196')
