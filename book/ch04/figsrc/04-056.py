import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# lecture du haut : 2 + 3 × 4 sans parenthèses
text(ax, 36, 79, '2 + 3 × 4', 'encre', 'l', weight='bold')
for x in (14, 18):
    box(ax, x, 56, 4, 4, 'sujet', r=0.3)
text(ax, 18, 52, '2 seuls', 'sujet', 's')
text(ax, 26, 64, '+', 'encre', 'l')
for c in range(3):
    for rr in range(4):
        box(ax, 30 + 4 * c, 56 + 4 * rr, 4, 4, 'varie', r=0.3)
text(ax, 36, 52, '3 × 4 = 12', 'varie', 's')
text(ax, 68, 64, '14 carreaux', 'resultat', 'm', weight='bold')
line(ax, [(4, 47), (84, 47)], 'fixe', dash=True)
# lecture du bas : (2 + 3) × 4 avec parenthèses
text(ax, 36, 40, '(2 + 3) × 4', 'encre', 'l')
for c in range(5):
    role = 'sujet' if c < 2 else 'varie'
    for rr in range(4):
        box(ax, 26 + 4 * c, 14 + 4 * rr, 4, 4, role, r=0.3)
text(ax, 23, 22, '4', 'fixe', 's')
box(ax, 26, 14, 20, 16, 'resultat', fill=False, lw=1.6, r=0.3)
brace(ax, 26, 46, 12, 'varie', label='5 de large', down=True, size='s')
text(ax, 68, 22, '20 carreaux', 'resultat', 'm', weight='bold')
save(fig, '04-056')
