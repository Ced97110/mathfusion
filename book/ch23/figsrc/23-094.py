import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(80)
bx = [(68, 'sujet', '64 − 16t² = 0'), (54, 'fixe', '16t² = 64'), (40, 'fixe', 't² = 4'), (26, 'varie', 't = 2 ou t = −2')]
for y, r, s in bx: box(ax, 4, y, 40, 9, r, label=s, size='s')
for (y, r, s), lab in zip(bx[:3], ('+ 16t² des deux côtés, ÷ 16', 'racine : deux réponses', 'on lit les réponses')):
    arrow(ax, (24, y), (24, y - 5), 'fixe')
text(ax, 48, 63.5, '+ 16t², puis ÷ 16', 'fixe', 's', ha='left')
text(ax, 48, 49.5, 'racine carrée', 'fixe', 's', ha='left')
text(ax, 48, 35.5, 'deux réponses', 'fixe', 's', ha='left')
arrow(ax, (14, 26), (14, 18), 'fixe'); arrow(ax, (34, 26), (34, 18), 'fixe')
box(ax, 4, 6, 20, 11, 'resultat', label='t = 2 s', size='s')
box(ax, 26, 6, 26, 11, 'fixe', label='−2 écarté', size='s')
text(ax, 44, 75, r'$64-16t^2=0$ : au sol', 'encre', 's') if False else None
save(fig, '23-094')
