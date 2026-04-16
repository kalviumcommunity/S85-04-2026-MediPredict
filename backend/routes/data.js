const express = require('express');
const HospitalData = require('../models/HospitalData');

const router = express.Router();

// POST /api/data - store hospital data
router.post('/data', async (req, res) => {
  try {
    const data = new HospitalData(req.body);
    await data.save();
    res.status(201).json({ message: 'Data saved successfully' });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// GET /api/data - fetch all data
router.get('/data', async (req, res) => {
  try {
    const data = await HospitalData.find().sort({ date: 1 });
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// GET /api/predict - return predictions for next 7 days
router.get('/predict', async (req, res) => {
  try {
    const data = await HospitalData.find().sort({ date: -1 }).limit(7); // Last 7 days
    if (data.length < 7) {
      return res.status(400).json({ error: 'Not enough data for prediction' });
    }

    const patients = data.map(d => d.total_patients);
    const oxygen = data.map(d => d.oxygen_usage);
    const icu = data.map(d => d.ICU_cases);

    const avgPatients = patients.reduce((a, b) => a + b, 0) / patients.length;
    const avgOxygen = oxygen.reduce((a, b) => a + b, 0) / oxygen.length;
    const avgICU = icu.reduce((a, b) => a + b, 0) / icu.length;

    const predictions = [];
    for (let i = 1; i <= 7; i++) {
      const futureDate = new Date();
      futureDate.setDate(futureDate.getDate() + i);
      predictions.push({
        date: futureDate.toISOString().split('T')[0],
        total_patients: Math.round(avgPatients),
        oxygen_usage: Math.round(avgOxygen * 100) / 100,
        ICU_cases: Math.round(avgICU)
      });
    }

    res.json(predictions);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;