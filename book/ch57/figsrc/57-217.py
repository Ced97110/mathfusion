import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# panneau 1 : somme directe
line(ax, [(6, 78), (38, 78)], 'sujet', lw=1.6)
line(ax, [(22, 60), (22, 95)], 'varie', lw=1.6)
line(ax, [(31, 78), (31, 90)], 'fixe', dash=True)
line(ax, [(22, 90), (31, 90)], 'fixe', dash=True)
disc(ax, 22, 78, 2.2, 'resultat', fill=False, lw=1.3)
disc(ax, 31, 90, 1.2, 'fixe')
text(ax, 33, 92.5, '(3 ; 5)', 'fixe', 's', ha='left')
text(ax, 65, 94, r'$M_1$ : multiples de (1 ; 0)', 'sujet', 's')
text(ax, 65, 88, r'$M_2$ : multiples de (0 ; 1)', 'varie', 's')
text(ax, 65, 80, 'intersection : (0 ; 0)', 'resultat', 's')
text(ax, 65, 73, '(3;5) = (3;0) + (0;5)', 'encre', 's')
text(ax, 65, 67, 'une seule écriture', 'resultat', 's', weight='bold')
line(ax, [(2, 55), (86, 55)], 'fixe', lw=0.5)
# panneau 2 : somme non directe
for k in range(6):
    x = 8 + 5.4 * k
    disc(ax, x, 30, 1.3, 'sujet')
    if k % 2 == 0:
        disc(ax, x, 30, 2.4, 'autre', fill=False, lw=1.0)
disc(ax, 8 + 5.4 * 2, 30, 3.4, 'limite', fill=False, lw=1.3)
text(ax, 8 + 5.4 * 2, 23, '(2 ; 0)', 'limite', 's')
text(ax, 65, 46, r'$N_1$ : multiples de (1 ; 0)', 'sujet', 's')
text(ax, 65, 40, r'$N_2$ : multiples de (2 ; 0)', 'autre', 's')
text(ax, 65, 33, '(2 ; 0) est dans les deux', 'limite', 's')
text(ax, 65, 26, '(2;0) = (2;0) + (0;0)', 'encre', 's')
text(ax, 65, 20, '(2;0) = (0;0) + (2;0)', 'encre', 's')
text(ax, 65, 13, 'deux écritures', 'limite', 's', weight='bold')
save(fig, '57-217')
