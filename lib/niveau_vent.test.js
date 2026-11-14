// Logique de jeu du niveau « Vent de travers » : chaque valeur affichée par la page vient d'ici.
import { describe, expect, it } from "vitest";
import data from "../data/vent_travers.json";
import {
  AVION_KT,
  DEMI_LARGEUR_M,
  DISTANCE_SEUIL_NM,
  VENT,
  formatDeg,
  formatDistanceM,
  formatNombre,
  positionApresNm,
  resultatTentative,
  tentativeJson,
  trianglePourCap,
} from "./niveau_vent.js";

const TOL = 1e-6;
const rad = (d) => (d * Math.PI) / 180;
const W = (data.vent.vitesse_m_s * 3600) / 1852;

describe("constantes tirées des mesures", () => {
  it("reprennent data/vent_travers.json sans arrondi", () => {
    expect(AVION_KT).toBe(119);
    expect(VENT.vientDuDeg).toBe(316);
    expect(Math.abs(VENT.vitesseKt - W)).toBeLessThan(TOL);
    expect(Math.abs(DEMI_LARGEUR_M - 350 * 0.3048)).toBeLessThan(TOL);
  });
  it("le seuil est à une heure de vol avec le bon cap (131,08 NM)", () => {
    expect(DISTANCE_SEUIL_NM).toBeCloseTo(131.08, 2);
  });
});

describe("position de l'avion", () => {
  it("après t heures = t × (vecteur air + vecteur vent)", () => {
    const p = positionApresNm(90, 0.5);
    expect(Math.abs(p.estNm - 0.5 * (119 + W * Math.sin(rad(136))))).toBeLessThan(TOL);
    expect(Math.abs(p.nordNm - 0.5 * W * Math.cos(rad(136)))).toBeLessThan(TOL);
  });
});

describe("résultat d'une tentative", () => {
  it("cap 090° : passe le seuil à 13,21 NM au sud, perd", () => {
    const r = resultatTentative(90);
    expect(r.gagne).toBe(false);
    expect(r.ecartSeuilM / 1852).toBeCloseTo(13.21, 2);
    expect(Math.abs(r.arrivee.estNm - DISTANCE_SEUIL_NM)).toBeLessThan(TOL);
    // écart = position nord au passage du seuil, en mètres, signe inversé (droite = sud)
    expect(Math.abs(r.ecartSeuilM + r.arrivee.nordNm * 1852)).toBeLessThan(1e-3);
  });
  it("cap 083,6° gagne, 083,5° et 083,7° perdent", () => {
    expect(resultatTentative(83.6).gagne).toBe(true);
    expect(resultatTentative(83.5).gagne).toBe(false);
    expect(resultatTentative(83.7).gagne).toBe(false);
  });
  it("la durée jusqu'au seuil est distance / composante est", () => {
    const r = resultatTentative(80);
    expect(Math.abs(r.heures - DISTANCE_SEUIL_NM / r.sol.estKt)).toBeLessThan(TOL);
  });
  it("un cap qui n'avance pas vers l'est n'atteint jamais le seuil", () => {
    const r = resultatTentative(270);
    expect(r.gagne).toBe(false);
    expect(r.heures).toBe(Number.POSITIVE_INFINITY);
  });
});

describe("triangle affiché pour l'explication", () => {
  it("bleu + violet = vert, composante par composante", () => {
    const t = trianglePourCap(90);
    expect(Math.abs(t.air.estNm + t.vent.estNm - t.sol.estNm)).toBeLessThan(TOL);
    expect(Math.abs(t.air.nordNm + t.vent.nordNm - t.sol.nordNm)).toBeLessThan(TOL);
    expect(Math.abs(Math.hypot(t.air.estNm, t.air.nordNm) - 119)).toBeLessThan(TOL);
    expect(Math.abs(Math.hypot(t.vent.estNm, t.vent.nordNm) - W)).toBeLessThan(TOL);
  });
});

describe("enregistrement JSON", () => {
  it("contient les champs du plan, avec les valeurs du calcul", () => {
    const r = resultatTentative(85);
    const j = tentativeJson(85, { estNm: 120, nordNm: -5 }, r, "2026-11-14T12:00:00.000Z");
    expect(Object.keys(j)).toEqual([
      "horodatage",
      "cap_deg",
      "prediction_xy",
      "arrivee_xy",
      "route_deg",
      "vitesse_sol_kt",
      "ecart_seuil_m",
      "gagne",
    ]);
    expect(j.cap_deg).toBe(85);
    expect(j.prediction_xy).toEqual([120, -5]);
    expect(j.ecart_seuil_m).toBe(r.ecartSeuilM);
    expect(JSON.parse(JSON.stringify(j))).toEqual(j);
  });
});

describe("format français", () => {
  it("virgule décimale et trois chiffres pour un cap", () => {
    expect(formatDeg(83.6)).toBe("083,6°");
    expect(formatDeg(90)).toBe("090,0°");
    expect(formatDeg(359.96)).toBe("000,0°");
    expect(formatNombre(131.0842, 1)).toBe("131,1");
    expect(formatNombre(-13.21, 2)).toBe("−13,21");
    expect(formatDistanceM(24463.4)).toBe("24,46 km");
    expect(formatDistanceM(-35.006)).toBe("35 m");
    expect(formatDistanceM(999.4)).toBe("999 m");
  });
});
