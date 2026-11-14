import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for k, (cx, role, pos) in enumerate([(4, 'sujet', (0.65, 0.5)), (48, 'autre', (0.35, 0.7))]):
    box(ax, cx, 14, 36, 40, 'fixe', r=1.0)
    ax0, ay0 = cx+6, 22
    arrow(ax, (ax0, ay0), (ax0+27, ay0), 'fixe', lw=0.8); arrow(ax, (ax0, ay0), (ax0, ay0+27), 'fixe', lw=0.8)
    px, py = ax0 + pos[0]*25, ay0 + pos[1]*25
    line(ax, [(px, ay0), (px, py)], role, dash=True); line(ax, [(ax0, py), (px, py)], role, dash=True)
    disc(ax, px, py, 1.8, role)
    text(ax, cx+18, 18, 'position', 'varie', 's')
    text(ax, ax0-1.5, ay0+14, 'vitesse × masse', 'varie', 's', rot=90)
    text(ax, cx+6, 50, r'$P_%d$' % (k+1), role, 'm')
    text(ax, cx+18, 59, 'bille %d' % (k+1), role, 's')
text(ax, 44, 34, '+', 'encre', 'l')
brace(ax, 4, 84, 11, 'resultat', label='espace symplectique', depth=1.8)
save(fig, '75-184')
