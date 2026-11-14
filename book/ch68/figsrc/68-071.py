import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
rows = [('répétition triple', 3), ('parité sur 4 bits', 2), ('code de Judson (4 mots)', 3)]
sq, g, x0 = 5, 1.2, 46
for r, (name, d) in enumerate(rows):
    yc = 40 - r * 14
    text(ax, 2, yc, name, 'fixe', 'm', ha='left')
    for i in range(d):
        x = x0 + i * (sq + g)
        poly(ax, [(x, yc - sq / 2), (x + sq, yc - sq / 2), (x + sq, yc + sq / 2), (x, yc + sq / 2)], 'sujet')
    text(ax, 74, yc, rf'$d={d}$', 'sujet', 'l', ha='left')
save(fig, '68-071')
