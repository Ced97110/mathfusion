import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 83, 'ce chapitre : cases 0 ou 1', 'sujet', 'm', weight='bold')
for i, c in enumerate('0011001'):
    box(ax, 16 + i * 8, 71, 7.2, 7, 'sujet' if c == '1' else 'fixe', label=c, size='m', r=0.4)
text(ax, 44, 63, 'même forme, autres cases', 'encre', 's')
arrow(ax, (44, 61.5), (44, 57.5), 'varie')
text(ax, 44, 52.5, r'Reed-Solomon (cyclique) : $\mathbb{F}_{256}$', 'autre', 's', weight='bold')
for i in range(7):
    box(ax, 16 + i * 8, 41, 7.2, 7, 'autre', label=rf'$a_{i + 1}$', size='s', r=0.4)
text(ax, 44, 36, r'$a_i$ : une des 256 valeurs de $\mathbb{F}_{256}$', 'autre', 's')
arrow(ax, (29, 34), (29, 27), 'varie')
arrow(ax, (59, 34), (59, 27), 'varie')
box(ax, 17, 15, 24, 11, 'resultat', label='QR codes', size='m')
box(ax, 47, 15, 24, 11, 'resultat', label='CD', size='m')
text(ax, 44, 6, 'à part : Reed-Muller (sonde Mariner)', 'fixe', 's')
save(fig, '68-221')
