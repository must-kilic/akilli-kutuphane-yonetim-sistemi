apiFetch("/my-penalties").then(data => {
    data.forEach(p => {
      penalties.innerHTML += `<li>${p.delay_days} gün → ${p.amount} TL</li>`;
    });
  });
  