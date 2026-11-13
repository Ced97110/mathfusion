import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$a=12,\ b=20$', 'encre', 'm')
text(ax, 44, 71, r'$d$ : nombre de marches depuis 1', 'fixe', 's')
def row(y, l, r, res, role_l, role_r):
    box(ax, 4, y, 24, 12, role_l, label=l); text(ax, 31, y + 6, '+', 'encre', 'l')
    box(ax, 34, y, 24, 12, role_r, label=r); box(ax, 62, y, 22, 12, 'resultat', label=res)
row(50, r'$d(60)=4$', r'$d(4)=2$', r'$=6$', 'fixe', 'fixe')
row(24, r'$d(12)=3$', r'$d(20)=3$', r'$=6$', 'sujet', 'autre')
text(ax, 44, 42, '=', 'resultat', 'xl', weight='bold')
text(ax, 44, 9, 'un exemple, pas une preuve', 'encre', 'm', weight='bold')
save(fig, '79-187')
