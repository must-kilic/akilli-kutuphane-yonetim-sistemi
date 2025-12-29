const user = getUser();

if (!user || user.role !== "user") {
  location.href = "../login.html";
}

document.getElementById("userInfo").innerText =
  `Hoş geldin (Kullanıcı ID: ${user.id})`;
