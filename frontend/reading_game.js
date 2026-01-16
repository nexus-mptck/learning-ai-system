let startRead;

function startReading(){
  startRead = Date.now();
  alert("Read and click OK");
}

function finishReading(words=120){
  const mins = (Date.now()-startRead)/60000;
  sessionState.metrics.reading_wpm = Math.round(words/mins);
  sessionState.metrics.regressions = Math.floor(Math.random()*6);
  sessionState.metrics.phoneme_errors = Math.floor(Math.random()*8);
}
