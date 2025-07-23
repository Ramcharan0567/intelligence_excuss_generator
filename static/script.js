document.getElementById("excuseForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const scenario = document.getElementById("scenario").value;
  const urgency = document.getElementById("urgency").value;
  const style = document.getElementById("style").value;
  const proof = document.getElementById("proof").value;
  const language = document.getElementById("language").value;

  document.getElementById("excuseText").textContent = "Generating...";

  try {
    const response = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ scenario, urgency, style, proof, language })
    });

    const data = await response.json();
    document.getElementById("excuseText").textContent = data.excuse;
  } catch (err) {
    console.error("Error:", err);
    document.getElementById("excuseText").textContent = "Something went wrong.";
  }
});
