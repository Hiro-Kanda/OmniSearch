export default async function Home() {
  const base = process.env.API_BASE_INTERNAL ?? "http://backend:8000";
  const res = await fetch(`${base}/api/health`, { cache: "no-store" });
  const data = await res.json();

  return (
    <main style={{ padding: 24, fontFamily: "sans-serif" }}>
      <h1>RAG SharePoint Dev</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}