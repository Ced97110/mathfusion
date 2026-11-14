import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'$F=\mathbb{Q}\subset K=\mathbb{Q}(j)$', 'encre', 'm')
box(ax, 4, 6, 80, 52, 'sujet', label=None)
text(ax, 44, 52, r'Gal($f$ sur $F$) : 6 éléments', 'sujet', 'm')
box(ax, 7, 12, 42, 30, 'autre', fill=False, lw=1.2)
text(ax, 28, 36, r'Gal($f$ sur $K$) : 3', 'autre', 'm')
for x in (14, 28, 42):
    disc(ax, x, 22, 3, 'autre')
for x in (60, 70, 79):
    disc(ax, x, 22, 3, 'sujet')
text(ax, 69, 33, 'en plus : 3', 'sujet', 's')
save(fig, '64-162')
