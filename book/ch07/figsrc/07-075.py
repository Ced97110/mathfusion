import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
cw = 6
# planches
text(ax, 3, 82, 'planches (pouces)', 'fixe', 's', ha='left', weight='bold')
for i in range(5): box(ax, 6 + i * cw, 70, cw, 8, 'sujet' if i < 3 else 'autre', r=0.2)
text(ax, 64, 74, r'$\frac{3}{8} + \frac{1}{4} = \frac{5}{8}$', 'resultat', 'm')
# resistances
text(ax, 3, 58, 'résistances en série', 'fixe', 's', ha='left', weight='bold')
line(ax, [(2, 47), (6, 47)], 'fixe'); line(ax, [(34, 47), (38, 47)], 'fixe')
box(ax, 6, 42, 14, 10, 'sujet', label=r'$R_1$'); box(ax, 20, 42, 14, 10, 'autre', label=r'$R_2$')
text(ax, 64, 47, r'$R_1 + R_2$', 'resultat', 'm')
# heritage
text(ax, 3, 32, 'héritage (parts)', 'fixe', 's', ha='left', weight='bold')
for i in range(6): box(ax, 6 + i * cw, 18, cw, 8, 'sujet' if i < 3 else ('autre' if i < 5 else 'fixe'), fill=i < 5, r=0.2)
text(ax, 64, 22, r'$\frac{1}{2} + \frac{1}{3} = \frac{5}{6}$', 'resultat', 'm')
text(ax, 44, 6, 'on additionne des mesures', 'varie', 's')
save(fig, '07-075')
