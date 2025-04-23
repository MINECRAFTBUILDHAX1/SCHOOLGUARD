<script>
  const logins = {
    "schoolguardfinal": { password: "1234", redirect: "schoolguardfinal.html" },
    "schoolB": { password: "abcd", redirect: "schoolB.html" },
    // add more schools as needed
  };

  document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (logins[username] && logins[username].password === password) {
      window.location.href = logins[username].redirect;
    } else {
      alert("Invalid username or password ❌");
    }
  });
</script>
