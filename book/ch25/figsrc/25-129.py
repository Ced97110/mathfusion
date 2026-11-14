import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'$0° < A < 90°$', 'sujet', 'l')
f = numberline(ax, 10, 76, 36, 0, 90, step=30, labels=False, arrow_right=False)
line(ax, [(f(0), 36), (f(90), 36)], 'resultat', lw=3)
for v in (0, 30, 60, 90): text(ax, f(v), 31.5, f'{v}°', 'fixe', 's')
disc(ax, f(0), 36, 1.8, 'limite'); disc(ax, f(90), 36, 1.8, 'limite')
disc(ax, f(40), 36, 1.5, 'varie'); text(ax, f(40), 41, 'A', 'varie', 'm')
# cas 0 degré : triangle aplati
line(ax, [(8, 14), (26, 14)], 'limite', lw=1.6); text(ax, 17, 7, 'A = 0° : aplati', 'limite', 's')
# cas réel
poly(ax, [(34, 14), (52, 14), (52, 14 + 18 * math.tan(math.radians(40)))], 'resultat')
text(ax, 43, 7, '0° < A < 90°', 'resultat', 's')
# cas 90 degrés
line(ax, [(74, 14), (74, 28)], 'limite', lw=1.6); text(ax, 74, 7, 'A = 90° : aplati', 'limite', 's')
save(fig, '25-129')
