import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
f = lambda v: 26 + v * 4.6
def block(ytitle, title, a, b):
    text(ax, 2, ytitle, title, 'encre', 's', ha='left', weight='bold')
    ys = (ytitle - 7, ytitle - 13, ytitle - 19)
    text(ax, 2, ys[0], f'multiples de {a}', 'sujet', 's', ha='left')
    text(ax, 2, ys[1], f'multiples de {b}', 'autre', 's', ha='left')
    text(ax, 2, ys[2], 'les deux', 'resultat', 's', ha='left')
    both = [v for v in range(13) if v % a == 0 and v % b == 0]
    for v in range(0, 13, a): disc(ax, f(v), ys[0], 1.4, 'sujet')
    for v in range(0, 13, b): disc(ax, f(v), ys[1], 1.4, 'autre')
    for v in both: disc(ax, f(v), ys[2], 2.1 if v else 1.4, 'resultat')
    for v in (0, 6, 12): text(ax, f(v), ys[2] - 4.5, str(v), 'fixe', 's')
block(63, '4 et 3 : commun dès 12', 4, 3); block(30, '2 et 6 : commun dès 6', 2, 6)
save(fig, '60-025')
