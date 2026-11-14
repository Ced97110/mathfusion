import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
names = [(r'$GL_n$', r'$O$'), (r'$SL_n$', r'$SO$'), (r'$C$', r'$\Omega$'), (r'$\{1\}$', r'$\{1\}$')]
conds = [('', ''), ('déterminant 1', 'déterminant 1'), ('commute avec tout', 'commutateurs'), ('', '')]
top0, band, inset = 66, 12, 3
text(ax, 44, 72, 'chaque groupe dans le précédent', 'fixe', 's') if False else text(ax, 44, 72.5, 'chacun dans le précédent', 'fixe', 's')
for t, cx, role in ((0, 22, 'sujet'), (1, 66, 'autre')):
    for i in range(4):
        w = 40 - 2 * inset * i
        top = top0 - band * i
        y = 3 + inset * i
        box(ax, cx - w / 2, y, w, top - y, role if i < 3 else 'fixe', fill=True, lw=0.9, r=1.2)
        if i < 3:
            text(ax, cx, top - 4.2, names[i][t], role, 'l')
            if conds[i][t]: text(ax, cx, top - 9.2, conds[i][t], 'varie', 's')
        else:
            text(ax, cx, (top + y) / 2, names[i][t], 'fixe', 'l')
save(fig, '73-145')
