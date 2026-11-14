import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 14, 58, 60, 12, 'sujet', label=r'automorphismes de $E/\mathbb{Q}$', size='s')
mids = [r'$r\mapsto r$', r'$r\mapsto jr$', r'$r\mapsto j^2r$']
cs = [16, 44, 72]
for c, m in zip(cs, mids):
    line(ax, [(44, 57.5), (c, 47)], 'fixe')
    box(ax, c - 13, 34, 26, 12, 'autre', label=m, size='s')
    for dx, lab in ((-7, r'$j\mapsto j$'), (7, r'$j\mapsto j^2$')):
        line(ax, [(c, 33.5), (c + dx, 23)], 'fixe')
        box(ax, c + dx - 7, 12, 14, 11, 'resultat', label=lab, size='s')
text(ax, 44, 4, r'$3\times2=6=[E:\mathbb{Q}]$', 'resultat', 'm')
save(fig, '63-094')
