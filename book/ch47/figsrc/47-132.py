import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, r'départ : $g^{-1}ng\in N$ pour tout $g$', 'encre', 'm')
# row A
def nested(y, big, small, role_b, role_s, cap):
    box(ax, 12, y, 34, 17, role_b, fill=True)
    text(ax, 16, y + 13, big, role_b, 'm', ha='left')
    box(ax, 22, y + 2.5, 20, 8, role_s, label=small)
    text(ax, 66, y + 8.5, cap, role_s, 'm')
nested(54, r'$gN$', r'$Ng$', 'sujet', 'autre', r'avec $g$')
nested(29, r'$Ng$', r'$gN$', 'autre', 'sujet', r'avec $g^{-1}$')
text(ax, 66, 51, '', 'encre', 's')
arrow(ax, (44, 27), (44, 21), 'resultat')
box(ax, 12, 6, 24, 9, 'sujet', label=r'$gN$')
text(ax, 44, 10.5, '=', 'resultat', 'l', weight='bold')
box(ax, 52, 6, 24, 9, 'autre', label=r'$Ng$')
text(ax, 44, 79, r'étape qui porte : remplacer $g$ par $g^{-1}$', 'varie', 's')
save(fig, '47-132')
