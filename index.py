<!-- Update the JavaScript code in your HTML file -->
<script>
document.addEventListener("DOMContentLoaded", function () {
  const endpointUrl = "/api/environment_data"; // Use the Flask route

  function fetchData() {
    fetch(endpointUrl)
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("temperature").textContent = data.temperature.toFixed(2);
        document.getElementById("humidity").textContent = data.humidity.toFixed(2);

        // Customize suggestions and background image based on data (as in your original JavaScript code)

        // ...

      })
      .catch((error) => {
        console.error("Error fetching data: " + error);
      });
  }

  // Initial data fetch
  fetchData();

  // Refresh data on button click
  document.getElementById("refresh-button").addEventListener("click", fetchData);
});
</script>
