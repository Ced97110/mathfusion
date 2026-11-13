import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 34, 36, 20, 12, 'sujet', label=r'$a$', size='xl')
text(ax, 44, 53, 'un nombre quelconque', 'sujet', 's')
for c, t in ((16, '3'), (44, '12'), (72, '100')):
    box(ax, c - 9, 10, 18, 10, 'varie', label=t, size='l')
    arrow(ax, (44 + (c - 44) * 0.3, 35.5), (c, 21), 'varie')
text(ax, 44, 4, r'on remplace $a$ par un nombre', 'varie', 's')
save(fig, '13-032')
