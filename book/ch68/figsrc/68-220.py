import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, 'une porte « ou exclusif »', 'encre', 'm', weight='bold')
for ym, a, b, out in ((34, '1', '0', '1'), (12, '1', '1', '0')):
    text(ax, 5, ym + 4, a, 'sujet', 'l', weight='bold')
    text(ax, 5, ym - 4, b, 'sujet', 'l', weight='bold')
    arrow(ax, (9, ym + 4), (22, ym + 2), 'fixe')
    arrow(ax, (9, ym - 4), (22, ym - 2), 'fixe')
    box(ax, 22, ym - 6, 26, 12, 'varie', label='ou exclusif', size='s')
    arrow(ax, (48.5, ym), (58, ym), 'fixe')
    text(ax, 63, ym, out, 'resultat', 'l', weight='bold')
    text(ax, 78, ym, f'{a} + {b} = {out}', 'resultat', 's')
save(fig, '68-220')
