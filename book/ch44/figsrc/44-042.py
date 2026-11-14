import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
BX = [3, 34, 65]
def lane(y, vals, g, grole, last, sub, note, tag):
    roles = ['sujet', 'fixe', last]
    for x, v, r in zip(BX, vals, roles): box(ax, x, y - 5.5, 20, 11, r, label=v)
    for (a, b), (t, tr) in zip([(BX[0], BX[1]), (BX[1], BX[2])], [(r'$\alpha$', 'varie'), (g, grole)]):
        arrow(ax, (a + 21, y), (b - 1, y), tr, lw=1.8 if tr == grole and tr != 'varie' else 1.0); text(ax, (a + b + 20) / 2, y + 4.5, t, tr, 'm')
    text(ax, BX[1] + 31, y - 8, sub, grole, 's')
    text(ax, BX[2] + 10, y - 13.5, note, last, 's')
    text(ax, 44, y + 14, tag, grole, 's', weight='bold')
lane(52, ['1, 2', '2, 1', '2, 1'], r'$1_S$', 'sujet', 'resultat', 'ne change rien', r'$1_S \circ \alpha = \alpha$', 'identité : neutre')
lane(16, ['1, 2', '2, 1', '1, 1'], r'$\beta$', 'autre', 'limite', 'tout devient 1', r'$\beta \circ \alpha \neq \alpha$', r'$\beta$ : pas neutre')
save(fig, '44-042')
