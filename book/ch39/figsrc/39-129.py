import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, L = 30, 32, 24
arrow(ax, (cx - L - 2, cy), (cx + L + 2, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - L - 2), (cx, cy + L + 2), 'fixe', lw=0.6)
for a in (30, 100, 250):
    r = math.radians(a)
    q = (cx + L * math.cos(r), cy + L * math.sin(r))
    line(ax, [(cx, cy), q], 'varie', lw=0.9, dash=True)
    text(ax, cx + (L + 4.5) * math.cos(r), cy + (L + 4.5) * math.sin(r), f'{a}°', 'varie', 's')
disc(ax, cx, cy, 2.0, 'sujet')
text(ax, cx + 5, cy - 4, r'$O$', 'sujet', ha='left')
text(ax, 70, 50, r'$r=0$', 'sujet')
text(ax, 70, 40, r'$0\times\cos\theta=0$', 'encre', 's')
text(ax, 70, 33, r'$0\times\sin\theta=0$', 'encre', 's')
text(ax, 70, 21, r'$\tan\theta=0/0$', 'limite')
text(ax, 70, 14, 'sans sens', 'limite', 's')
save(fig, '39-129')
