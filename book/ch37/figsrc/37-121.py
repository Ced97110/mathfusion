import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 26, 32, 20.0
pos = lambda t, r=R: (cx + r * math.cos(math.radians(t)), cy + r * math.sin(math.radians(t)))
Bp, Cp, Ap = pos(210), pos(310), pos(430)
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
poly(ax, [Ap, Bp, Cp], 'sujet')
disc(ax, cx, cy, 0.8, 'fixe')
line(ax, [(cx, cy), Ap], 'varie', dash=True)
text(ax, cx + 4.2, cy + 7.5, r'$R$', 'varie', 'm')
for t, a in ((70, '50°'), (210, '60°'), (310, '70°')):
    text(ax, *pos(t, R + 4.2), a, 'sujet', 's')
for P, Q, l in ((Bp, Cp, r'$a$'), (Cp, Ap, r'$b$'), (Ap, Bp, r'$c$')):
    m = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2); d = math.hypot(m[0] - cx, m[1] - cy)
    text(ax, m[0] + (m[0] - cx) / d * -3.2, m[1] + (m[1] - cy) / d * -3.2, l, 'sujet', 'm')
text(ax, 52, 56, r'$R$ = 10 cm', 'varie', 's', ha='left')
text(ax, 52, 48, r'$a$ = 20 sin 50° ≈ 15,3', 'sujet', 's', ha='left')
text(ax, 52, 41, r'$b$ = 20 sin 60° ≈ 17,3', 'sujet', 's', ha='left')
text(ax, 52, 34, r'$c$ = 20 sin 70° ≈ 18,8', 'sujet', 's', ha='left')
box(ax, 51, 12, 35, 11, 'resultat', label='Δ ≈ 124,7 cm²', size='m')
arrow(ax, (68, 31), (68, 24), 'resultat')
save(fig, '37-121')
