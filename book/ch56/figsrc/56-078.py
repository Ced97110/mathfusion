import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
y = 34
toks = [(12, '(', 'encre'), (20, '12', 'sujet'), (27, ',', 'encre'), (35, '18', 'autre'), (43, ')', 'encre'),
        (52, '=', 'encre'), (61, '6', 'resultat')]
for x, t, role in toks:
    text(ax, x, y, t, role, 'xl', weight='bold')
text(ax, 20, 45, '$a$', 'sujet', 'm')
text(ax, 35, 45, '$b$', 'autre', 'm')
brace(ax, 10, 45, 29, 'fixe', label='PGCD de 12 et de 18')
text(ax, 61, 26, 'le PGCD', 'resultat', 's')
text(ax, 44, 7, "pas un point du plan", 'limite', 's')
save(fig, '56-078')
