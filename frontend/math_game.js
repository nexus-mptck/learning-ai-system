function startMath(){
  let correct=0;
  for(let i=0;i<5;i++){
    let a=Math.floor(Math.random()*10);
    let b=Math.floor(Math.random()*10);
    if(parseInt(prompt(`${a}+${b}?`))===a+b) correct++;
  }
  sessionState.metrics.math_decay = Number((1-correct/5).toFixed(2));
  sessionState.metrics.weber_fraction = Number((Math.random()*0.4).toFixed(2));
}
