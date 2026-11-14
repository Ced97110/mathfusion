// Logique de jeu du niveau « Vent de travers » (chapitre 41). Fonctions pures, testées dans
// lib/niveau_vent.test.js. Repère : origine au départ, x vers l'est, y vers le nord, en milles nautiques.
import data from "../data/vent_travers.json";
import { capPourRoute, ecartAuSeuilM, vecteurSol } from "./vent.js";

const PIED_M = 0.3048;
const MILLE_M = 1852;

/** Vitesse air du Cessna 172S, en nœuds (mesure POH). */
export const AVION_KT = data.avion.vitesse_air_kt;
/** Vent mesuré à De Bilt, converti en nœuds avec la définition exacte du nœud. */
export const VENT = Object.freeze({
  vientDuDeg: data.vent.vient_du_deg,
  vitesseKt: (data.vent.vitesse_m_s * 3600) / MILLE_M,
});
/** Route vers la piste (choix de conception : plein est). */
export const ROUTE_DEG = data.mission.route_voulue_deg;
/** Demi-largeur du couloir d'approche au seuil (AIM : 700 ft au total). */
export const DEMI_LARGEUR_M = (data.tolerance_arrivee.largeur_totale_ft / 2) * PIED_M;
/** Durée de vol jusqu'au seuil avec le bon cap : choix de conception (une heure, comme la question papier). */
export const DUREE_CONCEPTION_H = 1;
/** Distance du départ au seuil le long de l'axe, en milles nautiques. */
export const DISTANCE_SEUIL_NM = capPourRoute(AVION_KT, VENT, ROUTE_DEG).vitesseSolKt * DUREE_CONCEPTION_H;

/**
 * @typedef {{ estNm: number, nordNm: number }} Point
 * @typedef {{ capDeg: number, sol: ReturnType<typeof vecteurSol>, heures: number,
 *   arrivee: Point, ecartSeuilM: number, gagne: boolean }} Resultat
 */

/**
 * Position de l'avion après t heures de vol, cap bloqué.
 * @param {number} capDeg
 * @param {number} heures
 * @returns {Point}
 */
export function positionApresNm(capDeg, heures) {
  const s = vecteurSol(AVION_KT, capDeg, VENT);
  return { estNm: s.estKt * heures, nordNm: s.nordKt * heures };
}

/**
 * Résultat d'une tentative : où et quand l'avion passe la ligne nord-sud du seuil, et s'il gagne.
 * @param {number} capDeg
 * @returns {Resultat}
 */
export function resultatTentative(capDeg) {
  const sol = vecteurSol(AVION_KT, capDeg, VENT);
  if (sol.estKt <= 0) {
    return {
      capDeg,
      sol,
      heures: Number.POSITIVE_INFINITY,
      arrivee: { estNm: Number.NaN, nordNm: Number.NaN },
      ecartSeuilM: Number.POSITIVE_INFINITY,
      gagne: false,
    };
  }
  const heures = DISTANCE_SEUIL_NM / sol.estKt;
  const ecartSeuilM = ecartAuSeuilM(sol.routeDeg, ROUTE_DEG, DISTANCE_SEUIL_NM);
  return {
    capDeg,
    sol,
    heures,
    arrivee: { estNm: DISTANCE_SEUIL_NM, nordNm: sol.nordKt * heures },
    ecartSeuilM,
    gagne: Math.abs(ecartSeuilM) <= DEMI_LARGEUR_M,
  };
}

/**
 * Les trois vecteurs d'une heure de vol : air (bleu), vent (violet), sol (vert).
 * @param {number} capDeg
 * @returns {{ air: Point, vent: Point, sol: Point }}
 */
export function trianglePourCap(capDeg) {
  const c = (capDeg * Math.PI) / 180;
  const v = ((VENT.vientDuDeg + 180) * Math.PI) / 180;
  const air = { estNm: AVION_KT * Math.sin(c), nordNm: AVION_KT * Math.cos(c) };
  const vent = { estNm: VENT.vitesseKt * Math.sin(v), nordNm: VENT.vitesseKt * Math.cos(v) };
  return { air, vent, sol: positionApresNm(capDeg, 1) };
}

/**
 * Enregistrement d'une tentative (format du plan).
 * @param {number} capDeg
 * @param {Point | null} prediction
 * @param {Resultat} r
 * @param {string} horodatage date ISO 8601
 */
export function tentativeJson(capDeg, prediction, r, horodatage) {
  return {
    horodatage,
    cap_deg: capDeg,
    prediction_xy: prediction ? [prediction.estNm, prediction.nordNm] : null,
    arrivee_xy: Number.isFinite(r.heures) ? [r.arrivee.estNm, r.arrivee.nordNm] : null,
    route_deg: r.sol.routeDeg,
    vitesse_sol_kt: r.sol.vitesseSolKt,
    ecart_seuil_m: Number.isFinite(r.ecartSeuilM) ? r.ecartSeuilM : null,
    gagne: r.gagne,
  };
}

/**
 * Nombre en français : virgule décimale, vrai signe moins.
 * @param {number} x
 * @param {number} decimales
 * @returns {string}
 */
export function formatNombre(x, decimales) {
  const s = Math.abs(x).toFixed(decimales).replace(".", ",");
  return x < 0 && Number(s.replace(",", ".")) !== 0 ? `−${s}` : s;
}

/**
 * Distance en mètres : en km avec deux décimales à partir de 1000 m, sinon en mètres entiers.
 * @param {number} m
 * @returns {string}
 */
export function formatDistanceM(m) {
  const a = Math.abs(m);
  return a >= 1000 ? `${formatNombre(a / 1000, 2)} km` : `${formatNombre(a, 0)} m`;
}

/**
 * Cap ou route au format aéronautique : trois chiffres, un décimal (083,6°).
 * @param {number} d
 * @returns {string}
 */
export function formatDeg(d) {
  const r = Math.round((((d % 360) + 360) % 360) * 10) / 10;
  const v = r >= 360 ? 0 : r;
  return `${v.toFixed(1).padStart(5, "0").replace(".", ",")}°`;
}
