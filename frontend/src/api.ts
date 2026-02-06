const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

export async function getHealth(): Promise<{ status: string; time_utc: string }> {
  const res = await fetch(`${API_URL}/api/v1/health`)
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`)
  }
  return res.json()
}
