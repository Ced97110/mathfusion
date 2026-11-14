import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
roles = ('fixe', 'autre', 'sujet'); names = ('tangente', 'sinus', 'cosinus')
tops = ('3 opposé', '3 opposé', '4 adjacent'); bots = ('4 adjacent', '5 hypoténuse', '5 hypoténuse'); vals = ('0,75', '0,6', '0,8')
box(ax, 34, 22, 48, 13, 'resultat', fill=False, dash=True, lw=1.0)
for i in range(3):
    x = 17 + 27 * i
    text(ax, x, 47, names[i], roles[i], 'l', weight='bold')
    text(ax, x, 40, tops[i], roles[i], 's')
    line(ax, [(x - 9, 36.5), (x + 9, 36.5)], roles[i], lw=1.0)
    text(ax, x, 29, bots[i], roles[i], 's')
    text(ax, x, 16, '= ' + vals[i], roles[i], 'm')
text(ax, 58, 6.5, 'même bas : l’hypoténuse 5', 'resultat', 's')
save(fig, '25-134')
