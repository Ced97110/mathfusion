import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 8, 72, 28, 1, 8, labels=False, arrow_right=False)
text(ax, 80, 28, 'dim.', 'fixe', 's')
for v, nm, role in [(1, r'$\mathbb{R}$', 'resultat'), (2, r'$\mathbb{C}$', 'resultat'), (3, None, 'limite'), (4, r'$\mathbb{H}$', 'resultat'), (8, r'$\mathbb{O}$', 'resultat')]:
    disc(ax, f(v), 40, 3.8, role, label=str(v))
    if nm: text(ax, f(v), 50, nm, role, 'l')
    line(ax, [(f(v), 36.2), (f(v), 29.2)], role, lw=0.8)
text(ax, f(3), 21, 'aucune algèbre à division', 'limite', 's')
text(ax, f(3), 16, 'réelle avec unité', 'limite', 's')
text(ax, f(3), 7, 'degré 3 : racine réelle', 'fixe', 's')
text(ax, f(3), 2.5, 'donc produit nul', 'fixe', 's')
save(fig, '78-158')
