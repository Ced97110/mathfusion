import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(66)
S, P = 6.0, 6.8

def row(y, n, title, ctrl):
    text(ax, 3, y + 11, title, 'encre', 'm', ha='left', weight='bold')
    for i in range(n):
        role = 'sujet' if i < 4 else 'varie'
        ax.add_patch(Rectangle((3 + i * P, y - S / 2), S, S, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    brace(ax, 3, 3 + 3 * P + S, y - 3.4, 'sujet', label='4 utiles', depth=1.6)
    brace(ax, 3 + 4 * P, 3 + (n - 1) * P + S, y - 3.4, 'varie', label=ctrl, depth=1.6)

row(46, 12, 'répétition triple : 12 bits', '8 de contrôle')
row(20, 7, 'Hamming : 7 bits', '3 de contrôle')
box(ax, 14, 2, 60, 7, 'resultat', label='les deux corrigent 1 erreur')
crop(fig, ax, 0.0, 61.4)
save(fig, '68-130')
