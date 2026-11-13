import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 21, 61, 'mantisse', 'sujet', 'l', weight='bold')
text(ax, 21, 55.5, 'les chiffres', 'sujet', 's')
text(ax, 68, 61, 'puissance de 10', 'autre', 'm')
for y, e in [(36, 7), (10, 8)]:
    box(ax, 4, y, 34, 12, 'sujet', label='2,9', size='l')
    text(ax, 45, y + 6, '×', 'encre', 'l')
    box(ax, 52, y, 32, 12, 'autre', label=rf'$10^{{{e}}}$', size='l')
text(ax, 21, 29, 'ne change pas', 'sujet', 's')
text(ax, 21, 25, 'ne change pas', 'sujet', 's') if False else None
arrow(ax, (21, 33), (21, 24), 'sujet', lw=0.0001) if False else None
line(ax, [(21, 34.5), (21, 30.8)], 'sujet', lw=0.9)
line(ax, [(21, 27.2), (21, 23.5)], 'sujet', lw=0.9)
arrow(ax, (68, 35), (68, 24), 'varie', lw=1.3)
text(ax, 77, 29.5, 'change', 'varie', 's', ha='center')
save(fig, '14-072')
