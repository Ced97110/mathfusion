import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, r'$K=\ker\eta$ : multiples de 12', 'sujet', 'l')
text(ax, 44, 43.5, 'tous envoyés sur l’heure 0', 'fixe', 's')
f = numberline(ax, 8, 80, 26, -24, 36, step=12, arrow_right=False, role='fixe', size='m')
for v in range(-24, 37, 12):
    disc(ax, f(v), 26, 1.9, 'sujet')
brace(ax, f(0), f(12), 29, 'varie', label=r'$f_1=12$', down=False)
text(ax, 44, 8, r'tout point $=k\times12$, un seul $k$', 'encre', 's')
save(fig, '59-036')
