function load() {
    apiFetch("/admin/books-status").then(data => {
      books.innerHTML = "";
      data.forEach(b => {
        books.innerHTML += `
          <tr>
            <td>${b.id}</td>
            <td>${b.title}</td>
            <td>${b.author}</td>
            <td>${b.borrowed_by || "-"}</td>
            <td><button onclick="del(${b.id})">Sil</button></td>
          </tr>`;
      });
    });
  }
  
  function addBook() {
    apiFetch("/books", {
      method: "POST",
      body: JSON.stringify({
        title: title.value,
        author: author.value
      })
    }).then(load);
  }
  
  function del(id) {
    apiFetch("/books/" + id, { method: "DELETE" }).then(load);
  }
  
  load();
  