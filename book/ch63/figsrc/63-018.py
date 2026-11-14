import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 22, 66, 'sous-groupes', 'encre', 's')
text(ax, 66, 66, 'corps', 'encre', 's')
roles = ['varie', 'autre', 'sujet']
left = [r'$\langle\sigma\rangle$', r'$\langle\tau\rangle$', r'$\langle\sigma\tau\rangle$']
right = [r'$\mathbb{Q}(\sqrt{3})$', r'$\mathbb{Q}(\sqrt{2})$', r'$\mathbb{Q}(\sqrt{6})$']
for cx0, top, bot, mids, xs, bw in [(22, r'$G$', r'$\{1\}$', left, [9, 22, 35], 11), (66, r'$\mathbb{Q}$', r'$E$', right, [52, 66, 80], 12.5)]:
    box(ax, cx0 - 6, 50, 12, 9, 'fixe', label=top)
    box(ax, cx0 - 6, 10, 12, 9, 'fixe', label=bot)
    for x, lab, role in zip(xs, mids, roles):
        box(ax, x - bw / 2, 30, bw, 9, role, label=lab, size='s')
        line(ax, [(cx0, 50), (x, 39)], 'fixe')
        line(ax, [(x, 30), (cx0, 19)], 'fixe')
save(fig, '63-018')
