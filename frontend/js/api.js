const API_URL = "http://localhost:5000";

function apiFetch(url, options = {}) {
  const token = localStorage.token;

  return fetch(API_URL + url, {
    ...options,
    headers: {
      ...(options.headers || {}),
      "Content-Type": "application/json",
      ...(token ? { "Authorization": "Bearer " + token } : {})
    }
  }).then(async res => {
    const data = await res.json();

    if (!res.ok) {
      console.error("API ERROR:", data);
      throw data;
    }

    return data;
  });
}
