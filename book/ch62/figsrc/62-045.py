import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 18, 84, r'$F$ = restes mod. 5', 'sujet', 's')
text(ax, 70, 84, r'$F^p$ : puissances 5', 'resultat', 's')
for i in range(5):
    y = 72 - i * 10
    disc(ax, 18, y, 3.6, 'sujet', label=str(i), size='m')
    disc(ax, 70, y, 3.6, 'resultat', label=str(i), size='m')
    arrow(ax, (23, y), (65, y), 'varie')
text(ax, 44, 27, r'$x\mapsto x^5$', 'varie', 'm')
text(ax, 44, 13, '2⁵ = 32 → reste 2\n3⁵ = 243 → reste 3\n4⁵ = 1 024 → reste 4', 'encre', 's')
save(fig, '62-045')
