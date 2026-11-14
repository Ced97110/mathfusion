import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
bw, bh = 12.8, 9
ys = [72, 46, 20]
def hasse(x0, labels, roles, top, bot, role_ext):
    xs = [x0 + i * (bw + 0.9) for i in range(3)]
    cxm = xs[1]
    box(ax, cxm, ys[0], bw, bh, role_ext[0], label=top, size='s')
    box(ax, cxm, ys[2], bw, bh, role_ext[1], label=bot, size='s')
    for x, l, r in zip(xs, labels, roles):
        box(ax, x, ys[1], bw, bh, r, label=l, size='s')
        line(ax, [(x + bw / 2, ys[1] + bh), (cxm + bw / 2, ys[0])], r, lw=0.8)
        line(ax, [(x + bw / 2, ys[1]), (cxm + bw / 2, ys[2] + bh)], r, lw=0.8)
roles = ['varie', 'autre', 'resultat']
hasse(1.5, [r'$\langle\sigma\rangle$', r'$\langle\tau\rangle$', r'$\langle\sigma\tau\rangle$'], roles, r'$G$', r'$\{1\}$', ('sujet', 'fixe'))
hasse(46, [r'$\mathbb{Q}(\sqrt{3})$', r'$\mathbb{Q}(\sqrt{2})$', r'$\mathbb{Q}(\sqrt{6})$'], roles, r'$\mathbb{Q}$', r'$E$', ('fixe', 'sujet'))
text(ax, 44, 87, 'même forme, ordre renversé', 'resultat', 's')
text(ax, 21, 12, 'sous-groupes : du plus', 'sujet', 's'); text(ax, 21, 7, 'grand au plus petit', 'sujet', 's')
text(ax, 66, 12, 'corps : du plus', 'autre', 's'); text(ax, 66, 7, 'petit au plus grand', 'autre', 's')
save(fig, '63-188')
