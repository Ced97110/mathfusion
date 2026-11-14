'use client';
// Carte vue de dessus, en milles nautiques. Origine = départ, x vers l'est, y vers le nord.
// Boîtes grises : aucun décor. Couleurs du livre : bleu = avion (vecteur air), violet = vent,
// vert = vecteur sol et trace réelle, orange = le cap réglé, gris = ce qui ne change pas.
import { AVION_KT, DISTANCE_SEUIL_NM, VENT } from '../../../lib/niveau_vent.js';

const K = 4; // pixels par mille nautique
const XMIN = -8;
const XMAX = 146;
const YMIN = -38;
const YMAX = 32;
export const LARGEUR = (XMAX - XMIN) * K;
export const HAUTEUR = (YMAX - YMIN) * K;
export const X = (est) => (est - XMIN) * K;
export const Y = (nord) => (YMAX - nord) * K;

/** Convertit un point écran en milles nautiques. */
export function pointCarte(svg, clientX, clientY) {
  const pt = svg.createSVGPoint();
  pt.x = clientX;
  pt.y = clientY;
  const p = pt.matrixTransform(svg.getScreenCTM().inverse());
  return { estNm: p.x / K + XMIN, nordNm: YMAX - p.y / K };
}

// Coordonnées arrondies au centième : le serveur et le navigateur doivent écrire le même texte (hydratation).
const r2 = (v) => Math.round(v * 100) / 100;
const rad = (d) => (d * Math.PI) / 180;
const VERS = rad(VENT.vientDuDeg + 180);
// Flèches de vent à l'échelle : longueur = distance parcourue par l'air en une heure.
const VENT_DX = r2(VENT.vitesseKt * Math.sin(VERS) * K);
const VENT_DY = r2(-VENT.vitesseKt * Math.cos(VERS) * K);
const POINTS_VENT = [
  [10, 22],
  [50, 22],
  [90, 22],
  [30, -26],
  [70, -26],
  [110, -26],
];

function Fleche({ x1, y1, x2, y2, couleur, epaisseur = 3, pointilles }) {
  const a = Math.atan2(y2 - y1, x2 - x1);
  const t = 9;
  const p1 = `${r2(x2 - t * Math.cos(a - 0.4))},${r2(y2 - t * Math.sin(a - 0.4))}`;
  const p2 = `${r2(x2 - t * Math.cos(a + 0.4))},${r2(y2 - t * Math.sin(a + 0.4))}`;
  return (
    <g>
      <line x1={r2(x1)} y1={r2(y1)} x2={r2(x2)} y2={r2(y2)} stroke={couleur} strokeWidth={epaisseur} strokeDasharray={pointilles ? '6 5' : undefined} />
      <polygon points={`${r2(x2)},${r2(y2)} ${p1} ${p2}`} fill={couleur} />
    </g>
  );
}

/**
 * @param {{ phase: string, cap: number, prediction: {estNm:number,nordNm:number}|null,
 *   resultat: any, triangle: any, onTap: (p:{estNm:number,nordNm:number}) => void,
 *   refs: { svgRef: any, avionRef: any, traceRef: any } }} props
 */
