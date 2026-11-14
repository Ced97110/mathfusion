import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# trois solutions sur une droite
f = numberline(ax, 8, 70, 52, -2, 2, step=1, labels=False, arrow_right=False)
for v in (1.53, 0.35, -1.88):
    disc(ax, f(v), 52, 1.6, 'sujet')
    text(ax, f(v), 46.5, f'{v:g}'.replace('.', ',').replace('-', '−'), 'sujet', 's')
text(ax, 44, 59, 'les trois solutions connues', 'sujet', 's')
# chaîne : solutions -> groupe -> radicaux
bw, bh, gap, y = 22, 14, 8, 14
x0 = 2
labs = [('solutions', 'sujet', False), ('groupe de\nGalois ?', 'varie', True), ('résoluble ?\npar radicaux', 'fixe', False)]
for i, (lab, role, dash) in enumerate(labs):
    box(ax, x0 + i * (bw + gap), y, bw, bh, role, label=lab, size='s', dash=dash)
arrow(ax, (x0 + bw, y + bh / 2), (x0 + bw + gap, y + bh / 2), 'varie')
arrow(ax, (x0 + 2 * bw + gap, y + bh / 2), (x0 + 2 * bw + 2 * gap, y + bh / 2), 'resultat')
text(ax, x0 + bw + gap / 2, y - 3.5, 'comment ?', 'varie', 's')
text(ax, x0 + 2 * bw + 1.5 * gap, y - 3.5, 'critère', 'resultat', 's')
arrow(ax, (x0 + bw / 2, 40), (x0 + bw / 2, y + bh + 1), 'fixe')
save(fig, '65-001')
