import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cols = [(4, 'sujet', 'Jacobson', 'Cauchy :\ngroupes abéliens', 'appliqué au centre'),
        (48, 'autre', 'Judson', 'Cauchy :\ntous les groupes', 'récurrence refaite\npour $p^r$')]
for x, r, t, s1, s2 in cols:
    text(ax, x + 18, 74, t, r, 'l', weight='bold')
    box(ax, x, 54, 36, 12, r, label=s1, size='s')
    box(ax, x, 33, 36, 12, r, label=s2, size='s')
    arrow(ax, (x + 18, 53.2), (x + 18, 45.8), 'varie')
    arrow(ax, (x + 18, 32.2), (x + 18, 20.8), 'resultat')
box(ax, 4, 8, 80, 12, 'resultat', label='même théorème : Sylow I', size='m')
save(fig, '50-145')
