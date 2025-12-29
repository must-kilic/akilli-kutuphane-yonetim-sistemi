apiFetch("/my-borrowings").then(data => {
    data.forEach(b => {
      list.innerHTML += `
        <li>
          ${b.title}
          <button onclick="ret(${b.borrow_id}, this)">İade</button>
        </li>`;
    });
  });
  
  function ret(id, btn) {
    apiFetch(`/api/borrowings/return/${id}`, {
      method: "PUT"
    }).then(res => {
      alert(res.message);
  
      btn.closest("li").remove();
    });
  }
  
  