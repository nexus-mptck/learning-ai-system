let times = [], start = null;

function startReaction() {
  times = [];
  nextTap();
}

function nextTap() {
  setTimeout(() => {
    start = Date.now();
    alert("TAP!");
  }, Math.random()*2000+1000);
}

document.onclick = () => {
  if(start){
    times.push(Date.now()-start);
    start = null;
    times.length < 5 ? nextTap() : finish();
  }
};

function finish(){
  const mean = times.reduce((a,b)=>a+b)/times.length;
  sessionState.metrics.reaction_time_mean = Math.round(mean);
  sessionState.metrics.reaction_time_std = Math.round(mean/4);
}
