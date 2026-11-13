import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
H = 20
rows = [(64, 'sujet', r'$\nu$ définie sur $D\setminus\{0\}$', 'le polynôme nul n’a pas de taille', r'$\nu=$ degré'),
        (37, 'varie', r'$\nu(a)\leq\nu(ab)$', r'$\nu(x)=1\leq\nu(x\cdot x)=2$', 'multiplier ne réduit pas'),
        (10, 'resultat', r'$r=0$ ou $\nu(r)<\nu(b)$', r'$x^2+1=x\cdot x+1$ : $0<1$', 'reste nul ou plus petit que $b$')]
for y, role, head, ex, note in rows:
    box(ax, 4, y, 80, H, role)
    text(ax, 8, y + 15.5, head, role, 'm', ha='left', weight='bold')
    text(ax, 8, y + 9, ex, role, 's', ha='left')
    text(ax, 8, y + 3.6, note, 'fixe', 's', ha='left')
# the same size nu links the three conditions
for ytop, ybot in [(64, 57), (37, 30)]:
    arrow(ax, (14, ytop), (14, ybot), 'fixe')
    text(ax, 17, (ytop + ybot) / 2, r'même $\nu$', 'fixe', 's', ha='left')
save(fig, '56-134')
