import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = [(60, r'$(4x^2+2x-8)+(3x^2-7x-10)$', '1. écrire la somme', 'sujet'),
        (40, r'$4x^2+2x-8+3x^2-7x-10$', '2. enlever les parenthèses', 'varie'),
        (20, r'$7x^2-5x-18$', '3. regrouper', 'resultat')]
for y, s, lab, r in rows:
    box(ax, 8, y - 5, 72, 10, r, label=s, size='m')
    text(ax, 44, y + 7, lab, 'encre', 's')
for y in (55, 35): arrow(ax, (44, y - 0.2 - 0), (44, y - 1.0 - 0.0), 'varie') if False else None
arrow(ax, (44, 50.2), (44, 47.5), 'varie'); arrow(ax, (44, 30.2), (44, 27.5), 'varie')
text(ax, 44, 7, r'pour $x=1$ : $-2+(-14)=-16$ et $-16$', 'resultat', 's')
save(fig, '15-114')
