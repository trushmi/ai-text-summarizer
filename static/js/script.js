// Get DOM elements

const inputTextArea = document.getElementById("inputTextArea");
const summarizeButton = document.getElementById("summarizeButton");
const summaryTextArea = document.getElementById("summaryTextArea");
const resetButton = document.getElementById("reset-button");
const loader = document.querySelector(".loader");

// Disable the summarize button by default

summarizeButton.disabled = true;

// Validate the input text area

function textValidation(e) {
  const textarea = e.target;
  const minLength = 200;
  const maxLength = 100000;
  if (textarea.value.length > minLength && textarea.value.length < maxLength) {
    summarizeButton.disabled = false;
  } else {
    summarizeButton.disabled = true;
  }
}
// Listen for input events on the input text area

inputTextArea.addEventListener("input", textValidation);

const loaderOverlay = document.querySelector(".loader-overlay");

function showLoader() {
  loaderOverlay.style.display = "flex";
}

function hideLoader() {
  loaderOverlay.style.display = "none";
}

// Listen for click events on the summarize button

summarizeButton.addEventListener("click", async (event) => {
  event.preventDefault();
  showLoader();
  const text = inputTextArea.value;
  try {
    const response = await fetch("/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    summaryTextArea.value = data.summary;
  } catch (error) {
    console.error("Error fetching summary:", error);
    summaryTextArea.value = "Error fetching summary";
  } finally {
    hideLoader();
  }
});

// Listen for click events on the reset button

resetButton.addEventListener("click", () => {
  inputTextArea.value = "";
  summaryTextArea.value = "";
  summarizeButton.disabled = true;
});
