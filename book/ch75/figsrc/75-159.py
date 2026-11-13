import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
def col(cx, head, vals, roles):
    text(ax, cx, 56, head, 'encre', 's')
    for k, (v, ro) in enumerate(zip(vals, roles)):
        box(ax, cx - 13 + k * 14, 34, 12, 14, ro, label=v, size='l', weight='bold')
col(15, r'$(1,0)$, $(0,1)$', ['1', '1'], ['resultat', 'resultat'])
col(43, r'$(0,1)$, $(1,0)$', ['1', '1'], ['resultat', 'resultat'])
col(74, r'$(2,0)$, $(0,1)$', ['4', '1'], ['limite', 'resultat'])
text(ax, 29, 64, 'valeurs $\\pm1$', 'resultat', 's', weight='bold'); text(ax, 74, 64, 'une valeur $4$', 'limite', 's', weight='bold')
line(ax, [(58, 12), (58, 60)], 'fixe', dash=True)
brace(ax, 2, 55, 31, 'resultat', label='deux valeurs 1 : même nombre', size='s')
brace(ax, 61, 86, 31, 'varie', label='une seule valeur 1', size='s')
text(ax, 29, 17, 'le nombre de 1 ne change pas', 'resultat', 's')
text(ax, 74, 17, r'$4\neq\pm1$ : il change', 'limite', 's')
save(fig, '75-159')
