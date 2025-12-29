const user = getUser();
if (!user || user.role !== "admin") {
  location.href = "../login.html";
}

apiFetch("/users").then(data => {
  data.forEach(u => {
    users.innerHTML += `
      <tr>
        <td>${u.id}</td>
        <td>${u.email}</td>
        <td>${u.role}</td>
        <td>
          <button onclick="del(${u.id})">Sil</button>
        </td>
      </tr>
    `;
  });
});

function del(id) {
  if (!confirm("Kullanıcı silinsin mi?")) return;
  apiFetch("/users/" + id, { method: "DELETE" })
    .then(() => location.reload());
}
