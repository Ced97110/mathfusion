import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 65, 'Si l’ensemble était vide', 'limite', 's')
box(ax, 4, 28, 36, 30, 'limite', dash=True)
text(ax, 22, 43, 'aucun\n$p$-Sylow', 'limite', 'm')
text(ax, 22, 22, 'impossible', 'limite', 'm', weight='bold')
text(ax, 66, 65, 'Triangle, $p = 2$', 'resultat', 's')
box(ax, 46, 6, 40, 54, 'resultat')
text(ax, 66, 55, 'ensemble des 2-Sylow', 'resultat', 's')
for i, lab in enumerate(['$s_A$', '$s_B$', '$s_C$']):
    y = 38 - i * 14
    box(ax, 52, y, 28, 10, 'sujet', label=r'$\{e,\ %s\}$' % lab.strip('$'), size='m')
text(ax, 66, 3.5, 'pas vide : 3 éléments', 'resultat', 's', weight='bold')
save(fig, '50-066')
