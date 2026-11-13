import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 17, 62, 'ℤ/7ℤ', 'sujet', 'l')
text(ax, 71, 62, 'ℚ[x]/(x²−2)', 'autre', 'l')
rows = [(48, 'restes', '0, 1, …, 6', r'$a+bx$'), (28, 'règle', r'$7=0$', r'$x^2=2$'), (8, 'racine', r'$7=0$', r'$x^2=2$')]
for y, lab, l, r in rows[:2]:
    box(ax, 2, y - 6, 30, 12, 'sujet', label=l)
    box(ax, 56, y - 6, 30, 12, 'autre', label=r)
    arrow(ax, (33, y), (55, y), 'resultat', both=True)
    text(ax, 44, y + 3.5, lab, 'resultat', 's')
text(ax, 44, 9, r'le reste $x$ vérifie la règle : racine', 'autre', 's')
save(fig, '62-048')
