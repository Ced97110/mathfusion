import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
k = 2.8; x0 = 6
text(ax, 44, 74, r'$n=2$, $q=5$ : $q^n=25$ vecteurs', 'sujet', 'm')
box(ax, x0, 60, 25 * k, 7, 'sujet', label='25', size='s')
for y, r, lab in ((44, 1, r'$u_1$ : $25-1=24$ choix'), (24, 5, r'$u_2$ : $25-5=20$ choix')):
    text(ax, 44, y + 11, lab, 'varie', 'm')
    box(ax, x0, y, r * k, 7, 'limite', label=str(r), size='s', r=0.4)
    box(ax, x0 + r * k, y, (25 - r) * k, 7, 'resultat', label=str(25 - r), size='s')
text(ax, 44, 7, r'$24\times 20=480$', 'resultat', 'l')
save(fig, '75-110')
