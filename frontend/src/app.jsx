// frontend/src/app.jsx
import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [file, setFile] = useState(null);
  const [scanResult, setScanResult] = useState(null);
  const [alerts, setAlerts] = useState([]);

  const handleScan = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/scan", formData);
    setScanResult(res.data);
  };

  const fetchAlerts = async () => {
    const res = await axios.get("http://localhost:8000/alerts");
    setAlerts(res.data);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">AI Antivirus Dashboard</h1>
      
      <input type="file" onChange={e => setFile(e.target.files[0])} className="mb-2" />
      <button onClick={handleScan} className="bg-blue-500 text-white px-4 py-2 rounded">Scan File</button>

      {scanResult && (
        <div className="mt-4 p-2 border rounded">
          <p><strong>File:</strong> {scanResult.filename}</p>
          <p><strong>Prediction:</strong> {scanResult.prediction}</p>
        </div>
      )}

      <button onClick={fetchAlerts} className="mt-4 bg-red-500 text-white px-4 py-2 rounded">Fetch Alerts</button>
      
      <ul className="mt-2">
        {alerts.map((alert, idx) => (
          <li key={idx} className="text-red-600">⚠️ {alert}</li>
        ))}
      </ul>
    </div>
  );
}
