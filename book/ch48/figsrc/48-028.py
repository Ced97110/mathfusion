import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 20, 68, r'$f(ab)$', 'sujet', 14); text(ax, 44, 68, '=', 'fixe', 14); text(ax, 68, 68, r'$f(a)f(b)$', 'autre', 14)
brace(ax, 6, 34, 60, 'sujet', label='combiner, puis f'); brace(ax, 52, 84, 60, 'autre', label='f, puis combiner')
text(ax, 20, 36, r'$f(3+6)=1$', 'sujet'); text(ax, 44, 36, '=', 'fixe', 'l'); text(ax, 68, 36, r'$f(3)+f(6)=1$', 'autre')
text(ax, 44, 20, 'pour a = 3 et b = 6', 'fixe', 's')
save(fig, '48-028')
