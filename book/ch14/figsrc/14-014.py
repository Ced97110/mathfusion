import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
s, g = 4.6, 1.0
def sq(y, role, n=8, fill=True, dash=False):
    for i in range(n): box(ax, 4 + i * (s + g), y, s, s, role, fill=fill, dash=dash, r=0.4)
text(ax, 4, 65, r'départ : $2^{3}=8$', 'sujet', 'm', ha='left')
sq(57, 'sujet')
# vrai
text(ax, 4, 49, r'vrai : $8\times2^{0}=8\times1=8$', 'resultat', 's', ha='left')
sq(41, 'resultat')
text(ax, 84, 43.3, 'vrai', 'resultat', 'm', ha='right', weight='bold')
# faux
text(ax, 4, 31, r'faux : $8\times0=0$', 'limite', 's', ha='left')
sq(23, 'limite', fill=False, dash=True)
line(ax, [(3, 21.5), (4 + 8 * (s + g), 28.5)], 'limite', lw=1.4)
line(ax, [(3, 28.5), (4 + 8 * (s + g), 21.5)], 'limite', lw=1.4)
text(ax, 84, 25.3, 'faux', 'limite', 'm', ha='right', weight='bold')
text(ax, 44, 11, r'$2^{0}=1$ garde 8', 'resultat', 'm')
text(ax, 44, 4.5, r'$2^{0}=0$ casse la règle', 'limite', 's')
save(fig, '14-014')
