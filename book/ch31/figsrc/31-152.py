import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(56)
s = 7.0; O = (10, 5)
arc(ax, O, 5 * s, -5, 100, 'fixe', 0.8)
line(ax, [O, (O[0] + 40, O[1])], 'fixe', 0.6); line(ax, [O, (O[0], O[1] + 42)], 'fixe', 0.6)
Pq = (O[0] + 3 * s, O[1] + 4 * s); Pr = (O[0] + 0.5981 * s, O[1] + 4.9641 * s)
line(ax, [O, Pq], 'sujet', 1.3); line(ax, [O, Pr], 'resultat', 1.3)
disc(ax, *Pq, 1.4, 'sujet'); disc(ax, *Pr, 1.4, 'resultat')
arc(ax, O, 14, math.degrees(math.atan2(4, 3)) + 1, math.degrees(math.atan2(4.9641, 0.5981)) - 1, 'varie', 1.2)
text(ax, O[0] + 6.8, O[1] + 19, r'$30°$', 'varie', 's')
text(ax, Pq[0] + 2, Pq[1] - 4, '(3 ; 4)', 'sujet', 's', ha='left')
text(ax, Pr[0] + 3, Pr[1] + 3, '(0,5981 ; 4,9641)', 'resultat', 's', ha='left')
text(ax, O[0] + 10, O[1] + 8.5, 'distance 5', 'sujet', 's', ha='left', rot=0) if False else None
text(ax, 66, 22, 'distance au centre : 5', 'sujet', 's'); text(ax, 66, 17, 'avant et après', 'sujet', 's')
text(ax, 66, 8, '0,3577 + 24,6423 = 25', 'resultat', 's')
save(fig, '31-152')
