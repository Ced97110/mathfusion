import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [16, 44, 72]
text(ax, 16, 65, 'départ', 'encre', 's', weight='bold')
text(ax, 44, 65, 'règle 1 : x − 2y', 'sujet', 's', weight='bold')
text(ax, 72, 65, 'règle 2 : tripler', 'autre', 's', weight='bold')
rows = [(48, [r'$(1\,;\,4)$', '−7', '−21'], 'sujet'), (16, [r'$(3\,;\,12)$', '−21', '−63'], 'resultat')]
for y, vals, role in rows:
    for x, v in zip(xs, vals):
        box(ax, x - 11, y - 6, 22, 12, role, label=v, size='s')
    arrow(ax, (xs[0] + 11.5, y), (xs[1] - 11.5, y), 'sujet', lw=1.2)
    arrow(ax, (xs[1] + 11.5, y), (xs[2] - 11.5, y), 'autre', lw=1.2)
for x in xs:
    arrow(ax, (x, 41.5), (x, 22.5), 'varie', lw=1.3)
    text(ax, x + 2, 32, r'$\times 3$', 'varie', 's', ha='left')
text(ax, 44, 5, 'même résultat dans les deux ordres : −63 = 3 × (−21)', 'resultat', 's')
save(fig, '57-175')
