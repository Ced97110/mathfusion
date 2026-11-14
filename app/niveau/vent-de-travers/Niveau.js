'use client';
// Niveau « Vent de travers » (chapitre 41) : prédire, agir, observer, expliquer.
// Toutes les valeurs affichées viennent de lib/niveau_vent.js (testé par Vitest).
import 'katex/dist/katex.min.css';
import './niveau.css';
import katex from 'katex';
import { useEffect, useRef, useState } from 'react';
import {
  AVION_KT,
  ROUTE_DEG,
  VENT,
  formatDeg,
  formatDistanceM,
  formatNombre,
  positionApresNm,
  resultatTentative,
  tentativeJson,
  trianglePourCap,
} from '../../../lib/niveau_vent.js';
import { composantesVent, sommeNaive } from '../../../lib/vent.js';
import Carte, { X, Y } from './Carte';
import Molette from './Molette';
import Seuil from './Seuil';

const CLE_STOCKAGE = 'niveau-vent-tentatives';
const ETAPES = ['Prédire', 'Agir', 'Observer', 'Expliquer'];

/** Nombre au format KaTeX : virgule décimale protégée, signe moins ASCII. */
const tex = (x, d) => formatNombre(x, d).replace('−', '-').replace(',', '{,}');
const rendu = (s) => ({ __html: katex.renderToString(s, { throwOnError: false, displayMode: true }) });

function lireTentatives() {
  try {
    const brut = window.localStorage.getItem(CLE_STOCKAGE);
    const t = brut ? JSON.parse(brut) : [];
    return Array.isArray(t) ? t : [];
  } catch {
    return [];
  }
}
function ecrireTentatives(t) {
  try {
    window.localStorage.setItem(CLE_STOCKAGE, JSON.stringify(t));
  } catch {
    // stockage indisponible (navigation privée) : les tentatives restent en mémoire et téléchargeables
  }
}

