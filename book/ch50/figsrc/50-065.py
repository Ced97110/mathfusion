import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, 'Bon ordre', 'resultat', 'm', weight='bold')
xs = [3, 32, 61]; bw = 24
titles = ['I', 'II', 'III']
subs = ["un $p$-Sylow\nexiste", "tous sont\nconjugués", "on compte\nleur nombre"]
for x, t, s in zip(xs, titles, subs):
    box(ax, x, 48, bw, 20, 'sujet')
    text(ax, x + bw / 2, 63, t, 'sujet', 'l', weight='bold')
    text(ax, x + bw / 2, 54, s, 'sujet', 's')
for a, b in [(0, 1), (1, 2)]:
    arrow(ax, (xs[a] + bw + 0.5, 58), (xs[b] - 0.5, 58), 'resultat', lw=1.2)
text(ax, 44, 42, 'Mauvais ordre', 'limite', 'm', weight='bold')
box(ax, 3, 6, 24, 30, 'limite')
text(ax, 15, 31, 'III', 'limite', 'l', weight='bold')
text(ax, 15, 17, 'lu en\npremier', 'limite', 's')
text(ax, 31, 26, 'sans I :', 'limite', 's', ha='left')
text(ax, 31, 22.5, 'ensemble vide ?', 'limite', 's', ha='left')
text(ax, 31, 14, 'sans II :', 'limite', 's', ha='left')
text(ax, 31, 10.5, 'pourquoi compter ?', 'limite', 's', ha='left')
save(fig, '50-065')
