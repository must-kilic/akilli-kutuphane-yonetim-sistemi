apiFetch("/admin/reports").then(data => {
    reports.innerHTML = "";
  
    data.forEach(r => {
      reports.innerHTML += `
        <li>
          Kullanıcı: ${r.user} |
          Kitap: ${r.book} |
          Ceza: ${r.amount || 0} TL
          <button onclick="clearPenalties('${r.user}')">
            Cezaları Temizle
          </button>
        </li>
      `;
    });
  });
  
  function clearPenalties(email) {
    if (!confirm(`${email} kullanıcısının tüm cezaları silinsin mi?`)) return;
  
    apiFetch("/admin/clear-penalties", {
      method: "POST",
      body: JSON.stringify({ email })
    }).then(res => {
      alert(res.message);
      location.reload();
    });
  }
  