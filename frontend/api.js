async function analyze(){
  const res = await fetch("http://127.0.0.1:8000/analyze",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify(sessionState.metrics)
  });

  const data = await res.json();
  localStorage.setItem("result",JSON.stringify(data));
  location.href="results.html";
}
