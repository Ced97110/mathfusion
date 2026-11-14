import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$f=x^3-3x+1$', 'sujet', 'm')
labs = [r'$f_0$', r'$f_1$', r'$f_2$', r'$f_3=9/4$']
for k, lab in enumerate(labs):
    box(ax, 2 + 22 * k, 48, 18, 10, 'resultat' if k == 3 else 'sujet', label=lab)
arrow(ax, (77, 48), (77, 38.5), 'resultat')
box(ax, 36, 29, 50, 9, 'resultat', label=r'constante : pas de racine multiple', size='s')
text(ax, 44, 22, r'$f=x^3-3x+2$', 'autre', 'm')
for k, lab in enumerate([r'$f_0$', r'$f_1$']):
    box(ax, 2 + 22 * k, 6, 18, 10, 'autre', label=lab)
box(ax, 46, 6, 24, 10, 'autre', label=r'$f_2=2x-2$')
text(ax, 72, 11, 'non\nconstant', 'autre', 's', ha='left')
save(fig, '69-086')
