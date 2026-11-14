import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 42, r'somme répétée : $3\cdot 2$', 'sujet', 'm')
text(ax, 44, 22, r'produit répété : $2\times 2\times 2$', 'autre', 'm')
for row, (yb, role, sign, res) in enumerate([(29, 'sujet', '+', r'$=6=2$'), (9, 'autre', r'$\times$', r'$=8=0$')]):
    xs = [4 + 18 * i for i in range(3)]
    for x in xs:
        box(ax, x, yb, 12, 9, role, label='2', size='l')
    for x in xs[:2]:
        text(ax, x + 15, yb + 4.5, sign, role, 'l')
    text(ax, 68, yb + 4.5, res, 'resultat' if row == 0 else 'autre', 'l')
save(fig, '51-129')
