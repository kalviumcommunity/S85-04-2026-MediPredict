const mongoose = require('mongoose');

const hospitalDataSchema = new mongoose.Schema({
  date: { type: Date, required: true },
  total_patients: { type: Number, required: true },
  oxygen_usage: { type: Number, required: true },
  ICU_cases: { type: Number, required: true }
});

module.exports = mongoose.model('HospitalData', hospitalDataSchema);