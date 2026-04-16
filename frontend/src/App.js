import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import './App.css';

function App() {
  const [data, setData] = useState([]);
  const [predictions, setPredictions] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetchData();
    fetchPredictions();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/data');
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const fetchPredictions = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/predict');
      setPredictions(response.data);
      checkAlerts(response.data);
    } catch (error) {
      console.error('Error fetching predictions:', error);
    }
  };

  const checkAlerts = (preds) => {
    const newAlerts = [];
    preds.forEach(pred => {
      if (pred.oxygen_usage > 500) {
        newAlerts.push(`Warning: Oxygen usage predicted to exceed 500L on ${pred.date}`);
      }
      if (pred.ICU_cases > 8) {
        newAlerts.push(`Alert: ICU cases may increase on ${pred.date}`);
      }
    });
    setAlerts(newAlerts);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const newData = {
      date: formData.get('date'),
      total_patients: parseInt(formData.get('total_patients')),
      oxygen_usage: parseFloat(formData.get('oxygen_usage')),
      ICU_cases: parseInt(formData.get('ICU_cases'))
    };
    try {
      await axios.post('http://localhost:5000/api/data', newData);
      fetchData();
      fetchPredictions();
    } catch (error) {
      console.error('Error saving data:', error);
    }
  };

  const chartData = [...data, ...predictions.map(p => ({ ...p, predicted: true }))];

  return (
    <div className="App">
      <h1>MediPredict Dashboard</h1>
      <form onSubmit={handleSubmit}>
        <input name="date" type="date" required />
        <input name="total_patients" type="number" placeholder="Total Patients" required />
        <input name="oxygen_usage" type="number" step="0.1" placeholder="Oxygen Usage (L)" required />
        <input name="ICU_cases" type="number" placeholder="ICU Cases" required />
        <button type="submit">Add Data</button>
      </form>
      <div>
        <h2>Historical and Predicted Data</h2>
        <LineChart width={800} height={400} data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="total_patients" stroke="#8884d8" />
          <Line type="monotone" dataKey="oxygen_usage" stroke="#82ca9d" />
          <Line type="monotone" dataKey="ICU_cases" stroke="#ffc658" />
        </LineChart>
      </div>
      <div>
        <h2>Alerts</h2>
        {alerts.length > 0 ? (
          <ul>
            {alerts.map((alert, index) => <li key={index}>{alert}</li>)}
          </ul>
        ) : (
          <p>No alerts</p>
        )}
      </div>
    </div>
  );
}

export default App;