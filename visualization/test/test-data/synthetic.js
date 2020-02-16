const fs = require('fs');
const parse = require('csv-parse/lib/sync');
const seedrandom = require('seedrandom');
const prng = seedrandom('42');


function read(filename) {
  const csv = fs.readFileSync(filename).toString();
  return parse(csv, {
    delimiter: ', ',
    columns: [
      'age',
      'workclass',
      'fnlwgt',
      'education',
      'education-num',
      'marital-status',
      'occupation',
      'relationship',
      'race',
      'sex',
      'capital-gain',
      'capital-loss',
      'hours-per-week',
      'native-country',
      'income-label'
    ]
  });
}


function simulatedPredictions(records, bias) {
  return records.map(r => prng() > bias ? 1 : 0);
}

function compute(records) {
  const features = (records.length === 0) ? [] : Object.keys(records[0]);
  const predictionsByModels = [
    simulatedPredictions(records, 0.3),
    simulatedPredictions(records, 0.3),
    simulatedPredictions(records, 0.3)
  ];
  const p = n => Math.round(n / records.length);
  return JSON.stringify({
    featureNames: features,
    // className: 
    trueY: records.map(r => r['income-label'] === '>50K' ? 1 : 0),
    predictedYs: predictionsByModels,
    augmentedData: records.map(r => Object.values(r))
  });
}


const n = 1000;
const records = read('./uci-adult.data');
const sampledRecords = records.sort((a, b) => prng() - 0.5).slice(0, n)
console.log(compute(sampledRecords));