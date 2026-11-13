import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ys = [6, 32, 58]; labs = [r'$\mathbb{Q}$', r'$\mathbb{Q}(\sqrt{2})$', r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$']; rl = ['fixe', 'autre', 'sujet']
ws = [14, 24, 34]
for y, l, r, w in zip(ys, labs, rl, ws): box(ax, 4, y, w, 13, r, label=l, size='s')
for i in range(2):
    arrow(ax, (9, ys[i] + 14), (9, ys[i + 1] - 1), 'varie', lw=1.2); text(ax, 13, ys[i] + 19.5, 'degré 2', 'varie', 's', ha='left')
text(ax, 50, 70, 'même corps, 3 façons :', 'encre', 's', ha='left')
for y, t in [(58, '(1) 4 briques'), (46, '(2) 2 générateurs'), (34, '(3) 2 étages')]: text(ax, 50, y, t, 'resultat', 's', ha='left')
save(fig, '61-124')
