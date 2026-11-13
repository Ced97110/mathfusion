import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cols = ['naturels', 'relatifs', 'rationnels', 'irrationnels', 'réels']
rows = [('3', [1,1,1,0,1]), ('−2', [0,1,1,0,1]), ('1/2', [0,0,1,0,1]), ('π', [0,0,0,1,1])]
x0, cw, ch = 12, 14.4, 9
for j, c in enumerate(cols):
    text(ax, x0 + j*cw + cw/2, 66, c, 'sujet' if j != 3 else 'autre', 's', rot=90, va='bottom')
for i, (lab, vals) in enumerate(rows):
    y = 48 - i*(ch+1.5)
    text(ax, 6, y + ch/2, lab, 'encre', 'l')
    for j, v in enumerate(vals):
        box(ax, x0 + j*cw + 0.8, y, cw - 1.6, ch, 'resultat' if v else 'fixe', fill=bool(v), dash=not v)
arrow(ax, (x0 + 1, 10), (x0 + 3*cw - 1, 10), 'varie')
text(ax, x0 + 1.5*cw, 5, 'de l’intérieur vers l’extérieur', 'varie', 's')
box(ax, 60, 4, 5, 4, 'resultat'); text(ax, 67, 6, 'oui', 'resultat', 's', ha='left')
box(ax, 74, 4, 5, 4, 'fixe', fill=False, dash=True); text(ax, 81, 6, 'non', 'fixe', 's', ha='left')
save(fig, '12-085')
