const user = getUser();

if (!user || user.role !== "admin") {
  location.href = "../login.html";
}

document.getElementById("adminInfo").innerText =
  `Hoş geldin Admin (ID: ${user.id})`;
