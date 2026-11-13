import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 2, 70, 28, 11, 'sujet', label=r'$P \subseteq N(P)$', size='s')
box(ax, 58, 70, 28, 11, 'resultat', label=r'$n_p$ divise $q$', size='s')
arrow(ax, (31, 75.5), (57, 75.5), 'varie', lw=1.4)
text(ax, 44, 79.5, 'étape clé', 'varie', 's', weight='bold')
text(ax, 44, 71.5, 'en dessous', 'varie', 's')
u = 7; x0 = 30
# (label, segments of size, count text, role colours)
rows = [(54, r'$[G:N(P)]$', [6], '1'), (40, r'$[N(P):P]$', [3, 3], '2'), (26, r'$[G:P]$', [3, 3], r'$2 = q$')]
for y, lab, segs, cnt in rows:
    text(ax, 27, y + 4, lab, 'encre', 's', ha='right')
    x = x0
    for k, sgl in enumerate(segs):
        role = 'sujet' if (len(segs) == 1) else ('autre' if k == 0 else 'fixe')
        if y == 54: role = 'sujet'
        for c in range(sgl):
            box(ax, x + c * u, y, u, 8, role, r=0.3, lw=0.6)
        x += sgl * u
    text(ax, x0 + 6 * u + 3, y + 4, cnt, 'resultat' if y == 26 else 'encre', 'm', ha='left', weight='bold')
text(ax, 2, 60, 'combien de copies :', 'fixe', 's', ha='left') if False else None
text(ax, 44, 12, r'$2 = 1 \times 2$', 'resultat', 'l', weight='bold')
text(ax, 44, 5, '$[G:P] = [G:N(P)] \\times [N(P):P]$', 'sujet', 's')
save(fig, '50-071')
