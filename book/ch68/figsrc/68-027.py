import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
pitch = 1.272 * 11 * 25.4 / 72
xc = 50
text(ax, 44, 53, 'ajouter e inverse les bits où e vaut 1', 'encre', 'm')
bx = xc + pitch
poly(ax, [(bx - 2.5, 12), (bx + 2.5, 12), (bx + 2.5, 49), (bx - 2.5, 49)], 'varie')
sp = lambda w: '  '.join(w)
text(ax, xc, 42, sp('0011001'), 'sujet', 'xl')
text(ax, xc, 30, sp('0000100'), 'varie', 'xl')
line(ax, [(30, 24), (70, 24)], 'fixe')
text(ax, xc, 17, sp('0011101'), 'autre', 'xl')
text(ax, 6, 42, r'$c$ envoyé', 'sujet', 'm', ha='left')
text(ax, 6, 30, r'$+\ e$ erreur', 'varie', 'm', ha='left')
text(ax, 6, 17, r'$r$ reçu', 'autre', 'm', ha='left')
text(ax, bx, 6, 'bit 5 : 0 devient 1', 'varie', 's')
save(fig, '68-027')
