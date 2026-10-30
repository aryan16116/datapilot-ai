import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000";

type HealthState =
  | { kind: "loading" }
  | { kind: "ok" }
  | { kind: "error"; message: string };

export default function App() {
  const [health, setHealth] = useState<HealthState>({ kind: "loading" });

  useEffect(() => {
    fetch(`${API_URL}/health`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }
        return res.json() as Promise<{ status: string }>;
      })
      .then((data) => {
        setHealth(data.status === "ok" ? { kind: "ok" } : { kind: "error", message: data.status });
      })
      .catch((err: Error) => {
        setHealth({ kind: "error", message: err.message });
      });
  }, []);

  return (
    <main style={{ fontFamily: "system-ui", padding: "2rem" }}>
      <h1>DataPilot AI</h1>
      {health.kind === "loading" && <p>Checking backend...</p>}
      {health.kind === "ok" && <p>Backend status: ok</p>}
      {health.kind === "error" && <p>Backend unreachable: {health.message}</p>}
    </main>
  );
}