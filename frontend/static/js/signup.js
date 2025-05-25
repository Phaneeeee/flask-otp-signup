document.getElementById("signupForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(this);
  const data = Object.fromEntries(formData.entries());
  const messageBox = document.getElementById("message");
  messageBox.textContent = ""; // Clear previous messages

  try {
    const response = await fetch("http://127.0.0.1:5000/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (response.ok) {
      // Store email to localStorage for OTP verification
      localStorage.setItem("emailForOtp", data.email);
      // Store success message to show in otp.html
      sessionStorage.setItem("otpMessage", "OTP sent successfully!");
      // Redirect to OTP verification page
      window.location.href = "/otp";
    } else {
      messageBox.textContent = result.error || "Signup failed.";
      messageBox.style.color = "red";
    }
  } catch (error) {
    console.error("Signup error:", error);
    messageBox.textContent = "Failed to signup. Please try again.";
    messageBox.style.color = "red";
  }
});
