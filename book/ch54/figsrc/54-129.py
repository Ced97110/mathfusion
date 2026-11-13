import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$\deg(0\cdot x)$', 'sujet', 's')
text(ax, 70, 55, r'$\deg 0+\deg x$', 'autre', 's')
rows = [(41, '0', r'$0$', r'$0+1=1$', 'limite', r'$\neq$'),
        (26, r'$-1$', r'$-1$', r'$-1+1=0$', 'limite', r'$\neq$'),
        (11, r'$-\infty$', r'$-\infty$', r'$-\infty+1=-\infty$', 'resultat', '=')]
for y, ch, lhs, rhs, role, sign in rows:
    box(ax, 3, y - 5, 22, 10, role, label='choix ' + ch, size='s')
    text(ax, 40, y, lhs, 'sujet', 'm')
    text(ax, 50, y, sign, role, 'l', weight='bold')
    text(ax, 70, y, rhs, 'autre', 'm')
save(fig, '54-129')
