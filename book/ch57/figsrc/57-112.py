import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, '$a$ = 3 dans ℤ', 'encre', 'm')
def panel(x0, role, head, rule, arrow_lab, note):
    xc = x0 + 20
    box(ax, x0, 8, 40, 44, role, fill=True)
    text(ax, xc, 46, head, role, 'l')
    text(ax, xc, 38, rule, role, 's')
    box(ax, x0 + 4, 20, 11, 10, role, label='5', size='s')
    arrow(ax, (x0 + 16, 25), (x0 + 25, 25), role)
    text(ax, xc, 29.5, arrow_lab, role, 's')
    box(ax, x0 + 26, 20, 11, 10, 'resultat', label='15', size='s')
    text(ax, xc, 13, note, role, 's')
panel(2, 'autre', '$a_L$', '$x$ ↦ $ax$', '3·5', 'écrit à gauche')
panel(46, 'sujet', '$a_R$', '$x$ ↦ $xa$', '5·3', 'écrit à droite')
text(ax, 44, 3, 'deux règles, même résultat', 'fixe', 's')
save(fig, '57-112')
