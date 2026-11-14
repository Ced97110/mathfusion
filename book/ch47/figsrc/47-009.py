import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, R = 26, 29, 21
pts = []
for h in range(12):
    a = math.radians(90 - 30 * h); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    if h % 3 == 0: pts.append((x, y))
poly(ax, pts, 'sujet', fill=False, lw=0.8)
for h in range(12):
    a = math.radians(90 - 30 * h); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    if h % 3 == 0: disc(ax, x, y, 3.8, 'sujet', label=str(h), size='m')
    else: disc(ax, x, y, 1.2, 'fixe')
text(ax, cx, cy + 2, r'$H$', 'sujet', 'xl'); text(ax, cx, cy - 4, '4 heures', 'sujet', 's')
def clk(h):
    a = math.radians(90 - 30 * h); return (cx + R * math.cos(a), cy + R * math.sin(a))
disc(ax, *clk(0), 5.6, 'resultat', fill=False, lw=1.2)
line(ax, [(clk(9)[0]+4.4, cy), (clk(3)[0]-4.4, cy)], 'resultat', dash=True)
text(ax, 67, 52, '0 est dans H', 'resultat', 's')
text(ax, 67, 43, 'Sommes dans H', 'resultat', 's')
for i, t in enumerate([r'$3+6=9$', r'$6+9=3$']): text(ax, 67, 36 - i * 7, t, 'resultat', 'm')
text(ax, 67, 20, 'Opposés dans H', 'resultat', 's')
for i, t in enumerate([r'$3+9=0$', r'$6+6=0$']): text(ax, 67, 13 - i * 7, t, 'resultat', 'm')
save(fig, '47-009')
