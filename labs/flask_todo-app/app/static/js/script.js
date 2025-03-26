document.addEventListener("DOMContentLoaded", function () {
  // Fade in the todo items when page loads
  const todoItems = document.querySelectorAll(".todo-item");
  todoItems.forEach((item, index) => {
    setTimeout(() => {
      item.style.opacity = "1";
    }, index * 100);
  });

  // Confirm before deleting
  const deleteForms = document.querySelectorAll('form[action*="delete"]');
  deleteForms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      if (!confirm("Are you sure you want to delete this item?")) {
        e.preventDefault();
      }
    });
  });
});
