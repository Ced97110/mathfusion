import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 24, 58, r'$\frac{a}{b}$', 'sujet', 'xl')
text(ax, 44, 58, '=', 'fixe', 'l')
text(ax, 64, 58, r'$\frac{c}{d}$', 'fixe', 'xl')
text(ax, 24, 47, 'le premier rapport', 'sujet', 's', weight='bold')
for cx, lab in [(15, r'$\frac{3}{4}$'), (44, r'$\frac{6}{8}$'), (73, 'tout autre')]:
    arrow(ax, (24, 43.5), (cx, 31), 'varie')
    box(ax, cx - 13, 10, 26, 20, 'sujet', label=lab, size='xl' if cx != 73 else 's')
save(fig, '09-046')
