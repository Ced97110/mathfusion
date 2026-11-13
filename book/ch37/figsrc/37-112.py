import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
import math
s = 0.85; R = 80 / math.sqrt(7)
A0, B0, C0 = (0, 0), (60, 0), (37.5, math.sqrt(1093.75)); O0 = (30, math.sqrt(R * R - 900))
cx, cy = 44, 36
T = lambda p: (cx + (p[0] - O0[0]) * s, cy + (p[1] - O0[1]) * s)
disc(ax, cx, cy, R * s, 'fixe', fill=False, lw=0.9)
poly(ax, [T(A0), T(B0), T(C0)], 'sujet')
Cp = T(C0); dx, dy = cx - Cp[0], cy - Cp[1]; n = math.hypot(dx, dy); Cq = (cx + dx / n * R * s, cy + dy / n * R * s)
arrow(ax, Cp, Cq, 'varie', both=True, lw=1.2)
disc(ax, cx, cy, 1.1, 'varie')
text(ax, cx + 4, cy + 3.5, 'O', 'varie', weight='bold')
text(ax, Cp[0] + 3, Cp[1] + 3, 'C', 'sujet', weight='bold')
text(ax, (T(A0)[0] + T(B0)[0]) / 2, T(A0)[1] - 3.2, '60 m', 'sujet', 's')
text(ax, 40, 18, r'$2R \approx 60{,}47$ m', 'varie', 's', ha='left')
text(ax, 44, 70, r'$R = 80/\sqrt{7} \approx 30{,}24$ m', 'resultat', 'm')
save(fig, '37-112')
