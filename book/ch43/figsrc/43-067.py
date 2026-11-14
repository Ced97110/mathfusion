import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'la classe $[(3,\,4)]$ dépend de la relation', 'encre', 'm')
s = 2.8
for cx, role, lab in [(22, 'sujet', "même distance à l'origine"), (66, 'autre', 'même abscisse')]:
    cy = 38
    line(ax, [(cx - 18, cy), (cx + 18, cy)], 'fixe', lw=0.6); line(ax, [(cx, cy - 20), (cx, cy + 20)], 'fixe', lw=0.6)
    if role == 'sujet':
        ax.add_patch(Circle((cx, cy), 5 * s, ec=COL[role], fc='none', lw=1.4, zorder=3))
        text(ax, cx, cy - 20 + 2.5, 'cercle de rayon 5', role, 's') if False else None
        text(ax, cx, 14, 'cercle de rayon 5', role, 's')
    else:
        line(ax, [(cx + 3 * s, cy - 19), (cx + 3 * s, cy + 19)], role, lw=1.4)
        text(ax, cx, 14, 'droite verticale', role, 's')
    disc(ax, cx + 3 * s, cy + 4 * s, 1.3, 'varie')
    text(ax, cx + 3 * s + 2.2, cy + 4 * s + 2.5, r'$(3,\,4)$', 'varie', 's', ha='left')
    text(ax, cx, 62, lab, role, 's')
    text(ax, cx, 8, '', role, 's')
save(fig, '43-067')
