import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$\eta(\sqrt{2})^2=2$ : seulement ici', 'encre', 'm')
f = numberline(ax, 14, 74, 22, -2, 2, 1, arrow_right=False)
r2 = math.sqrt(2)
disc(ax, 44, 52, 4.5, 'sujet', label=r'$\sqrt{2}$')
for v, lab in [(-r2, r'$-\sqrt{2}$'), (r2, r'$\sqrt{2}$')]:
    disc(ax, f(v), 22, 2.0, 'resultat')
    text(ax, f(v), 29, lab, 'resultat', 'm')
    arrow(ax, (44 + (f(v) - 44) * 0.2, 47.5), (f(v), 33), 'varie')
text(ax, 44, 8, 'ailleurs, le carré n’est pas 2', 'fixe', 's')
save(fig, '63-053')
