import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
cx, cy, S = 34, 22, 30
th = np.radians(np.linspace(-45, 45, 300)); r = np.sqrt(np.cos(2 * th))
for sg in (1, -1):
    line(ax, list(zip(cx + sg * S * r * np.cos(th), cy + sg * S * r * np.sin(th))), 'sujet', lw=1.3)
line(ax, [(cx - 34, cy), (cx + 36, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy), (cx + 16, cy + 16)], 'fixe', dash=True)
disc(ax, cx + S, cy, 1.3, 'varie'); text(ax, cx + S + 3, cy + 3, 'θ = 0 :', 'varie', 's', ha='left')
text(ax, cx + S + 3, cy - 2, r'$r^2$ = 1', 'varie', 's', ha='left')
disc(ax, cx, cy, 1.3, 'varie'); text(ax, cx + 18, cy + 19, r'θ = 45° : $r^2$ = 0', 'fixe', 's', ha='left')
text(ax, 44, 46, r'$r^2 = a^2 \cos 2\theta$, $a$ = 1', 'sujet', 'l')
save(fig, '34-179')
