import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
# A. infini
text(ax, 44, 91, 'infini : chacune se défait', 'varie', 'm')
for i, lab in enumerate([r'$\times 2$', r'$\times 3$', r'$\times 4$', '…']):
    x = 6 + i * 20.5
    box(ax, x, 72, 16, 10, 'varie' if i < 3 else 'fixe', label=lab, dash=(i == 3))
    if i < 3: arrow(ax, (x + 16.3, 77), (x + 20.2, 77), 'fixe', lw=0.8)
# B. non abélien
text(ax, 44, 64, 'non abélien', 'autre', 'm')
box(ax, 4, 44, 30, 10, 'sujet', label='r puis s')
box(ax, 54, 44, 30, 10, 'autre', label='s puis r')
text(ax, 44, 49, r'$\neq$', 'encre', 'l')
# C. contient D4
box(ax, 3, 3, 82, 34, 'sujet', fill=False, lw=1.2)
text(ax, 17, 22, r'$GL_2(\mathbb{R})$', 'sujet', 'l')
box(ax, 30, 6, 52, 28, 'resultat', dash=True)
text(ax, 56, 28, '8 symétries du carré', 'resultat', 's')
for i in range(8):
    disc(ax, 36.5 + i * 5.6, 15, 2.1, 'resultat')
save(fig, '44-191')
