function showAlert() {
    alert("Hello from external JS!");
}

function showTable() {
    // Show the hidden CSV table
    const tableDiv = document.getElementById("csv-table");
    tableDiv.style.display = "block";

    // Optional: alert when showing table
    alert("CSV table is now visible!");
}
