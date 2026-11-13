import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, 'entrées rangées par nombre de 1', 'encre', 's')
rows = [(76, [('000', 44, 'f')]),
        (62, [('001', 22, 'f'), ('010', 44, 'm'), ('100', 66, 'm')]),
        (48, [('011', 22, 'm'), ('101', 44, 'm'), ('110', 66, 'f')]),
        (34, [('111', 44, 'f')])]
pos = {}
for y, items in rows:
    for lab, x, k in items:
        box(ax, x - 6.5, y - 4, 13, 8, 'resultat' if k == 'f' else 'varie', label=lab, size='s')
        pos[lab] = (x, y)
arrow(ax, (pos['010'][0] + 7.2, 62), (pos['100'][0] - 7.2, 62), 'varie', both=True, lw=1.1)
arrow(ax, (pos['011'][0] + 7.2, 48), (pos['101'][0] - 7.2, 48), 'varie', both=True, lw=1.1)
box(ax, 4, 14, 36, 8, 'resultat', label='4 entrées fixes', size='s')
box(ax, 46, 14, 38, 8, 'varie', label='2 paires échangées', size='s')
text(ax, 44, 5, r'4 + 2 = 6 cycles, $2^{6}=64$', 'encre', 'm')
save(fig, '49-265')
