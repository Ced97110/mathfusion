import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def word(x, y, w, rl, s=5):
    for i, ch in enumerate(w): box(ax, x + i * s, y, s, s, rl, label=ch, size='m', r=0.5)
def case(y, a, b, res):
    word(4, y, a, 'sujet'); text(ax, 19.5, y + 2.5, 'puis', 'encre', 's'); word(26, y, b, 'autre')
    arrow(ax, (38, y + 2.5), (45, y + 2.5), 'varie'); 
    for i, ch in enumerate(res): box(ax, 48 + i * 5, y, 5, 5, 'sujet' if i < 2 else 'autre', label=ch, size='m', r=0.5)
case(56, 'ab', 'ba', 'abba'); case(44, 'ba', 'ab', 'baab')
box(ax, 48, 33, 20, 6, 'limite', label='≠', size='l')
text(ax, 44, 64, 'les mots : l’ordre compte', 'limite', 's')
text(ax, 44, 22, r'$2+3=3+2$', 'resultat', 'l')
text(ax, 44, 14, 'entiers : l’ordre ne compte pas', 'resultat', 's')
save(fig, '44-078')
