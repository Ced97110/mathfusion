import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'$(1+x)\,m_3(x) = 1 + x^5$', 'sujet', 'l', weight='bold')
text(ax, 44, 64, 'une case par puissance de $x$ : 0 à 5', 'fixe', 's')
cw, x0 = 9, 30
rows = [(54, '111110', r'$m_3$', 'sujet'), (45, '011111', r'$x \cdot m_3$', 'varie'), (36, '100001', 'somme', 'resultat')]
for y, s, lab, role in rows:
    text(ax, 3, y + 3, lab, role, 'm', ha='left')
    for i, c in enumerate(s):
        box(ax, x0 + i * cw, y, cw - 0.8, 6.2, role if c == '1' else 'fixe', label=c, size='m', r=0.4)
text(ax, 44, 27, r'pour $x = \omega^3$ : $x^5 = \omega^{15} = 1$', 'encre', 's')
text(ax, 44, 19.5, r'$1 + 1 = 0$ et $1 + \omega^3 \neq 0$', 'encre', 's')
box(ax, 22, 4, 44, 10, 'resultat', label=r'$m_3(\omega^3) = 0$', size='l', weight='bold')
save(fig, '68-211')
