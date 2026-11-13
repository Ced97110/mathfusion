import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$p = q = 5$, $n = 25$', 'encre', 'l')
cw, g = 6.4, 0.6
for k in range(24):
    v = k + 1
    r, c = divmod(k, 12)
    box(ax, 2.3 + c * (cw + g), 56 - r * (cw + g), cw, cw, 'varie' if v % 5 == 0 else 'sujet', r=0.3)
box(ax, 4, 42, 4.5, 4.5, 'varie', r=0.3)
text(ax, 11, 44.3, '4 multiples de 5 : retirés', 'varie', 's', ha='left')
box(ax, 4, 35, 4.5, 4.5, 'sujet', r=0.3)
text(ax, 11, 37.3, '20 nombres restent', 'sujet', 's', ha='left')
text(ax, 22, 26, 'nombre réel', 'resultat', 's')
text(ax, 66, 26, 'formule', 'limite', 's')
box(ax, 3, 11, 38, 12, 'resultat', label=r'$\varphi(25) = 20$')
text(ax, 44, 17, r'$\neq$', 'encre', 'l')
box(ax, 47, 11, 38, 12, 'limite', label=r'$(5-1)(5-1) = 16$')
save(fig, '53-085')
