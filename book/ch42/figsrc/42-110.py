import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lens(cx1, cx2, cy, r):
    a = math.acos((cx2 - cx1) / (2 * r)); n = 24
    right = [(cx1 + r * math.cos(-a + 2 * a * i / n), cy + r * math.sin(-a + 2 * a * i / n)) for i in range(n + 1)]
    left = [(cx2 + r * math.cos(math.pi - a + 2 * a * i / n), cy + r * math.sin(math.pi - a + 2 * a * i / n)) for i in range(n + 1)]
    return right + left
fig, ax = canvas(74)
text(ax, 44, 69, r'$A \cap B$', 'sujet', 'xl'); text(ax, 44, 62, 'lu « A inter B »', 'sujet', 's')
disc(ax, 33, 40, 16, 'fixe'); disc(ax, 55, 40, 16, 'fixe')
poly(ax, lens(33, 55, 40, 16), 'sujet')
text(ax, 24, 40, r'$A$', 'fixe', 'l'); text(ax, 64, 40, r'$B$', 'fixe', 'l')
disc(ax, 44, 40, 1.4, 'varie'); text(ax, 44, 35, r'$x$', 'varie', 'm')
text(ax, 44, 17, r'$x \in A \cap B$', 'sujet', 'l')
text(ax, 44, 9, r'$x \in A$  et  $x \in B$', 'resultat', 'm')
save(fig, '42-110')
