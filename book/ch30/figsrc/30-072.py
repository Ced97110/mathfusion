import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for xc, tit, num, nr, res in ((22, 'sécante', '1', 'varie', '= 2'), (66, 'tangente', 'sin = 0,866', 'autre', '= 1,732')):
    text(ax, xc, 60, tit, 'encre', 'm', weight='bold')
    box(ax, xc - 14, 44, 28, 9, nr, label=num)
    line(ax, [(xc - 14, 40.5), (xc + 14, 40.5)], 'encre', lw=1.4)
    box(ax, xc - 14, 27, 28, 9, 'sujet', label='cos = 0,5')
    text(ax, xc, 19, res, 'resultat', 'l')
text(ax, 44, 8, 'même dénominateur', 'fixe', 's')
save(fig, '30-072')
