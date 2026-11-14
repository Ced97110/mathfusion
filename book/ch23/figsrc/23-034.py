import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 6, 76, 14, -8, 8, step=1, labels=False, arrow_right=False)
text(ax, f(0), 9, '0', 'fixe', 's')
for v, lab in ((-7, '−7'), (7, '7')):
    disc(ax, f(v), 14, 1.8, 'resultat'); text(ax, f(v), 9, lab, 'resultat', 'm')
box(ax, 3, 32, 38, 10, 'resultat', label='(−7) × (−7) = 49')
box(ax, 47, 32, 38, 10, 'resultat', label='7 × 7 = 49')
arrow(ax, (22, 31), (f(-7), 17), 'resultat'); arrow(ax, (66, 31), (f(7), 17), 'resultat')
text(ax, 44, 48, 'deux nombres, même carré 49', 'sujet', 'm')
save(fig, '23-034')
