import { useEffect, useState } from "react";
export default function Home() {
  const [apiMessage, setApiMessage] = useState("");
  useEffect(() => {
    fetch("/api/hello")
      .then((res) => res.json())
      .then((data) => setApiMessage(data.message));
  }, []);
  return (
    <main style={{fontFamily:'sans-serif', padding:'2rem'}}>
      <h1>Welcome to Xylon IDE 3 (React)</h1>
      <p>This is now a full-stack React app ready for Vercel.</p>
      <p>API says: <b>{apiMessage}</b></p>
    </main>
  );
}