import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(104)
text(ax, 44, 98, r'départ : $N(\alpha\beta)$, quatre facteurs', 'encre', 's')
xs = [14, 32, 50, 68]
top = [(r'$\alpha$', 'sujet'), (r'$\beta$', 'autre'), (r'$\bar{\alpha}$', 'sujet'), (r'$\bar{\beta}$', 'autre')]
bot = [top[0], top[2], top[1], top[3]]
for x, (s, r) in zip(xs, top): box(ax, x - 7, 80, 14, 12, r, s, 'l')
for x, (s, r) in zip(xs, bot): box(ax, x - 7, 46, 14, 12, r, s, 'l')
arrow(ax, (xs[0], 79), (xs[0], 59), 'varie')
arrow(ax, (xs[1], 79), (xs[2], 59), 'varie')
arrow(ax, (xs[2], 79), (xs[1], 59), 'varie')
arrow(ax, (xs[3], 79), (xs[3], 59), 'varie')
text(ax, 77, 69, 'on réordonne', 'varie', 's', ha='center')
text(ax, 44, 40, r'$\mathbb{C}$ est commutatif', 'varie', 's')
brace(ax, 7, 39, 36, 'sujet', r'$N(\alpha)=5$', True, 's')
brace(ax, 47, 79, 36, 'autre', r'$N(\beta)=10$', True, 's')
box(ax, 18, 6, 52, 12, 'resultat', r'$N(\alpha)N(\beta)=5\times 10=50$', 'm')
save(fig, '51-259')
