import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(56)
s = 8.0; O = (8, 6)
a, b, R = 3 * s, 4 * s, 5 * s
P = (O[0] + a, O[1] + b); Q = (O[0] + a, O[1])
poly(ax, [O, Q, P], 'sujet')
disc(ax, *O, 9.0 * 0 + 5.0 * 0 + 0.01, 'fixe') if False else None
arc(ax, O, 9.0, 0, 53.13, 'resultat', 1.0)
s2 = 9.0
poly(ax, [O, (O[0] + 0.6 * s2, O[1]), (O[0] + 0.6 * s2, O[1] + 0.8 * s2)], 'resultat')
text(ax, O[0] + a / 2, O[1] - 3, r'$a = 3$', 'sujet', 's')
text(ax, Q[0] + 4.5, O[1] + b / 2, r'$b = 4$', 'sujet', 's')
text(ax, O[0] + a / 2 - 5, O[1] + b / 2 + 3, r'$R = 5$', 'sujet', 's')
text(ax, 48, 46, 'rayon 1 : ', 'resultat', 's', ha='left') if False else None
text(ax, 47, 44, 'même angle', 'varie', 's', ha='left')
text(ax, 47, 36, r'$a/R = 0{,}6 = \cos\theta$', 'resultat', 's', ha='left')
text(ax, 47, 30, r'$b/R = 0{,}8 = \sin\theta$', 'resultat', 's', ha='left')
text(ax, 47, 22, r'$\theta \approx 53{,}13°$', 'varie', 's', ha='left')
text(ax, 47, 14, r'$0{,}6^2 + 0{,}8^2 = 1$', 'resultat', 's', ha='left')
text(ax, 22, 12, r'$\theta$', 'varie', 's')
text(ax, 10.4, 3.2, '0,6', 'resultat', 's'); text(ax, 17, 9.5, '0,8', 'resultat', 's'); text(ax, 7.5, 13, '1', 'resultat', 's')
text(ax, 15.5, 11.5, '1', 'resultat', 's') if False else None
save(fig, '31-149')
