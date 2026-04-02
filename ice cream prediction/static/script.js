document.getElementById("predictForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const temperature = document.getElementById("temperature").value;
  const rainfall = document.getElementById("rainfall").value;

  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ temperature, rainfall })
  });

  const result = await response.json();
  document.getElementById("result").innerText =
    "Predicted Ice Creams Sold: " + result.prediction;
});
