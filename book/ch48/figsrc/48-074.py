import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, "même paquet ⇔ même position", 'encre', 's')
for x, role, lab, vals, pos in [(4, 'sujet', r"paquet $1K$", ['1', '5', '9'], '1'), (48, 'autre', r"paquet $2K$", ['2', '6', '10'], '2')]:
    box(ax, x, 30, 36, 22, role)
    text(ax, x + 18, 47, lab, role, 's')
    for i, v in enumerate(vals):
        disc(ax, x + 7 + 11 * i, 37, 3.6, role, label=v, size='s')
        arrow(ax, (x + 7 + 11 * i, 33.4), (x + 18 + (i - 1) * 3, 15.5), 'varie', lw=0.8)
    disc(ax, x + 18, 11, 4, 'resultat', label=pos, size='s')
text(ax, 22, 3, "position 1", 'resultat', 's'); text(ax, 66, 3, "position 2", 'resultat', 's')
save(fig, '48-074')
