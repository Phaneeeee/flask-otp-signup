document.getElementById("loginForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(this);
  const data = Object.fromEntries(formData.entries());

  const messageBox = document.getElementById("loginMessage");
  messageBox.textContent = ""; // Clear previous messages

  try {
    const response = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (response.ok) {
      messageBox.style.color = "green";
      messageBox.textContent = result.message || "Login successful!";
      // Optionally redirect after a delay
      setTimeout(() => {
        window.location.href = "/dashboard"; // Change to your desired route
      }, 1500);
    } else {
      messageBox.style.color = "red";
      messageBox.textContent = result.error || "Login failed.";
    }
  } catch (error) {
    console.error("Login error:", error);
    messageBox.style.color = "red";
    messageBox.textContent = "Failed to login. Please try again.";
  }
});
