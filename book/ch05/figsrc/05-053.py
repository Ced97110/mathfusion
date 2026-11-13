import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, 'on teste 47 avec 2, 3, 5, 7', 'encre', 'm')
tests = [(2, '47 est impair'), (3, r'$4 + 7 = 11$, hors table de 3'),
         (5, 'finit par 7, ni 0 ni 5'), (7, r'$47 = 7 \times 6 + 5$, reste 5')]
for k, (d, s) in enumerate(tests):
    y = 58 - k * 12
    box(ax, 4, y - 4.5, 10, 9, 'varie', label=str(d), size='l')
    arrow(ax, (14.6, y), (18.4, y), 'varie', lw=0.8)
    text(ax, 20, y, s, 'encre', 's', ha='left')
    xc = 83
    line(ax, [(xc - 1.8, y - 1.8), (xc + 1.8, y + 1.8)], 'limite', lw=1.3)
    line(ax, [(xc - 1.8, y + 1.8), (xc + 1.8, y - 1.8)], 'limite', lw=1.3)
text(ax, 44, 15.5, r'quotient $6 < 7$ : on arrête', 'varie', 'm')
box(ax, 18, 2, 52, 9, 'resultat', label='aucun ne divise : 47 est premier', size='s')
text(ax, 77, 65, 'ne divise pas', 'limite', 's')
save(fig, '05-053')
