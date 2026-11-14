import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 22, 44, 44, 11, 'sujet', label=r'$x+4=6$', size='l')
text(ax, 44, 59, 'égalité + variable', 'sujet', 's')
for cx, x, calc, v, role, sign in [(23, '2', r'$2+4=6$', 'vrai', 'resultat', 0), (65, '5', r'$5+4=9\neq6$', 'faux', 'limite', 1)]:
    arrow(ax, (cx + (7 if not sign else -7), 43), (cx, 36), 'varie')
    text(ax, cx, 32, r'$x=' + x + r'$', 'varie', 'm')
    box(ax, cx - 17, 8, 34, 16, role)
    text(ax, cx, 18, calc, role, 'm'); text(ax, cx, 12, v, role, 'm', weight='bold')
save(fig, '12-139')
