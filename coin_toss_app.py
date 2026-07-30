<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>LSTTP - Coin Toss Explorer</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>

body{
    font-family: Arial, sans-serif;
    background:#f5f7fb;
    margin:20px;
    text-align:center;
}

h1{
    color:#c62828;
}

.controls{
    margin:20px;
}

button{
    background:#c62828;
    color:white;
    border:none;
    padding:12px 20px;
    margin:5px;
    border-radius:8px;
    cursor:pointer;
    font-size:16px;
}

button:hover{
    background:#a61d1d;
}

.cards{
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:15px;
    margin:20px 0;
}

.card{
    background:white;
    padding:15px;
    width:180px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.1);
}

.card h3{
    margin:0;
}

.card p{
    font-size:26px;
    margin:10px 0 0;
}

.row{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:20px;
}

.chart-box{
    background:white;
    width:500px;
    padding:20px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.1);
}

.line-box{
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.1);
    margin-top:20px;
}

#result{
    font-size:28px;
    font-weight:bold;
    color:#1565c0;
}

</style>
</head>

<body>

<h1>LSTTP</h1>
<h2>Learn Stats To The Point</h2>
<h2>One Coin Toss Explorer</h2>

<div id="result">Ready to Toss</div>

<div class="controls">
<button onclick="tossCoin(1)">Toss 1</button>
<button onclick="tossCoin(10)">Toss 10</button>
<button onclick="tossCoin(100)">Toss 100</button>
<button onclick="resetAll()">Reset</button>
</div>

<div class="cards">

<div class="card">
<h3>Total Tosses</h3>
<p id="total">0</p>
</div>

<div class="card">
<h3>Heads</h3>
<p id="heads">0</p>
</div>

<div class="card">
<h3>Tails</h3>
<p id="tails">0</p>
</div>

<div class="card">
<h3>P(H)</h3>
<p id="ph">0.000</p>
</div>

<div class="card">
<h3>P(T)</h3>
<p id="pt">0.000</p>
</div>

</div>

<div class="row">

<div class="chart-box">
<h3>Theoretical Probability</h3>
<canvas id="pieChart"></canvas>
</div>

<div class="chart-box">
<h3>Observed Frequency</h3>
<canvas id="barChart"></canvas>
</div>

</div>

<div class="line-box">
<h3>Law of Large Numbers</h3>
<canvas id="lineChart"></canvas>
</div>

<script>

let heads=0;
let tails=0;
let total=0;

let labels=[];
let probabilities=[];

const pieChart=new Chart(
document.getElementById('pieChart'),
{
type:'pie',
data:{
labels:['Head','Tail'],
datasets:[{
data:[50,50]
}]
}
}
);

const barChart=new Chart(
document.getElementById('barChart'),
{
type:'bar',
data:{
labels:['Head','Tail'],
datasets:[{
label:'Frequency',
data:[0,0]
}]
},
options:{
responsive:true
}
}
);

const lineChart=new Chart(
document.getElementById('lineChart'),
{
type:'line',
data:{
labels:[],
datasets:[{
label:'Experimental P(H)',
data:[],
fill:false,
tension:0.1
}]
},
options:{
responsive:true,
scales:{
y:{
min:0,
max:1
}
}
}
}
);

function tossCoin(n){

let latest="";

for(let i=0;i<n;i++){

if(Math.random()<0.5){
heads++;
latest="HEAD";
}
else{
tails++;
latest="TAIL";
}

total++;

let p=heads/total;

labels.push(total);
probabilities.push(p);
}

document.getElementById("result").innerHTML=
"Latest Outcome: "+latest;

updateDisplay();
}

function updateDisplay(){

let ph=(total===0)?0:heads/total;
let pt=(total===0)?0:tails/total;

document.getElementById("total").innerHTML=total;
document.getElementById("heads").innerHTML=heads;
document.getElementById("tails").innerHTML=tails;

document.getElementById("ph").innerHTML=
ph.toFixed(3);

document.getElementById("pt").innerHTML=
pt.toFixed(3);

barChart.data.datasets[0].data=[
heads,
tails
];

barChart.update();

lineChart.data.labels=labels;
lineChart.data.datasets[0].data=
probabilities;

lineChart.update();
}

function resetAll(){

heads=0;
tails=0;
total=0;

labels=[];
probabilities=[];

document.getElementById("result").innerHTML=
"Ready to Toss";

updateDisplay();
}

</script>

</body>
</html>
