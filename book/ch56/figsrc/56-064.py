import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$xy=f\,g$ : $\deg f+\deg g=2$', 'encre', 'm')
rows = [(46, 0, 2, 'sujet', 'autre', 'f constante', 'resultat'),
        (28, 2, 0, 'sujet', 'autre', 'g constante', 'resultat'),
        (10, 1, 1, 'limite', 'limite', 'degré 1 : hors de $R$', 'limite')]
for y, df, dg, rf, rg, com, rc in rows:
    box(ax, 3, y, 27, 11, rf, label=rf'$f$ : degré {df}')
    box(ax, 32, y, 27, 11, rg, label=rf'$g$ : degré {dg}')
    text(ax, 61, y + 5.5, com.replace('f constante', '$f$ constante').replace('g constante', '$g$ constante'), rc, 's', ha='left')
save(fig, '56-064')
