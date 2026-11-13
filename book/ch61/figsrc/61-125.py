import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ys = [6, 32, 58]; labs = ['$F$', '$K$', '$E$']; rl = ['fixe', 'sujet', 'sujet']
for y, l, r in zip(ys, labs, rl): box(ax, 6, y, 16, 13, r, label=l, size='l')
text(ax, 38, 72, 'on suppose', 'varie', 'm', weight='bold')
text(ax, 72, 72, 'on conclut', 'resultat', 'm', weight='bold')
for i, t in enumerate([r'$K$ algébrique sur $F$', r'$E$ algébrique sur $K$']):
    arrow(ax, (14, ys[i] + 14), (14, ys[i + 1] - 1), 'varie', lw=1.2)
    text(ax, 26, ys[i] + 20, t, 'varie', 's', ha='left')
line(ax, [(24, ys[0] + 6.5), (66, ys[0] + 6.5)], 'resultat', lw=0.8, dash=True)
line(ax, [(24, ys[2] + 6.5), (66, ys[2] + 6.5)], 'resultat', lw=0.8, dash=True)
arrow(ax, (66, ys[0] + 6.5), (66, ys[2] + 6.5), 'resultat', lw=1.6)
text(ax, 68, 39, r'$E$ algébrique' + '\nsur $F$', 'resultat', 's', ha='left')
save(fig, '61-125')
