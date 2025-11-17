const toggleBtn = document.getElementById("theme-toggle");
const body = document.body;

// Load saved theme preference
if (localStorage.getItem("theme") === "dark") {
  body.classList.add("dark");
  toggleBtn.textContent = "☀️ Light Mode";
} else if (localStorage.getItem("theme") === "light") {
  body.classList.remove("dark");
  toggleBtn.textContent = "🌙 Dark Mode";
} else {
  // Auto-detect from system if no preference saved
  if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    body.classList.add("dark");
    toggleBtn.textContent = "☀️ Light Mode";
  }
}

// Toggle on button click
toggleBtn.addEventListener("click", () => {
  if (body.classList.contains("dark")) {
    body.classList.remove("dark");
    localStorage.setItem("theme", "light");
    toggleBtn.textContent = "🌙 Dark Mode";
  } else {
    body.classList.add("dark");
    localStorage.setItem("theme", "dark");
    toggleBtn.textContent = "☀️ Light Mode";
  }
});
