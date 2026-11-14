import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ys = {1: 62, 2: 52, 3: 42}
for p in (1, 2, 3):
    text(ax, 2, ys[p], f'place {p}', 'fixe', 's', ha='left')
text(ax, 28, 72, '1↔3, puis 1↔2', 'sujet', 's', weight='bold')
text(ax, 64, 72, '1↔2, puis 1↔3', 'autre', 's', weight='bold')
for x0, places, role in ((18, (1, 3, 3), 'sujet'), (54, (1, 2, 2), 'autre')):
    pts = [(x0 + 12 * t, ys[p]) for t, p in enumerate(places)]
    for a, b in zip(pts, pts[1:]):
        if a != b:
            d = math.hypot(b[0] - a[0], b[1] - a[1]); ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
            arrow(ax, (a[0] + 2.6 * ux, a[1] + 2.6 * uy), (b[0] - 2.6 * ux, b[1] - 2.6 * uy), role, lw=1.2)
        else:
            line(ax, [(a[0] + 2.6, a[1]), (b[0] - 2.6, b[1])], role, lw=1.2, dash=True)
    for q in pts: disc(ax, q[0], q[1], 2.2, role)
text(ax, 46, 33, 'objet 1 : fin à des places différentes', 'encre', 's')
labs = (r'$S_4$', r'$A_4$', r'$V$', r'$\{e\}$')
for i, lab in enumerate(labs):
    x = 1 + 24 * i
    box(ax, x, 6, 14, 9, 'sujet', label=lab, size='s')
    if i < 3:
        arrow(ax, (x + 14.5, 10.5), (x + 23.5, 10.5), 'resultat')
        text(ax, x + 19, 17.5, ('ℤ/2', 'ℤ/3', r'$V$')[i], 'resultat', 's')
save(fig, '64-023')
