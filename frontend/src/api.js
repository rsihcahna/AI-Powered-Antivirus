// src/api.js

const BASE_URL = "http://localhost:8000"; // Change this URL if deploying backend elsewhere

// 🧠 ML Prediction
export const predictThreat = async (fileData) => {
  const response = await fetch(`${BASE_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data: fileData }),
  });
  return response.json();
};

// 🌐 Network Logs
export const fetchNetworkLogs = async () => {
  const response = await fetch(`${BASE_URL}/network/logs`);
  return response.json();
};

// 🐍 System Scan (Rust Engine)
export const startSystemScan = async () => {
  const response = await fetch(`${BASE_URL}/scan`, {
    method: "POST",
  });
  return response.json();
};

// 📊 Get Alerts
export const getAlerts = async () => {
  const response = await fetch(`${BASE_URL}/alerts`);
  return response.json();
};
