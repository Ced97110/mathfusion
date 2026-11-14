import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 24
f = numberline(ax, 8, 72, y, 0, 4, step=1, labels=False, arrow_right=True)
for v, lab in enumerate(['0', 'a', '2a', '3a', '4a']):
    disc(ax, f(v), y, 1.7, 'sujet')
    text(ax, f(v), y - 6.5, lab, 'sujet', 'm')
disc(ax, f(0.5), y, 1.7, 'limite')
text(ax, f(0.5), y + 12, 'a/2', 'limite', 'm', weight='bold')
arrow(ax, (f(0.5), y + 9), (f(0.5), y + 3.2), 'limite')
text(ax, 44, 56, r'si $\mathbb{Q}$ était engendré par un seul nombre $a$ :', 'encre', 's')
text(ax, 44, 50, 'ses éléments seraient 0, a, 2a, 3a, …', 'sujet', 's')
text(ax, 62, 36, 'a/2 est dans ℚ,', 'limite', 's')
text(ax, 62, 31.5, 'pas un multiple entier de a', 'limite', 's')
text(ax, 44, 8, 'ℚ n’est pas de type fini', 'limite', 'm', weight='bold')
save(fig, '60-143')
