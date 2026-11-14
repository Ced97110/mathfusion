import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, R = 24, 50, 14
line(ax, [(cx + R * math.cos(math.radians(t)), cy + R * math.sin(math.radians(t))) for t in range(0, 361, 5)], 'fixe', lw=0.5)
line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', lw=0.4)
line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', lw=0.4)
labs = [r'$\sqrt[3]{2}$', r'$j\sqrt[3]{2}$', r'$j^2\sqrt[3]{2}$']
for k, lab in enumerate(labs):
    a = math.radians(120 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2, 'sujet')
    text(ax, cx + (R + 7) * math.cos(a) - (2 if k == 0 else 0), cy + (R + 5) * math.sin(a), lab, 'sujet', 's')
line(ax, [(cx, cy), (cx + R * math.cos(math.radians(120)), cy + R * math.sin(math.radians(120)))], 'varie', lw=0.6)
line(ax, [(cx, cy), (cx + R, cy)], 'varie', lw=0.6)
text(ax, cx + 4, cy + 4.5, '120°', 'varie', 's')
box(ax, 54, 62, 32, 12, 'sujet', label=r'$E=\mathbb{Q}(j,\sqrt[3]{2})$')
box(ax, 54, 40, 32, 12, 'sujet', label=r'$\mathbb{Q}(j)$')
box(ax, 54, 18, 32, 12, 'sujet', label=r'$\mathbb{Q}$')
arrow(ax, (70, 31), (70, 39), 'varie'); arrow(ax, (70, 53), (70, 61), 'varie')
text(ax, 74, 35, '2', 'varie', 'm'); text(ax, 74, 57, '3', 'varie', 'm')
text(ax, 44, 7, r'$[E:\mathbb{Q}]=2\times3=6$ : $S_3$', 'resultat', 'm')
save(fig, '64-168')
