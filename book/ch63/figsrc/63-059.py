import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cx, cy, R = 36, 46, 26
ang = [0, 120, 240]
P = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in ang]
poly(ax, P, 'fixe')
line(ax, [(6, cy), (70, cy)], 'fixe', lw=0.6, dash=True)
for p in P:
    disc(ax, p[0], p[1], 3.2, 'sujet')
for a, l in zip(ang, [r'$r$', r'$jr$', r'$j^2r$']):
    rr = R + 9.5
    text(ax, cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a)), l, 'sujet', 'm')
Ra = R + 7
for a in ang:
    pts = [(cx + Ra * math.cos(math.radians(a + 15 + 90 * t / 12)), cy + Ra * math.sin(math.radians(a + 15 + 90 * t / 12))) for t in range(13)]
    line(ax, pts, 'varie', lw=1.2)
    arrow(ax, pts[-2], pts[-1], 'varie', lw=1.2)
text(ax, cx + 40 * math.cos(math.radians(60)), cy + 40 * math.sin(math.radians(60)), r'$\sigma$', 'varie', 'l')
arrow(ax, (31, cy + 14), (31, cy - 14), 'resultat', lw=1.4, both=True)
text(ax, 36, cy + 8, r'$\tau$', 'resultat', 'l')
text(ax, 44, 4, r'$\sigma$ : tiers de tour ; $\tau$ : miroir', 'encre', 'm')
save(fig, '63-059')
