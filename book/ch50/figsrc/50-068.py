import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$G$ : 6 éléments', 'fixe', 'm', weight='bold')
cw = 11; gap = 1.2; x0 = 44 - (6 * cw + 5 * gap) / 2
for i in range(6):
    box(ax, x0 + i * (cw + gap), 62, cw, 10, 'sujet' if i < 2 else 'fixe')
for g in range(3):
    xa = x0 + 2 * g * (cw + gap); xb = xa + 2 * cw + gap
    brace(ax, xa, xb, 61, 'sujet' if g == 0 else 'fixe', down=True, depth=1.6)
text(ax, x0 + cw + gap / 2, 53.5, r'$N(P)$ : 2', 'sujet', 's')
text(ax, 44 + (x0 + 3 * (cw + gap) - 44) + 0, 53.5, '2', 'fixe', 's')
text(ax, x0 + 5 * (cw + gap), 53.5, '2', 'fixe', 's')
bx = [x0 + 2 * g * (cw + gap) + cw + gap / 2 for g in range(3)]
for g, xc in enumerate(bx):
    arrow(ax, (xc, 49), (xc, 36), 'varie', lw=1.2)
    box(ax, xc - 11, 20, 22, 14, 'sujet' if g == 0 else 'autre')
labs = [r'$P$', r'$P\,'+"'"+'$', r'$P\,'+"''"+'$']
for xc, l, g in zip(bx, labs, range(3)):
    text(ax, xc, 27, l, 'sujet' if g == 0 else 'autre', 'm')
text(ax, 44, 14, 'chaque paire donne un conjugué', 'varie', 's')
text(ax, 44, 6, r'orbite : $6 / 2 = 3$ éléments', 'resultat', 'm', weight='bold')
save(fig, '50-068')
