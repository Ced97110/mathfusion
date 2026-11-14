import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
poly(ax, [(2, 10), (30, 10), (30, 52), (2, 52)], 'sujet', fill=False, lw=1.1)
poly(ax, [(58, 10), (86, 10), (86, 52), (58, 52)], 'autre', fill=False, lw=1.1)
text(ax, 16, 58, r'$C$', 'sujet', 'l')
text(ax, 72, 58, r'$e+C$', 'autre', 'l')
for y, a, b in [(36, '000', '100'), (16, '111', '011')]:
    box(ax, 6, y, 20, 9, 'sujet', label=a)
    box(ax, 62, y, 20, 9, 'autre', label=b)
    arrow(ax, (27, y + 4.5), (61, y + 4.5), 'varie')
text(ax, 44, 30.5, r'$+\ 100$', 'varie', 'm')
save(fig, '68-078')
