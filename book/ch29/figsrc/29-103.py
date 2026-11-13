import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(76)
text(ax, 44, 72, 'piste de rayon 50 m', 'encre')
text(ax, 22, 62, 'arc s', 'sujet', 'm', weight='bold'); text(ax, 66, 62, 'aire A', 'varie', 'm', weight='bold')
C = (22, 40)
n = 160
sp = [(C[0] + (8 + 7 * i / n) * math.cos(4 * math.pi * i / n), C[1] + (8 + 7 * i / n) * math.sin(4 * math.pi * i / n)) for i in range(n + 1)]
line(ax, sp, 'sujet', lw=1.6)
arrow(ax, sp[-4], sp[-1], 'sujet', lw=1.2)
text(ax, C[0], C[1], '2 tours', 'sujet', 's')
text(ax, 22, 22, '628 m parcourus', 'resultat'); text(ax, 22, 16, 'sens gardé', 'resultat', 's')
D = (66, 40)
disc(ax, D[0], D[1], 15, 'varie'); text(ax, D[0], D[1], r'$\times 2$', 'varie', 'xl')
text(ax, 66, 22, r'$2\times 7\,854$ m$^2$', 'varie'); text(ax, 66, 16, 'surface balayée', 'varie', 's')
save(fig, '29-103')
