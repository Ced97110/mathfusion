import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
cols = [(20, 'sujet', r'$A$', 'on part de A'), (44, 'varie', r'$\setminus$', 'on retire'), (68, 'autre', r'$B$', "l'ensemble retiré")]
for cx, role, sym, lab in cols:
    box(ax, cx - 8, 28, 16, 12, role, label=sym, size='l', lw=1.0)
    arrow(ax, (cx, 28), (cx, 23), role)
    text(ax, cx, 19, lab, role, 's')
text(ax, 44, 7, 'se lit « A privé de B »', 'encre', 'm')
save(fig, '42-133')
