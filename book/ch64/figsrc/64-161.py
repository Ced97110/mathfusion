import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
r5 = 5 ** 0.5
c1, c2 = (3 - r5) / 2, (3 + r5) / 2   # racines : somme 3, produit 1
text(ax, 44, 56, r'$c+c^\prime=3$ et $c\times c^\prime=1$', 'encre', 'm')
f = numberline(ax, 8, 64, 38, 0, 3, arrow_right=False)
for v, lab in ((c1, r'$c^\prime$'), (c2, '$c$')):
    disc(ax, f(v), 38, 1.6, 'sujet')
    text(ax, f(v), 44, lab, 'sujet', 'm')
brace(ax, f(c1), f(c2), 30, 'sujet', label=r'$c-c^\prime=\sqrt{5}$', down=True)
box(ax, 3, 4, 40, 11, 'sujet', label=r'$(c-c^\prime)^2=9-4=5$')
box(ax, 48, 4, 37, 11, 'resultat', label=r'$b^2-4q=\Delta=5$')
arrow(ax, (44, 9.5), (47.5, 9.5), 'varie')
save(fig, '64-161')
