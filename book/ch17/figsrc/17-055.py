import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 22
arrow(ax, (6, y), (84, y), 'fixe', lw=0.9)
xa, xb, xc = 22, 46, 68
for x, s in [(xa, r'$a$'), (xb, r'$b$')]:
    disc(ax, x, y, 2.0, 'sujet')
    text(ax, x, y - 6, s, 'sujet', 'l')
ax.add_patch(Circle((xc, y), 2.0, ec=COL['autre'], fc=FILL['autre'], lw=0.9, ls='--', zorder=2))
text(ax, xc, y - 6, r'$c$', 'autre', 'l')
arrow(ax, (xc - 9, y + 6), (xc + 9, y + 6), 'autre', lw=0.9, both=True)
text(ax, xc, y + 10, 'place libre', 'autre', 's')
brace(ax, xa, xb, y + 4, 'sujet', r'$a$ à gauche de $b$', down=False)
text(ax, 44, 46, r'$a$, $b$, $c$ : nombres réels, $a < b$', 'fixe', 'm')
save(fig, '17-055')
