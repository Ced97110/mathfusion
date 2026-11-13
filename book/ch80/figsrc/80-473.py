import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
def venn(cx, mode):
    r = 10; ya = 34
    p1 = Circle((cx - 6, ya), r, ec=COL['sujet'], fc=FILL['sujet'] if mode == 'u' else 'none', lw=0.9, zorder=2)
    p2 = Circle((cx + 6, ya), r, ec=COL['autre'], fc=FILL['autre'] if mode == 'u' else 'none', lw=0.9, zorder=2)
    ax.add_patch(p1); ax.add_patch(p2)
    if mode == 'i':
        c = Circle((cx + 6, ya), r, ec='none', fc=FILL['resultat'], zorder=2.5); ax.add_patch(c); c.set_clip_path(p1)
        ax.add_patch(Circle((cx - 6, ya), r, ec=COL['sujet'], fc='none', lw=0.9, zorder=3))
        ax.add_patch(Circle((cx + 6, ya), r, ec=COL['autre'], fc='none', lw=0.9, zorder=3))
    else:
        c = Circle((cx + 6, ya), r, ec='none', fc=FILL['resultat'], zorder=2.5); ax.add_patch(c); c.set_clip_path(p1)
        ax.add_patch(Circle((cx - 6, ya), r, ec=COL['sujet'], fc='none', lw=0.9, zorder=3))
        ax.add_patch(Circle((cx + 6, ya), r, ec=COL['autre'], fc='none', lw=0.9, zorder=3))
    text(ax, cx - 10, ya, r'$a$', 'sujet', 'm'); text(ax, cx + 10, ya, r'$b$', 'autre', 'm')
venn(21, 'i'); venn(67, 'u')
text(ax, 44, 57, 'positions où chacun est fermé', 'encre', 's')
text(ax, 21, 14, 'série : partage commun', 'resultat', 's'); text(ax, 67, 14, 'parallèle : réunion', 'resultat', 's')
text(ax, 21, 8, r'$a\wedge b$ : les deux', 'fixe', 's'); text(ax, 67, 8, r"$a\vee b$ : l'un des deux", 'fixe', 's')
save(fig, '80-473')
