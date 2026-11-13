import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(60)
R, th, O = 50, 0.6, (10, 8)
A = (60, 8); T = (60, 8 + R * math.tan(th))
poly(ax, [O, A, T], 'sujet')
line(ax, [A, T], 'resultat', lw=2.2)
line(ax, [(57, 8), (57, 11), (60, 11)], 'fixe')
line(ax, arc(O[0], O[1], 12, 0, th), 'varie', lw=1.2)
text(ax, 31, 11.5, r'$\theta = 0{,}6$', 'varie', 's')
text(ax, 6, 5.5, r'$O$'); text(ax, 60, 4.5, r'$A$'); text(ax, 63, 45, r'$T$')
text(ax, 35, 4.5, 'OA = 1', 'sujet', 's'); text(ax, 75, 25, r'$AT \approx 0{,}684$', 'resultat', 's')
text(ax, 36, 54, 'aire du triangle OAT', 'sujet')
text(ax, 36, 48, r'$\frac{1}{2}\times 1\times 0{,}684 \approx 0{,}342$', 'sujet')
save(fig, '29-110')
