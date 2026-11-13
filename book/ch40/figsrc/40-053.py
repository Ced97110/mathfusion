import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Famille : cercle r = 2a cos θ, cardioïde r = 1 + cos θ, rosaces r = a cos(nθ) (n = 3 puis n = 2)
fig, ax = canvas(56)
def curve(o, u, f, role):
    pts = [(o[0] + u * f(t) * math.cos(t), o[1] + u * f(t) * math.sin(t)) for t in [i * 2 * math.pi / 360 for i in range(361)]]
    line(ax, pts, role, lw=1.4)
y0 = 32
curve((2.5, y0), 8, lambda t: 2 * math.cos(t), 'fixe')
curve((29, y0), 7.5, lambda t: 1 + math.cos(t), 'fixe')
curve((55, y0), 10, lambda t: math.cos(3 * t), 'sujet')
curve((77, y0), 10, lambda t: math.cos(2 * t), 'sujet')
for x in (2.5, 29, 55, 77):
    disc(ax, x, y0, 0.6, 'encre')
text(ax, 10.5, 14, 'cercle', 'fixe', 's')
text(ax, 10.5, 9, r'$r = 2a\cos\theta$', 'fixe', 's')
text(ax, 33, 14, 'cardioïde', 'fixe', 's')
text(ax, 33, 9, r'$r = 1 + \cos\theta$', 'fixe', 's')
text(ax, 55, 14, r'$n = 3$', 'sujet', 's')
text(ax, 77, 14, r'$n = 2$', 'sujet', 's')
text(ax, 66, 9, r'rosace $r = a\cos(n\theta)$', 'sujet', 's')
text(ax, 44, 52, 'même famille : un cosinus', 'encre', 'm')
text(ax, 66, 47, r'$n$ multiplie l’angle', 'sujet', 's')
save(fig, '40-053')
