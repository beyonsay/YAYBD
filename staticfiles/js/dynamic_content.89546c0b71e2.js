document.addEventListener("DOMContentLoaded", function () {
  const categoryButtons = document.querySelectorAll("#category-list button");
  const contentItems = document.querySelectorAll(".content-item");

  categoryButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const categoryId = button.getAttribute("data-category-id");

      contentItems.forEach((item) => {
        const category = item.getAttribute("data-category");
        if (categoryId === "All" || category === categoryId) {
          item.style.display = "block"; // Show the item
        } else {
          item.style.display = "none"; // Hide the item
        }
      });
    });
  });
});