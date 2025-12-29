function login() {
    apiFetch("/login", {
      method: "POST",
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    }).then(res => {
      if (!res.token) {
        error.innerText = "Giriş başarısız";
        return;
      }
  
      localStorage.token = res.token;
  
      const payload = JSON.parse(atob(res.token.split('.')[1]));
      const role = payload.role; 
      if (role === "admin") {
        window.location.href = "admin/dashboard.html";
      } else {
        window.location.href = "user/dashboard.html";
      }
    });
  }
  
  function getUser() {
    const token = localStorage.token;
    if (!token) return null;
  
    const payload = JSON.parse(atob(token.split('.')[1]));
  
    return {
      id: payload.sub,     // string user_id
      role: payload.role, // claim
      email: payload.email
    };
  }
  