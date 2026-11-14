import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def panel(y, title, cont):
    text(ax, 4, y + 17, title, 'sujet', 'm', ha='left', weight='bold')
    f = numberline(ax, 14, 62, y, 0, 4, labels=True, every=2, role='fixe')
    if cont: line(ax, [(f(0), y), (f(4), y)], 'sujet', lw=2.4)
    else:
        for v in range(5): disc(ax, f(v), y, 1.5, 'sujet')
    return f
f = panel(50, r'domaine $\mathbb{R}$', True)
arrow(ax, (f(1.5), 53), (f(3), 53), 'varie', curve=-0.5); text(ax, (f(1.5) + f(3)) / 2, 61, r'$\times2$', 'varie', 'm')
disc(ax, f(1.5), 50, 2.0, 'varie'); disc(ax, f(3), 50, 2.0, 'resultat')
text(ax, f(1.5), 45, '1,5', 'varie', 's'); text(ax, f(3), 45, '3', 'resultat', 's')
g = panel(16, r'domaine $\mathbb{N}$', False)
x = g(1.5)
line(ax, [(x - 2, 14), (x + 2, 18)], 'limite', lw=1.4); line(ax, [(x - 2, 18), (x + 2, 14)], 'limite', lw=1.4)
text(ax, x, 11, '1,5', 'limite', 's')
save(fig, '42-174')
