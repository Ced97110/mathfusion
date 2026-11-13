import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 17, 56, 'chiffres : précision', 'sujet', 's'); text(ax, 62, 56, r'$10^3$ : taille', 'varie', 's')
for y, d, wdt, res in ((38, '4', 12, '≈ 4 000'), (24, '4,3', 18, '≈ 4 300'), (10, '4,316', 28, '= 4 316')):
    x = 30 - wdt
    box(ax, x, y, wdt, 9, 'sujet', label=d, size='l')
    box(ax, 30, y, 22, 9, 'varie', label=r'$\times\,10^3$', size='l')
    text(ax, 56, y + 4.5, res, 'resultat', 'm', ha='left')
save(fig, '10-092')
