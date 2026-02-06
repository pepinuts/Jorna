import { useEffect, useState } from 'react'
import { getHealth } from './api'

type Health = { status: string; time_utc: string }

export default function App() {
  const [health, setHealth] = useState<Health | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    getHealth()
      .then(setHealth)
      .catch((e) => setError(e instanceof Error ? e.message : String(e)))
  }, [])

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: 24, maxWidth: 720 }}>
      <h1 style={{ margin: 0 }}>Training App</h1>
      <p style={{ marginTop: 8, opacity: 0.8 }}>
        Starter minimal (FastAPI + React). Objectif : coder brique par brique.
      </p>

      <div style={{ marginTop: 16, padding: 16, border: '1px solid #ddd', borderRadius: 12 }}>
        <h2 style={{ marginTop: 0 }}>Connexion API</h2>

        {!health && !error && <p>Chargement…</p>}
        {error && (
          <p>
            <strong>Erreur:</strong> {error}
          </p>
        )}
        {health && (
          <ul>
            <li>
              <strong>Status:</strong> {health.status}
            </li>
            <li>
              <strong>Heure (UTC):</strong> {health.time_utc}
            </li>
          </ul>
        )}

        <p style={{ marginTop: 12, opacity: 0.8 }}>
          Essaie aussi Swagger: <code>http://localhost:8000/docs</code>
        </p>
      </div>
    </div>
  )
}
