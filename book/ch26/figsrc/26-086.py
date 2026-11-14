import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(52)
x0, y0, L = 4, 38, 62
rise = L * 0.1
hyp = math.hypot(L, rise)
line(ax, [(x0, y0), (x0 + L, y0)], 'fixe', lw=1.4)
line(ax, [(x0 + L, y0), (x0 + L, y0 + rise)], 'sujet', lw=1.6)
line(ax, [(x0, y0), (x0 + L, y0 + rise)], 'autre', lw=1.4)
text(ax, x0 + L / 2, y0 - 3.5, 'avancée 100 m', 'fixe', 's')
text(ax, x0 + L + 2, y0 + rise / 2, 'montée 10 m', 'sujet', 's', ha='left')
text(ax, x0 + L / 2, y0 + rise + 4, 'chemin', 'autre', 's')
box(ax, 2, 14, 40, 14, 'sujet'); text(ax, 22, 24, 'pente = tan θ', 'sujet', 's'); text(ax, 22, 18, '10 / 100 = 0,1', 'sujet', 'm', weight='bold')
box(ax, 46, 14, 40, 14, 'autre'); text(ax, 66, 24, 'sinus θ', 'autre', 's'); text(ax, 66, 18, '10 / chemin ≈ 0,0995', 'autre', 's')
text(ax, 44, 7, 'angle ≈ 5,71° (en degrés)', 'fixe', 's')
save(fig, '26-086')
