import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [(r'$\nu(ab)$', 'sujet', 'départ'), (r'$abK$', 'fixe', ''), (r'$(aK)(bK)$', 'varie', ''), (r'$\nu(a)\,\nu(b)$', 'resultat', 'arrivée')]
labs = [r'définition de $\nu$', 'produit des classes\n(étape clé)', r'définition de $\nu$']
ys = [70, 48, 26, 4]
for (s, role, tag), y in zip(rows, ys):
    box(ax, 6, y, 36, 10, role, label=s, size='m')
    if tag: text(ax, 50, y + 5, tag, role, 's', ha='left')
for i in range(3):
    y0 = ys[i]; y1 = ys[i + 1] + 10
    arrow(ax, (24, y0 - 0.5), (24, y1 + 0.5), 'fixe' if i != 1 else 'varie', lw=1.2 if i == 1 else 1.0)
    text(ax, 30, (y0 + y1) / 2, labs[i], 'varie' if i == 1 else 'fixe', 's', ha='left', weight='bold' if i == 1 else 'normal')
save(fig, '48-085')
