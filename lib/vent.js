// Calculs du niveau « Vent de travers » (chapitre 41, addition de deux vecteurs).
// Fonctions pures : chaque valeur affichée par le niveau vient d'ici et est testée
// dans lib/vent.test.js. Angles en degrés depuis le nord, sens des aiguilles d'une montre.

const NOEUD_M_S = 1852 / 3600;

/**
 * @typedef {{ vientDuDeg: number, vitesseKt: number }} Vent
 *   Direction météorologique : le côté d'où vient le vent.
 * @typedef {{ estKt: number, nordKt: number, routeDeg: number, vitesseSolKt: number }} Sol
 */

const rad = (d) => (d * Math.PI) / 180;
const deg = (r) => (r * 180) / Math.PI;
const norm360 = (d) => ((d % 360) + 360) % 360;

/** @param {number} v @param {string} nom */
function verifierVitesse(v, nom) {
  if (!Number.isFinite(v) || v < 0) {
    throw new RangeError(`${nom} doit être un nombre fini positif ou nul (reçu ${v})`);
  }
}

/** @param {number} a @param {string} nom */
function verifierAngle(a, nom) {
  if (!Number.isFinite(a)) throw new RangeError(`${nom} doit être un nombre fini (reçu ${a})`);
}

/** @param {Vent} vent */
function verifierVent(vent) {
  verifierAngle(vent.vientDuDeg, "vientDuDeg");
  verifierVitesse(vent.vitesseKt, "vitesseKt");
}

/**
 * @param {number} ms vitesse en m/s
 * @returns {number} vitesse en nœuds (1 kt = 1852 m / 3600 s)
 */
export function noeudsDepuisMs(ms) {
  verifierVitesse(ms, "ms");
  return ms / NOEUD_M_S;
}

/**
 * Composantes du vent par rapport à une route.
 * traversKt < 0 : le vent pousse vers la droite de la route. faceKt < 0 : vent arrière.
 * @param {Vent} vent
 * @param {number} routeDeg
 * @returns {{ traversKt: number, faceKt: number }}
 */
export function composantesVent(vent, routeDeg) {
  verifierVent(vent);
  verifierAngle(routeDeg, "routeDeg");
  const a = rad(vent.vientDuDeg - routeDeg);
  return { traversKt: vent.vitesseKt * Math.sin(a), faceKt: vent.vitesseKt * Math.cos(a) };
}

/**
 * Vecteur sol = vecteur avion (cap, vitesse air) + vecteur vent (vers lequel il pousse).
 * @param {number} tasKt vitesse air
 * @param {number} capDeg
 * @param {Vent} vent
 * @returns {Sol}
 */
export function vecteurSol(tasKt, capDeg, vent) {
  verifierVitesse(tasKt, "tasKt");
  verifierAngle(capDeg, "capDeg");
  verifierVent(vent);
  const vers = rad(vent.vientDuDeg + 180);
  const estKt = tasKt * Math.sin(rad(capDeg)) + vent.vitesseKt * Math.sin(vers);
  const nordKt = tasKt * Math.cos(rad(capDeg)) + vent.vitesseKt * Math.cos(vers);
  return {
    estKt,
    nordKt,
    routeDeg: norm360(deg(Math.atan2(estKt, nordKt))),
    vitesseSolKt: Math.hypot(estKt, nordKt),
  };
}

/**
 * Cap à prendre pour suivre une route (triangle des vents).
 * cap = route + asin(travers / vitesse air). null si le vent de travers dépasse la vitesse air.
 * @param {number} tasKt
 * @param {Vent} vent
 * @param {number} routeDeg
 * @returns {{ capDeg: number, correctionDeg: number, vitesseSolKt: number } | null}
 */
export function capPourRoute(tasKt, vent, routeDeg) {
  verifierVitesse(tasKt, "tasKt");
  const { traversKt } = composantesVent(vent, routeDeg);
  if (Math.abs(traversKt) > tasKt) return null;
  const correctionDeg = deg(Math.asin(traversKt / tasKt));
  const capDeg = norm360(routeDeg + correctionDeg);
  return { capDeg, correctionDeg, vitesseSolKt: vecteurSol(tasKt, capDeg, vent).vitesseSolKt };
}

/**
 * Écart latéral à l'axe de la piste au moment où l'avion a avancé de distanceNm le long de la route voulue.
 * Positif = à droite de l'axe. Vue de dessus, terre plate, vent constant, cap bloqué pendant le vol.
 * @param {number} routeReelleDeg
 * @param {number} routeVoulueDeg
 * @param {number} distanceNm distance le long de l'axe jusqu'au seuil
 * @returns {number} écart en mètres
 */
export function ecartAuSeuilM(routeReelleDeg, routeVoulueDeg, distanceNm) {
  verifierAngle(routeReelleDeg, "routeReelleDeg");
  verifierAngle(routeVoulueDeg, "routeVoulueDeg");
  verifierVitesse(distanceNm, "distanceNm");
  const ecartDeg = ((routeReelleDeg - routeVoulueDeg + 540) % 360) - 180;
  if (Math.abs(ecartDeg) >= 90) return Number.POSITIVE_INFINITY;
  return distanceNm * 1852 * Math.tan(rad(ecartDeg));
}

/**
 * Réponse de la fausse idée « les vitesses s'additionnent ».
 * @param {number} tasKt
 * @param {Vent} vent
 * @returns {number}
 */
export function sommeNaive(tasKt, vent) {
  verifierVitesse(tasKt, "tasKt");
  verifierVent(vent);
  return tasKt + vent.vitesseKt;
}
