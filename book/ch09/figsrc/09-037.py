import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
for cx, a, b, role, cap in [(20, '30', '2', 'sujet', '30 pour 2'), (68, '15', '1', 'resultat', '15 pour 1')]:
    text(ax, cx, 38, a, role, 'xl', weight='bold')
    line(ax, [(cx - 6, 31), (cx + 6, 31)], role, lw=1.2)
    text(ax, cx, 24, b, role, 'xl', weight='bold')
    text(ax, cx, 8, cap, role, 'm')
arrow(ax, (30, 38), (58, 38), 'varie')
arrow(ax, (30, 24), (58, 24), 'varie')
text(ax, 44, 42, r'$\div 2$', 'varie', 'm')
text(ax, 44, 28, r'$\div 2$', 'varie', 'm')
text(ax, 44, 50, 'même rapport', 'encre', 'l')
save(fig, '09-037')
