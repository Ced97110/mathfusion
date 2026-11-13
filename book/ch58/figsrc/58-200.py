import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# transposé : les images (2, 1) et (4, 3) passent des colonnes aux lignes
cw, ch = 9, 8
def mat(x, y, vals, title):
    text(ax, x + 9.75, 44, title, 'encre', 's', weight='bold')
    for j in range(2):
        for i in range(2):
            role = 'sujet' if (vals[j][i][1] == 0) else 'varie'
            box(ax, x + i * 10.5, y + 10 - j * 9.5 + 9, cw, ch, role, label=vals[j][i][0], size='m', r=0.5)
# cellules : (texte, numéro de l'image) ; l'image 0 est (2, 1), l'image 1 est (4, 3)
livre = [[('2', 0), ('4', 1)], [('1', 0), ('3', 1)]]
jacob = [[('2', 0), ('1', 0)], [('4', 1), ('3', 1)]]
mat(4, 6, livre, 'le livre')
mat(63, 6, jacob, 'Jacobson')
arrow(ax, (31, 24.3), (60, 24.3), 'varie', lw=1.4)
text(ax, 45.5, 30, 'transposé :', 'varie', 's')
text(ax, 45.5, 18.5, 'lignes ↔ colonnes', 'varie', 's')
text(ax, 4, 6, 'bleu : image de $e_1$ = (2, 1)', 'sujet', 's', ha='left')
text(ax, 46, 6, 'orange : image de $e_2$ = (4, 3)', 'varie', 's', ha='left')
save(fig, '58-200')
