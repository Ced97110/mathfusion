import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1, y0, hgt = 8, 76, 14, 32
fx = lambda d: x0 + d / 180 * (x1 - x0)
fy = lambda s: y0 + s * hgt
def curve(d0, d1, role):
    n = 40; pts = [(fx(d0 + (d1 - d0) * i / n), fy(math.sin(math.radians(d0 + (d1 - d0) * i / n)))) for i in range(n + 1)]
    line(ax, pts, role, 1.8)
curve(0, 90, 'resultat'); curve(90, 180, 'fixe')
numberline(ax, x0, x1, y0, 0, 180, step=30, arrow_right=False, every=1)
# 30° et 60° : le sinus croît
for d, v in ((30, '0,5'), (60, '0,866')):
    s = math.sin(math.radians(d))
    line(ax, [(fx(d), y0), (fx(d), fy(s))], 'resultat', 0.7, dash=True)
    disc(ax, fx(d), fy(s), 1.0, 'resultat')
# 120° : même sinus que 60°
s = math.sin(math.radians(60))
line(ax, [(fx(60), fy(s)), (fx(120), fy(s))], 'limite', 0.8, dash=True)
line(ax, [(fx(120), y0), (fx(120), fy(s))], 'limite', 0.7, dash=True)
disc(ax, fx(120), fy(s), 1.0, 'limite')
text(ax, fx(30) - 5, fy(0.5) + 3, '0,5', 'resultat', 's'); text(ax, fx(60) - 6, fy(s) + 1.5, '0,866', 'resultat', 's')
text(ax, fx(120) + 7, fy(s) + 3, '0,866', 'limite', 's')
text(ax, 42, y0 - 9, 'angle en degrés', 'fixe', 's')
text(ax, fx(45), 58, 'de 0° à 90° : le sinus croît', 'resultat', 's')
text(ax, fx(120), 52, 'à 120° : même sinus', 'limite', 's')
save(fig, '27-047')