export default function Carte({ phase, cap, prediction, resultat, triangle, onTap, refs }) {
  const { svgRef, avionRef, traceRef } = refs;
  const choisir = phase === 'choisir';
  const xs = X(DISTANCE_SEUIL_NM);

  function tap(e) {
    if (!choisir || !svgRef.current) return;
    onTap(pointCarte(svgRef.current, e.clientX, e.clientY));
  }

  return (
    <svg
      ref={svgRef}
      className={`nv-carte${choisir ? ' nv-tap' : ''}`}
      viewBox={`0 0 ${LARGEUR} ${HAUTEUR}`}
      role="img"
      aria-label="Carte vue de dessus : départ à l'ouest, piste à l'est, vent qui pousse vers le sud-est"
      onPointerUp={tap}
    >
      <rect x="0" y="0" width={LARGEUR} height={HAUTEUR} fill="#fff" />
      {/* nord */}
      <g fill="var(--gris)" stroke="var(--gris)">
        <line x1={LARGEUR - 22} y1="44" x2={LARGEUR - 22} y2="16" strokeWidth="2" />
        <polygon points={`${LARGEUR - 22},8 ${LARGEUR - 28},20 ${LARGEUR - 16},20`} stroke="none" />
        <text x={LARGEUR - 22} y="60" textAnchor="middle" fontSize="13" stroke="none">N</text>
      </g>
      {/* vent, à l'échelle */}
      {POINTS_VENT.map(([e, n]) => (
        <Fleche key={`${e}${n}`} x1={X(e)} y1={Y(n)} x2={X(e) + VENT_DX} y2={Y(n) + VENT_DY} couleur="var(--violet)" epaisseur={2.5} />
      ))}
      <text x={X(10)} y={Y(22) - 10} fontSize="12" fill="var(--violet)">vent 18,5 kt, vient du 316°</text>
      {/* axe voulu et piste (symbole, non à l'échelle) */}
      <line x1={X(0)} y1={Y(0)} x2={xs} y2={Y(0)} stroke="var(--gris)" strokeWidth="1.2" strokeDasharray="4 6" />
      <rect x={xs - 2} y={Y(0) - 5} width="34" height="10" fill="var(--gris)" />
      <text x={xs + 15} y={Y(0) - 12} textAnchor="middle" fontSize="12" fill="var(--gris)">piste</text>
      <circle cx={X(0)} cy={Y(0)} r="5" fill="var(--encre)" />
      <text x={X(0) - 6} y={Y(0) - 12} fontSize="12" fill="var(--encre)">départ</text>

      {/* cap réglé : où irait l'avion en une heure sans vent */}
      {choisir && (
        <Fleche
          x1={X(0)}
          y1={Y(0)}
          x2={r2(X(AVION_KT * Math.sin(rad(cap))))}
          y2={r2(Y(AVION_KT * Math.cos(rad(cap))))}
          couleur="var(--orange)"
          epaisseur={2}
          pointilles
        />
      )}

      {/* triangle d'une heure de vol : bleu + violet = vert */}
      {phase === 'bilan' && triangle && (
        <g>
          <Fleche x1={X(0)} y1={Y(0)} x2={X(triangle.air.estNm)} y2={Y(triangle.air.nordNm)} couleur="var(--bleu)" />
          <Fleche
            x1={X(triangle.air.estNm)}
            y1={Y(triangle.air.nordNm)}
            x2={X(triangle.sol.estNm)}
            y2={Y(triangle.sol.nordNm)}
            couleur="var(--violet)"
          />
          <Fleche x1={X(0)} y1={Y(0)} x2={X(triangle.sol.estNm)} y2={Y(triangle.sol.nordNm)} couleur="var(--vert)" />
        </g>
      )}

      {/* prédiction du joueur */}
      {prediction && (
        <g stroke="var(--encre)" strokeWidth="2" fill="none">
          <circle cx={X(prediction.estNm)} cy={Y(prediction.nordNm)} r="7" />
          <line x1={X(prediction.estNm) - 11} y1={Y(prediction.nordNm)} x2={X(prediction.estNm) + 11} y2={Y(prediction.nordNm)} />
          <line x1={X(prediction.estNm)} y1={Y(prediction.nordNm) - 11} x2={X(prediction.estNm)} y2={Y(prediction.nordNm) + 11} />
        </g>
      )}

      {/* trace réelle (mise à jour image par image hors de React) */}
      <polyline ref={traceRef} points="" fill="none" stroke="var(--vert)" strokeWidth="2.5" />
      {resultat && phase === 'bilan' && Number.isFinite(resultat.heures) && (
        <circle cx={X(resultat.arrivee.estNm)} cy={Y(resultat.arrivee.nordNm)} r="5" fill="var(--vert)" />
      )}

      {/* avion : le nez suit le cap, pas la trace */}
      <g ref={avionRef} transform={`translate(${X(0)} ${Y(0)}) rotate(${cap})`}>
        <polygon points="0,-12 7,8 0,4 -7,8" fill="var(--bleu)" />
      </g>
    </svg>
  );
}
