import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
vals = ['2 cis 30°', '4 cis 60°', '8 cis 90°', '16 cis 120°']
exps = ['$z^{1}$', '$z^{2}$', '$z^{3}$', '$z^{4}$']
w, h, g, x0, y0 = 17.5, 11, 4.7, 3, 28
for i, v in enumerate(vals):
    x = x0 + i * (w + g)
    role = 'sujet' if i == 0 else ('resultat' if i == 3 else 'fixe')
    box(ax, x, y0, w, h, role, label=v, size='s')
    text(ax, x + w / 2, y0 + h + 3.5, exps[i], role if i in (0, 3) else 'fixe', 'm')
    if i < 3:
        arrow(ax, (x + w, y0 + h / 2), (x + w + g, y0 + h / 2), 'varie', lw=1.3)
text(ax, x0 + w / 2, y0 - 4, 'départ', 'sujet', 's')
text(ax, x0 + 3 * (w + g) + w / 2, y0 - 4, 'arrivée', 'resultat', 's')
brace(ax, x0 + w, x0 + 3 * (w + g), y0 - 8, 'varie', label='chaque pas : × z, de n à n + 1', down=True, size='s')
text(ax, 44, 52, 'même pas répété : ×z', 'varie', 's')
save(fig, '39-079')
