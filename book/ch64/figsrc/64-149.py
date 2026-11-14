import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
r, Rr, cy = 2.4, 12, 56
cl, cr = 22, 66

# les deux objets : racines de l'unité (à gauche), horloge à 5 heures (à droite)
def role_of(k):
    return 'varie' if k in (2, 4) else ('resultat' if k == 1 else 'sujet')

ax.add_patch(Circle((cl, cy), Rr, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
ax.add_patch(Circle((cr, cy), Rr, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
for k in range(5):
    a = math.radians(72 * k)               # racines : 0°, 72°, ... dans le sens inverse des aiguilles
    disc(ax, cl + Rr * math.cos(a), cy + Rr * math.sin(a), r, role_of(k))
    text(ax, cl + (Rr + 8) * math.cos(a), cy + (Rr + 6) * math.sin(a), f'{72 * k}°', role_of(k), 's')
    b = math.radians(90 - 72 * k)          # horloge : 0 en haut, sens des aiguilles
    disc(ax, cr + Rr * math.cos(b), cy + Rr * math.sin(b), r, role_of(k))
    text(ax, cr + (Rr + 5.5) * math.cos(b), cy + (Rr + 5) * math.sin(b), str(k), role_of(k), 's')
text(ax, cl, 30, r"racines de 1 : produit", 'sujet', 's')
text(ax, cr, 30, r'$\mathbb{Z}/5$ : somme', 'sujet', 's')
text(ax, 44, 14, "144° + 288° = 432° $\\equiv$ 72°\n2 + 4 = 6 $\\equiv$ 1 (modulo 5)", 'encre', 's')
save(fig, '64-149')
