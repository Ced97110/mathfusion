import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
steps = [(r'$(g_1g_2)\,x\,(g_1g_2)^{-1}$', 'sujet', 'départ', 58),
         (r'$(g_1g_2)^{-1}=g_2^{-1}g_1^{-1}$', 'varie', 'étape clé : ordre contraire', 32),
         (r'$g_1\,(g_2\,x\,g_2^{-1})\,g_1^{-1}$', 'resultat', 'arrivée', 6)]
for s, role, lab, y in steps:
    box(ax, 6, y, 76, 12, role, label=s, size='m')
    text(ax, 44, y + 16, lab, role, 's')
arrow(ax, (12, 57), (12, 45), 'encre')
arrow(ax, (12, 31), (12, 19), 'encre')
save(fig, '49-117')
