import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$(u,\ v)$', 'sujet', 'xl')
data = [(36, 'A = ℝ', r'$u=1$', r'$v=2$', 'complexe'), (14, 'A = ℂ', r'$u\in\mathbb{C}$', r'$v\in\mathbb{C}$', 'quaternion')]
for y, a, u_, v_, res in data:
    text(ax, 12, y + 5, a, 'sujet', 'm')
    box(ax, 22, y, 14, 10, 'sujet', label=u_, size='l'); box(ax, 38, y, 14, 10, 'sujet', label=v_, size='l')
    arrow(ax, (54, y + 5), (60, y + 5), 'varie')
    box(ax, 62, y, 24, 10, 'resultat', label=res)
save(fig, '78-100')
