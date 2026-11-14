import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 14, 52, 60, 24, 'sujet')
text(ax, 44, 71, 'théorème sur les modules', 'sujet', 'm', weight='bold')
text(ax, 44, 65, 'quotient par le noyau ≅ image', 'sujet', 's')
items = [('groupe abélien', 'R = ℤ', r'$(x\,;\,y)\mapsto x-2y$', 'sujet'),
         ('espace vectoriel', 'R = corps', r'$(p\,;\,q)\mapsto p$', 'autre'),
         ('transf. linéaire', 'R = polynômes', 'x : quart de tour', 'varie')]
for i, (a, b, c, role) in enumerate(items):
    x = 2 + i * 29
    box(ax, x, 6, 26, 34, role)
    text(ax, x + 13, 34, a, role, 's', weight='bold')
    text(ax, x + 13, 26, b, role, 's')
    text(ax, x + 13, 15, c, role, 's')
    arrow(ax, (44 + (i - 1) * 16, 51.5), (x + 13, 40.5), 'resultat', lw=1.2)
text(ax, 44, 58, 'vrai sans autre preuve', 'resultat', 's')
save(fig, '57-179')
