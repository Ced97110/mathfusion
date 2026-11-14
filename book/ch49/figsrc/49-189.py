import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1 = 8, 76; y = 44
f = numberline(ax, x0, x1, y, 0, 6, size='m', arrow_right=False)
for v in range(7):
    role = 'fixe' if v == 0 else ('limite' if v == 1 else 'resultat' if v == 2 else 'sujet')
    disc(ax, f(v), y + 7, 2.0, role)
text(ax, f(0), y + 14, '0 : non', 'fixe', 's', ha='left')
text(ax, f(1) + 5, y + 14, '1 : pas multiple de 2', 'limite', 's', ha='left')
text(ax, f(4), y - 11, '2, 4, 6 : multiples de 2', 'sujet', 's')
arrow(ax, (f(2), y + 4), (f(2), y - 1.5), 'resultat', lw=0.9)
text(ax, f(2), 21.5, r'$|C| \geq 1$ et multiple de 2 : $|C| \geq 2$', 'resultat', 'm')
box(ax, 10, 4, 68, 11, 'resultat')
disc(ax, 22, 9.5, 2.4, 'resultat'); text(ax, 28, 9.5, 'neutre', 'resultat', 's', ha='left')
disc(ax, 50, 9.5, 2.4, 'resultat'); text(ax, 56, 9.5, 'demi-tour', 'resultat', 's', ha='left')
save(fig, '49-189')
