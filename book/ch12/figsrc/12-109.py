import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
for i in range(6): box(ax, 8 + 12 * i, 20, 12, 10, 'sujet', label='1/6', r=0.5)
brace(ax, 8, 80, 30.5, 'fixe', 'le tout : 1', down=False)
brace(ax, 8, 80, 19.5, 'resultat', '6 · 1/6 = 1', down=True, size='m')
save(fig, '12-109')
