import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, 'Les 55 cases de 0 à 54', 'encre', 'm')
s, x0, y0 = 6.4, 8.8, 50
cnt = dict(sujet=0, varie=0, autre=0, resultat=0)
for k in range(55):
    r, c = divmod(k, 11)
    m5, m11 = k % 5 == 0, k % 11 == 0
    role = 'autre' if (m5 and m11) else 'sujet' if m5 else 'varie' if m11 else 'resultat'
    cnt[role] += 1
    box(ax, x0 + c * s, y0 - r * s, s - 0.6, s - 0.6, role, r=0.2, lw=0.5)
assert cnt == dict(sujet=10, varie=4, autre=1, resultat=40)
box(ax, 6, 3, 6, 5, 'sujet'); text(ax, 14, 5.5, 'multiples de 5 (11)', 'sujet', 's', ha='left')
box(ax, 46, 3, 6, 5, 'varie'); text(ax, 54, 5.5, 'multiples de 11 (5)', 'varie', 's', ha='left')
box(ax, 6, 11, 6, 5, 'autre'); text(ax, 14, 13.5, 'case 0 : dans les deux listes', 'autre', 's', ha='left')
box(ax, 6, 19, 6, 5, 'resultat'); text(ax, 14, 21.5, '40 cases restent', 'resultat', 's', ha='left')
save(fig, '53-108')
