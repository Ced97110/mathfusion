import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(74)
text(ax, 44, 69, 'message 1001 = 1 + x³ : deux termes', 'sujet', 's')
# chaque terme du message multiplie g = 1101000
a, b = '1101000', '0001101'
c = ''.join(str((int(u) + int(v)) % 2) for u, v in zip(a, b))
assert c == '1100101'
both = [i for i in range(7) if a[i] == '1' and b[i] == '1']
ra = ['varie' if i in both else 'sujet' for i in range(7)]
rb = ['varie' if i in both else 'sujet' for i in range(7)]
rc = ['varie' if i in both else 'resultat' for i in range(7)]
text(ax, 2, 57, r'$1 \times g$', 'sujet', 's', ha='left')
brow(fig, ax, 58, 57, a, roles=ra)
text(ax, 2, 45, r'$+\ x^3 \times g$', 'sujet', 's', ha='left')
brow(fig, ax, 58, 45, b, roles=rb)
line(ax, [(2, 37), (86, 37)], 'fixe')
text(ax, 2, 30, 'mot envoyé', 'resultat', 's', ha='left')
brow(fig, ax, 58, 30, c, roles=rc)
text(ax, 44, 18, 'les deux 1 en x³ s’annulent', 'varie', 's')
text(ax, 44, 10, '1 + 1 = 0', 'varie', 'm')
save(fig, '68-180')