export default function Niveau() {
  const [cap, setCap] = useState(90);
  const [phase, setPhase] = useState('choisir');
  const [prediction, setPrediction] = useState(null);
  const [resultat, setResultat] = useState(null);
  const [tentatives, setTentatives] = useState([]);
  const [modeFps, setModeFps] = useState(false);
  const [fps, setFps] = useState(null);
  const svgRef = useRef(null);
  const avionRef = useRef(null);
  const traceRef = useRef(null);
  const rafRef = useRef(0);

  useEffect(() => {
    setTentatives(lireTentatives());
    setModeFps(new URLSearchParams(window.location.search).has('fps'));
    return () => cancelAnimationFrame(rafRef.current);
  }, []);

  function placerAvion(p, c) {
    avionRef.current?.setAttribute('transform', `translate(${X(p.estNm)} ${Y(p.nordNm)}) rotate(${c})`);
  }

  function lancer() {
    if (phase !== 'choisir' || !prediction) return;
    const r = resultatTentative(cap);
    const capFige = cap;
    const heuresVol = Number.isFinite(r.heures) ? Math.min(r.heures, 2) : 1;
    const dureeMs = heuresVol * (modeFps ? 10 : 4) * 1000;
    const points = [];
    const intervalles = [];
    let t0 = 0;
    let avant = 0;
    setResultat(r);
    setPhase('vol');

    const image = (maintenant) => {
      if (!t0) {
        t0 = maintenant;
        avant = maintenant;
      } else {
        intervalles.push(maintenant - avant);
        avant = maintenant;
      }
      const f = Math.min(1, (maintenant - t0) / dureeMs);
      const p = positionApresNm(capFige, f * heuresVol);
      placerAvion(p, capFige);
      points.push(`${X(p.estNm).toFixed(1)},${Y(p.nordNm).toFixed(1)}`);
      traceRef.current?.setAttribute('points', points.join(' '));
      if (f < 1) {
        rafRef.current = requestAnimationFrame(image);
        return;
      }
      const total = intervalles.reduce((a, b) => a + b, 0);
      setFps(
        intervalles.length
          ? { moyenne: (1000 * intervalles.length) / total, minimum: 1000 / Math.max(...intervalles), duree: total / 1000 }
          : null,
      );
      const j = tentativeJson(capFige, prediction, r, new Date().toISOString());
      setTentatives((anciennes) => {
        const nouvelles = [...anciennes, j];
        ecrireTentatives(nouvelles);
        return nouvelles;
      });
      setPhase('bilan');
    };
    rafRef.current = requestAnimationFrame(image);
  }

  function nouvelEssai() {
    cancelAnimationFrame(rafRef.current);
    traceRef.current?.setAttribute('points', '');
    placerAvion({ estNm: 0, nordNm: 0 }, cap);
    setPrediction(null);
    setResultat(null);
    setFps(null);
    setPhase('choisir');
  }

  function telecharger() {
    const blob = new Blob([JSON.stringify(tentatives, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'vent-de-travers-tentatives.json';
    a.click();
    URL.revokeObjectURL(url);
  }

  function effacer() {
    setTentatives([]);
    ecrireTentatives([]);
  }

  const etape = phase === 'vol' ? 2 : phase === 'bilan' ? 3 : prediction ? 1 : 0;
  const triangle = resultat ? trianglePourCap(resultat.capDeg) : null;

  return (
    <article className="nv">
      <Carte
        phase={phase}
        cap={cap}
        prediction={prediction}
        resultat={resultat}
        triangle={triangle}
        onTap={setPrediction}
        refs={{ svgRef, avionRef, traceRef }}
      />

      <ol className="nv-etapes" aria-label="Étapes">
        {ETAPES.map((e, i) => (
          <li key={e} className={i === etape ? 'nv-actuelle' : i < etape ? 'nv-faite' : ''} aria-current={i === etape ? 'step' : undefined}>
            {e}
          </li>
        ))}
      </ol>

      <div className="nv-grille">
        <Molette cap={cap} bloque={phase !== 'choisir'} onChange={setCap} />

        <div className="nv-panneau">
          {phase === 'choisir' && (
            <>
              <h1>Vent de travers</h1>
              <p>
                Un Cessna 172S vole à {AVION_KT} kt dans l'air. Le vent le pousse vers le sud-est. Fais-le passer sur la piste, plein est.
              </p>
              <p className="nv-consigne">
                {prediction
                  ? 'Ta prédiction est posée. Lance le vol : le cap sera bloqué jusqu’à la fin.'
                  : 'Règle le cap. Puis touche la carte là où tu penses que l’avion passera la ligne de la piste.'}
              </p>
              <button type="button" className="nv-btn" disabled={!prediction} onClick={lancer}>
                Lancer le vol
              </button>
            </>
          )}

          {phase === 'vol' && <p className="nv-consigne">Vol en cours. Le cap est bloqué au {formatDeg(cap)}.</p>}

          {phase === 'bilan' && resultat && (
            <Bilan resultat={resultat} prediction={prediction} triangle={triangle} fps={modeFps ? fps : null} onRejouer={nouvelEssai} />
          )}
        </div>
      </div>

      <section className="nv-tentatives" aria-label="Tentatives enregistrées">
        <h2>Tentatives ({tentatives.length})</h2>
        {tentatives.length > 0 && (
          <ul>
            {tentatives.slice(-5).reverse().map((t) => (
              <li key={t.horodatage}>
                Cap {formatDeg(t.cap_deg)} · {t.ecart_seuil_m === null ? 'n’atteint pas la piste' : `${formatDistanceM(t.ecart_seuil_m)} de l’axe`} ·{' '}
                <span className={t.gagne ? 'nv-vrai' : 'nv-faux'}>{t.gagne ? 'gagné' : 'raté'}</span>
              </li>
            ))}
          </ul>
        )}
        <div className="nv-actions">
          <button type="button" className="nv-sec" disabled={!tentatives.length} onClick={telecharger}>
            Télécharger (JSON)
          </button>
          <button type="button" className="nv-sec" disabled={!tentatives.length} onClick={effacer}>
            Effacer
          </button>
        </div>
      </section>

      <p className="nv-sources">
        Mesures : Cessna 172S, 119 kt (manuel de vol, Rev. 4, fig. 4-3) ; vent à De Bilt le 12 novembre 2026, 12 h UTC, 1222 m, vient du 316° à 9,5 m/s
        (University of Wyoming) ; couloir d’approche de 700 ft au seuil (AIM, FAA). Carte : la piste est un symbole, pas à l’échelle.
      </p>
    </article>
  );
}

function Bilan({ resultat, prediction, triangle, fps, onRejouer }) {
  const { sol, gagne, ecartSeuilM, heures } = resultat;
  const naif = sommeNaive(AVION_KT, VENT);
  const ecartPrediction =
    prediction && Number.isFinite(heures)
      ? Math.hypot(prediction.estNm - resultat.arrivee.estNm, prediction.nordNm - resultat.arrivee.nordNm)
      : null;
  const travers = composantesVent(VENT, ROUTE_DEG).traversKt;
  const somme =
    String.raw`\underbrace{\begin{pmatrix}${tex(triangle.air.estNm, 1)}\\${tex(triangle.air.nordNm, 1)}\end{pmatrix}}_{\text{air}}` +
    String.raw`+\underbrace{\begin{pmatrix}${tex(triangle.vent.estNm, 1)}\\${tex(triangle.vent.nordNm, 1)}\end{pmatrix}}_{\text{vent}}` +
    String.raw`=\underbrace{\begin{pmatrix}${tex(triangle.sol.estNm, 1)}\\${tex(triangle.sol.nordNm, 1)}\end{pmatrix}}_{\text{sol}}`;
  const regle = String.raw`\text{cap}=090^\circ-\arcsin\frac{${tex(-travers, 2)}}{${AVION_KT}}=${formatDeg(90 + (Math.asin(travers / AVION_KT) * 180) / Math.PI).replace(',', '{,}').replace('°', '^\\circ')}`;

  return (
    <div className="nv-bilan">
      <h1 className={gagne ? 'nv-vrai' : 'nv-faux'}>{gagne ? 'Posé sur la piste' : 'À côté de la piste'}</h1>
      <Seuil ecartM={ecartSeuilM} />
      {ecartPrediction !== null && <p>Ta prédiction était à {formatNombre(ecartPrediction, 1)} NM du point réel.</p>}
      <p>
        En une heure, l’avion parcourt <span className="nv-bleu">{AVION_KT} NM dans l’air vers le {formatDeg(resultat.capDeg)}</span>, et l’air
        lui-même avance de <span className="nv-violet">{formatNombre(VENT.vitesseKt, 1)} NM vers le {formatDeg(VENT.vientDuDeg + 180)}</span>. Au sol, cela
        fait <span className="nv-vert">{formatNombre(sol.vitesseSolKt, 1)} NM vers le {formatDeg(sol.routeDeg)}</span>.
      </p>
      <div className="nv-formule" dangerouslySetInnerHTML={rendu(somme)} />
      <p className="nv-petit">Vecteurs en milles nautiques par heure : en haut vers l’est, en bas vers le nord.</p>
      <p>
        Vitesse sol : {formatNombre(sol.vitesseSolKt, 1)} kt, pas {AVION_KT} + {formatNombre(VENT.vitesseKt, 1)} = {formatNombre(naif, 1)} kt. Les longueurs ne
        s’additionnent pas : ce sont les flèches qui s’additionnent, bout à bout.
      </p>
      {gagne && (
        <>
          <p>La règle des pilotes donne le même cap :</p>
          <div className="nv-formule" dangerouslySetInnerHTML={rendu(regle)} />
        </>
      )}
      {fps && (
        <p className="nv-petit">
          Mesure d’affichage : {formatNombre(fps.moyenne, 1)} images par seconde en moyenne, minimum {formatNombre(fps.minimum, 1)}, sur{' '}
          {formatNombre(fps.duree, 1)} s.
        </p>
      )}
      <button type="button" className="nv-btn" onClick={onRejouer}>
        Nouvel essai
      </button>
    </div>
  );
}
