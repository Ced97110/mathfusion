import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = lambda v: 8 + v * 6.4
ys = 30
for v in range(12):
    inH = v % 3 == 0
    disc(ax, X(v), ys, 1.9 if inH else 1.2, 'resultat' if inH else 'sujet')
for v in (0, 3, 6, 9):
    text(ax, X(v), ys - 5.5, str(v), 'resultat', 's')
for v in range(11):
    arrow(ax, (X(v) + 1.4, ys - 1), (X(v + 1) - 1.4, ys - 1), 'sujet', lw=0.6, curve=0.5)
for v in (0, 3, 6):
    arrow(ax, (X(v) + 1.5, ys + 2), (X(v + 3) - 1.5, ys + 2), 'varie', lw=1.0, curve=-0.45)
text(ax, 44, 55, r'un groupe cyclique $G$ : 1 générateur', 'sujet', 'm')
text(ax, 44, 49, r'ses pas : $a$, $a^2$, $a^3$, …', 'sujet', 's')
text(ax, 44, 17, r'un sous-groupe $H$ : 0, 3, 6, 9', 'resultat', 'm')
text(ax, 44, 11, r'ses pas : $a^3$ seulement', 'varie', 's')
text(ax, 44, 4.5, r'$H$ est cyclique aussi', 'resultat', 'm', weight='bold')
save(fig, '46-114')
