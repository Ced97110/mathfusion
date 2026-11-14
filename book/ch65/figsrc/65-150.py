import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# haut : la méthode à la main
box(ax, 2, 44, 84, 46, 'fixe')
text(ax, 44, 85, r'à la main : signe de $f$ en $-2$ à $2$', 'fixe', 's', weight='bold')
signs = ['−', '+', '+', '−', '+']
for i, s in enumerate(signs):
    x = 8 + i * 16
    box(ax, x, 66, 12, 11, 'varie' if s == '−' else 'sujet', label=s, size='l')
for i in (0, 2, 3):
    xm = 8 + i * 16 + 14
    line(ax, [(xm, 63), (xm, 80)], 'resultat', lw=1.4, dash=True)
text(ax, 44, 58, '3 changements de signe', 'resultat', 's')
text(ax, 44, 49, 'dérivée : 2 changements\nde direction', 'encre', 's')
# bas : Sturm
arrow(ax, (44, 43), (44, 29), 'varie', lw=1.2)
text(ax, 48, 36, 'remplacé par', 'varie', 's', ha='left')
box(ax, 2, 4, 84, 24, 'autre', dash=True, fill=False, label='Sturm (ch. 69) : compte\nexactement les racines réelles', size='s', weight='bold')
save(fig, '65-150')
