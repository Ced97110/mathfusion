import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [(26, None, None, 0), (44, 'constante', 0, 1), (62, 'degré 1', 1, 2), (80, 'degré 2', 2, 3)]
yn, yd = 38, 12
text(ax, 4, yn, r'Judson $\nu$', 'sujet', 's', ha='left')
text(ax, 4, yd, r'Jacobson $\delta$', 'resultat', 's', ha='left')
for x, name, nu, de in cols:
    if name:
        text(ax, x, 54, name, 'fixe', 's')
    if nu is None:
        box(ax, x - 6, yn - 4.5, 12, 9, 'fixe', dash=True, fill=False, label='nul :\naucune', size='s')
    else:
        box(ax, x - 6, yn - 4.5, 12, 9, 'sujet', label=str(nu))
    arrow(ax, (x, yn - 5), (x, yd + 6), 'varie', lw=1.0)
    box(ax, x - 6, yd - 4.5, 12, 9, 'resultat', label=str(de))
text(ax, 44, 2.5, r'$\delta=\nu+1$ ; $\delta(0)=0$ posé', 'varie', 's')
save(fig, '56-137')
