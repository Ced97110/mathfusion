'use client';
// Vue rapprochée du seuil de piste : couloir d'approche de 700 ft (AIM) et point de passage de l'avion.
import { DEMI_LARGEUR_M, formatDistanceM, formatNombre } from '../../../lib/niveau_vent.js';

const ECHELLE_M = 1000; // demi-hauteur de la vue, en mètres
const H = 140;
const L = 280;
const MILIEU = H / 2;
const PX_PAR_M = (H / 2 - 12) / ECHELLE_M;

/** @param {{ ecartM: number }} props  écart positif = au sud de l'axe */
export default function Seuil({ ecartM }) {
  const fini = Number.isFinite(ecartM);
  const hors = !fini || Math.abs(ecartM) > ECHELLE_M;
  const y = fini ? MILIEU + Math.max(-ECHELLE_M, Math.min(ECHELLE_M, ecartM)) * PX_PAR_M : MILIEU;
  const bande = DEMI_LARGEUR_M * PX_PAR_M;
  const cote = ecartM > 0 ? 'au sud' : 'au nord';
  const texte = !fini
    ? "L'avion n'atteint jamais la piste."
    : `${formatDistanceM(ecartM)} ${cote} de l'axe`;

  return (
    <figure className="nv-seuil">
      <svg viewBox={`0 0 ${L} ${H}`} role="img" aria-label={`Passage au seuil : ${texte}`}>
        <rect x="0" y="0" width={L} height={H} fill="#fff" stroke="var(--filet)" />
        <rect x="150" y={MILIEU - bande} width="120" height={2 * bande} fill="var(--gris)" opacity="0.18" />
        <line x1="20" y1={MILIEU} x2={L - 10} y2={MILIEU} stroke="var(--gris)" strokeDasharray="4 5" />
        <line x1="150" y1="8" x2="150" y2={H - 8} stroke="var(--gris)" strokeWidth="2" />
        <text x="158" y={MILIEU - bande - 6} fontSize="11" fill="var(--gris)">couloir 700 ft</text>
        <text x="132" y="18" textAnchor="end" fontSize="11" fill="var(--gris)">nord</text>
        <text x="132" y={H - 8} textAnchor="end" fontSize="11" fill="var(--gris)">sud</text>
        <text x="20" y={H - 8} fontSize="11" fill="var(--gris)">±1 km</text>
        {fini && <circle cx="150" cy={y} r="6" fill={hors ? 'var(--rouge)' : 'var(--vert)'} />}
        {fini && hors && (
          <polygon
            points={ecartM > 0 ? `150,${H - 2} 144,${H - 12} 156,${H - 12}` : `150,2 144,12 156,12`}
            fill="var(--rouge)"
          />
        )}
      </svg>
      <figcaption>Passage au seuil : {texte}. Pour gagner : moins de {formatNombre(DEMI_LARGEUR_M, 0)} m.</figcaption>
    </figure>
  );
}
