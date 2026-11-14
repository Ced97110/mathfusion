import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="encre", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(58)
def tri(x0, y0, s, a, b, h, r, res):
    C = (x0, y0); A = (x0 + 4 * s, y0); B = (x0, y0 + 3 * s)
    poly(ax, [C, A, B], 'fixe')
    line(ax, [C, A], 'varie', lw=2.0); line(ax, [C, B], 'sujet', lw=2.0); line(ax, [A, B], 'fixe', lw=2.0)
    text(ax, x0 + 2 * s, y0 - 3.4, f'b = {b}', 'varie', 's')
    text(ax, x0 - 5.5, y0 + 1.5 * s, f'a = {a}', 'sujet', 's')
    text(ax, x0 + 2 * s + 3.0, y0 + 1.5 * s + 3.4, str(h), 'fixe', 's')
    arc(ax, B, r, 270, 323.13); text(ax, B[0] + r * 0.9 + 1.5, B[1] + 1.8, 'B', 'encre', 's', weight='bold')
    text(ax, x0 + 2 * s, y0 - 9, res, 'resultat', 'm', weight='bold')
tri(12, 18, 4.5, 3, 4, 5, 3.5, r'4 ÷ 3 ≈ 1,333')
tri(44, 18, 9, 6, 8, 10, 6, r'8 ÷ 6 ≈ 1,333')
text(ax, 44, 52, r'$\tan B = b\,/\,a$', 'encre', 'l')
save(fig, '25-066')
