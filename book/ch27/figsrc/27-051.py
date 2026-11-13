import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
mx, my = 20, 16
a = math.radians(30)
line(ax, [(mx, my), (mx + 56, my)], 'fixe', lw=2.0)
tip = (mx + 50 * math.cos(a), my + 50 * math.sin(a))
line(ax, [(mx, my), tip], 'autre', lw=2.0)
r = 22
pts = [(mx, my)] + [(mx + r * math.cos(a * t / 20), my + r * math.sin(a * t / 20)) for t in range(21)]
poly(ax, pts, 'sujet', lw=0.6)
text(ax, mx + 32, my + 3.5, '30°', 'sujet', 'l')
text(ax, mx + 57, my - 1, 'dans le sol', 'fixe', 's', ha='right', va='top')
text(ax, tip[0] + 1, tip[1] + 4.5, 'dans le toit', 'autre', 's', ha='right')
disc(ax, mx, my, 2.0, 'sujet')
disc(ax, mx, my, 0.6, 'encre')
text(ax, mx, my - 5.5, r'$M$ : sur la charnière', 'sujet', 's', ha='left')
text(ax, mx - 12, my + 22, 'charnière', 'sujet', 's', ha='left')
text(ax, mx - 12, my + 18.6, 'vue de bout', 'sujet', 's', ha='left')
arrow(ax, (mx - 5, my + 16), (mx - 2.2, my + 3.2), 'sujet', lw=0.8)
save(fig, '27-051')
