import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="encre", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(52)
s = 7.5
def tri(x0, y0, ch):
    C = (x0, y0); A = (x0 + 4 * s, y0); B = (x0, y0 + 3 * s)
    poly(ax, [C, A, B], 'fixe')
    rb, ra = ('sujet', 'varie') if ch == 'A' else ('varie', 'sujet')
    line(ax, [C, A], rb, lw=2.2); line(ax, [C, B], ra, lw=2.2); line(ax, [A, B], 'fixe', lw=2.2)
    text(ax, x0 + 2 * s, y0 - 3.4, 'b = 4', rb, 's')
    text(ax, x0 - 5.5, y0 + 1.5 * s, 'a = 3', ra, 's')
    text(ax, x0 + 2 * s + 3.0, y0 + 1.5 * s + 3.4, '5', 'fixe', 's')
    if ch == 'A':
        arc(ax, A, 6, 143.13, 180); text(ax, A[0] + 3, A[1] - 3, 'A', 'encre', 'm', weight='bold')
    else:
        arc(ax, B, 6, 270, 323.13); text(ax, B[0] + 3.2, B[1] + 2.2, 'B', 'encre', 'm', weight='bold')
    return C
tri(11, 14, 'A'); tri(51, 14, 'B')
text(ax, 26, 43, 'angle choisi A', 'encre', 'm'); text(ax, 66, 43, 'angle choisi B', 'encre', 'm')
text(ax, 26, 4.5, r'$\tan A = a\,/\,b$', 'encre', 'm'); text(ax, 66, 4.5, r'$\tan B = b\,/\,a$', 'encre', 'm')
save(fig, '25-065')
