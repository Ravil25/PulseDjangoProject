function toggleSidebar() {
    let sidebar = document.getElementById("sidebar");
    let button = document.getElementById("sidebar-button");
    if (sidebar.style.display === "none") {
        sidebar.style.display = "block";
        button.innerText = "Hide";
    } else {
        sidebar.style.display = "none";
        button.innerText = "Show";
    }
}