import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
y = 30; x0, x1 = 8, 78
X = lambda d: x0 + d / 180 * (x1 - x0)
line(ax, [(x0, y), (x1, y)], 'fixe')
pi_lab = {30: r'$\pi/6$', 45: r'$\pi/4$', 60: r'$\pi/3$', 90: r'$\pi/2$', 180: r'$\pi$'}
for d in (0, 30, 45, 60, 90, 180):
    line(ax, [(X(d), y - 1.3), (X(d), y + 1.3)], 'fixe')
    text(ax, X(d), y - 4, f'{d}°', 'sujet' if d == 30 else 'fixe', 's')
    if d in pi_lab:
        yy = y + (10 if d == 45 else 5.5)
        if d == 45: line(ax, [(X(d), y + 1.8), (X(d), yy - 1.8)], 'fixe', lw=0.5)
        text(ax, X(d), yy, pi_lab[d], 'sujet' if d == 30 else 'fixe', 's')
disc(ax, X(30), y, 1.5, 'sujet')
text(ax, X(30), y + 14.5, r'$A$', 'sujet', 'l')
arrow(ax, (X(30), y + 12.5), (X(30), y + 8.5), 'sujet', lw=0.8)
brace(ax, X(0), X(30), y - 8, 'sujet', label='1/6 de demi-tour')
brace(ax, X(0), X(180), y - 17, 'fixe', label=None)
text(ax, X(90), y - 23, 'demi-tour = 180° = π', 'fixe', 's')
save(fig, '33-012')
