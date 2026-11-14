import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 26, 56, r'$(a+bi)(c+di)$', 'sujet', 'm'); text(ax, 70, 56, r'$(a,b)(c,d)$', 'autre', 'm')
text(ax, 26, 50, r'$i^2=-1$', 'sujet', 's'); text(ax, 70, 50, r'$c=-1$', 'autre', 's')
for y, lab, f_ in [(30, '1er nombre', r'$ac-bd$'), (10, '2e nombre', r'$ad+bc$')]:
    box(ax, 4, y, 40, 11, 'sujet', label=f_, size='l')
    text(ax, 48, y + 5.5, r'$=$', 'resultat', 'xl')
    box(ax, 52, y, 34, 11, 'autre', label=f_, size='l')
    text(ax, 24, y + 15, lab, 'fixe', 's')
save(fig, '78-110')
