import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
side, gap = 6.0, 0.3
x0 = (88 - (13 * side + 12 * gap)) / 2
text(ax, 44, 40, '13 blocs de 12 : 156', 'sujet', 'm')
for k in range(13):
    role = 'sujet' if k < 10 else 'varie'
    ax.add_patch(Rectangle((x0 + k * (side + gap), 24), side, side, ec=COL[role], fc=FILL[role], lw=0.7, zorder=2))
brace(ax, x0, x0 + 10 * side + 9 * gap, 22, 'sujet', label=r'$10\times12=120$')
brace(ax, x0 + 10 * (side + gap), x0 + 13 * side + 12 * gap, 22, 'varie', label=r'$3\times12=36$')
text(ax, 44, 5, r'$156=12\times13+0$ : reste 0', 'resultat', 'm')
save(fig, '54-143')
