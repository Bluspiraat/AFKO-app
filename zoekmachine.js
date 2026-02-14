let data = [];

fetch("afco_lijst.json")
  .then(res => res.json())
  .then(json => data = json);

function normaliseer(str) {
  return str
    .toLowerCase()
    .trim();
}

function zoek() {
  const q = normaliseer(
    document.getElementById("searchBox").value
  );

  const results = data.filter(item =>
    normaliseer(item.Afkorting).includes(q)
  );

  const resultDiv = document.getElementById("result");

  if(results.length === 0){
    resultDiv.innerText = "Niet gevonden";
    return;
  }

  resultDiv.innerHTML = results
    .map(r => `<p><b>${r.Afkorting}</b> = ${r.Betekenis.trim()}</p>`)
    .join("");
}