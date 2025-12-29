apiFetch("/books").then(data => {
    data.forEach(b => {
      books.innerHTML += `
        <div>
          ${b.title}
          <button onclick="borrow(${b.id})">Ödünç Al</button>
        </div>`;
    });
  });
  
  function borrow(id) {
    apiFetch("/api/borrowings/", {
      method: "POST",
      body: JSON.stringify({ book_id: id })
    }).then(res => {
      alert(res.message);
    });
  }
  
  