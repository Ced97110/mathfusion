import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
import math
O = (23, 40); R = 19.0
th = {'A': 90, 'B': 230, 'C': 330}
V = {k: (O[0] + R * math.cos(math.radians(t)), O[1] + R * math.sin(math.radians(t))) for k, t in th.items()}
disc(ax, *O, R, 'fixe', fill=False, lw=0.9)
poly(ax, [V['A'], V['B'], V['C']], 'sujet')
arrow(ax, O, (O[0] + R, O[1]), 'varie', lw=1.2); disc(ax, *O, 0.8, 'varie')
text(ax, O[0] + R / 2, O[1] + 2.8, r'$R=10$ cm', 'varie', 's')
text(ax, V['A'][0], V['A'][1] - 3.6, '50°', 'sujet', 's'); text(ax, V['B'][0] + 6.5, V['B'][1] + 2.8, '60°', 'sujet', 's'); text(ax, V['C'][0] - 6.5, V['C'][1] + 2.8, '70°', 'sujet', 's')
text(ax, V['A'][0] + 2.5, V['A'][1] + 3.5, 'A', 'sujet', weight='bold'); text(ax, V['B'][0] - 3, V['B'][1] - 2, 'B', 'sujet', weight='bold'); text(ax, V['C'][0] + 3, V['C'][1] - 2, 'C', 'sujet', weight='bold')
bx, bw, h = 48, 38, 12
rows = [(r'$2R^2=2\times10^2=200$', 'sujet'), ('trois sinus :\n0,7660 ; 0,8660 ; 0,9397', 'sujet'), ('produit ≈ 0,6234', 'varie'), (r'$\Delta\approx200\times0{,}6234$' + '\n' + r'$\approx124{,}7$ cm²', 'resultat')]
tops = [72, 54, 36, 14]
for (lab, role), y in zip(rows, tops):
    hh = 13 if lab.count('\n') else 9
    box(ax, bx, y - hh, bw, hh, role, label=lab, size='s')
for y0, y1 in ((63, 54), (45, 36), (27, 27 - 0)): pass
arrow(ax, (bx + bw / 2, 63), (bx + bw / 2, 54), 'fixe'); arrow(ax, (bx + bw / 2, 41), (bx + bw / 2, 36), 'fixe'); arrow(ax, (bx + bw / 2, 27), (bx + bw / 2, 14), 'fixe')
save(fig, '37-120')
