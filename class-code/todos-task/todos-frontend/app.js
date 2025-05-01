// API URLs from environment variables (would be injected at runtime in K8s)
// For local development, we check localStorage first
const API_URLS = {
  users:
    window.ENV?.USERS_API_URL ||
    localStorage.getItem("USERS_API_URL") ||
    "http://users-svc.default:5001",
  auth:
    window.ENV?.AUTH_API_URL ||
    localStorage.getItem("AUTH_API_URL") ||
    "http://auth-svc.default:5002",
  todos:
    window.ENV?.TODOS_API_URL ||
    localStorage.getItem("TODOS_API_URL") ||
    "http://todos-svc.default:5003",
};

// DOM Elements
const loginForm = document.getElementById("login-form");
const todoForm = document.getElementById("todo-form");
const loginContainer = document.getElementById("login-container");
const todosContainer = document.getElementById("todos-container");
const todosList = document.getElementById("todos-list");
const userNameSpan = document.getElementById("user-name");
const logoutBtn = document.getElementById("logout-btn");

// Status Elements
const usersStatus = document.getElementById("users-status");
const authStatus = document.getElementById("auth-status");
const todosStatus = document.getElementById("todos-status");

// Current User State
let currentUser = null;
let currentUserId = localStorage.getItem("currentUserId");
let currentUsername = localStorage.getItem("currentUsername");

// Check Service Status
async function checkServiceStatus() {
  // Check Users API
  try {
    const usersResponse = await fetch(`${API_URLS.users}/health`);
    if (usersResponse.ok) {
      usersStatus.textContent = "Users: Online";
      usersStatus.className = "status-badge status-up";
    } else {
      throw new Error("Users API not responding properly");
    }
  } catch (error) {
    usersStatus.textContent = "Users: Offline";
    usersStatus.className = "status-badge status-down";
  }

  // Check Auth API
  try {
    const authResponse = await fetch(`${API_URLS.auth}/healthz`);
    if (authResponse.ok) {
      authStatus.textContent = "Auth: Online";
      authStatus.className = "status-badge status-up";
    } else {
      throw new Error("Auth API not responding properly");
    }
  } catch (error) {
    authStatus.textContent = "Auth: Offline";
    authStatus.className = "status-badge status-down";
  }

  // Check Todos API
  try {
    const todosResponse = await fetch(`${API_URLS.todos}/healthz`);
    if (todosResponse.ok) {
      todosStatus.textContent = "Todos: Online";
      todosStatus.className = "status-badge status-up";
    } else {
      throw new Error("Todos API not responding properly");
    }
  } catch (error) {
    todosStatus.textContent = "Todos: Offline";
    todosStatus.className = "status-badge status-down";
  }
}

// Login Handler
async function handleLogin(e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    // Get all users from users API
    const usersResponse = await fetch(`${API_URLS.users}/users`);
    if (!usersResponse.ok) {
      throw new Error("Failed to get users list");
    }

    const usersData = await usersResponse.json();

    // Find user based on username
    const user = usersData.users.find((u) => u.name === username);
    if (!user) {
      throw new Error("User not found");
    }

    // Try to authenticate with auth service
    const authResponse = await fetch(`${API_URLS.auth}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    });

    if (!authResponse.ok) {
      throw new Error("Authentication failed");
    }

    // Store user info
    currentUser = user;
    currentUserId = user.id;
    currentUsername = username;

    localStorage.setItem("currentUserId", currentUserId);
    localStorage.setItem("currentUsername", currentUsername);

    // Update UI
    userNameSpan.textContent = username;
    loginContainer.classList.add("hidden");
    todosContainer.classList.remove("hidden");

    // Load todos
    loadTodos();
  } catch (error) {
    alert("Login failed: " + error.message);
  }
}

// Load Todos
async function loadTodos() {
  if (!currentUserId) return;

  try {
    const response = await fetch(
      `${API_URLS.todos}/todos?user_id=${currentUserId}`
    );
    if (!response.ok) {
      throw new Error("Failed to load todos");
    }

    const data = await response.json();
    renderTodos(data.todos || []);
  } catch (error) {
    alert("Failed to load todos: " + error.message);
  }
}

// Render Todos
function renderTodos(todos) {
  todosList.innerHTML = "";

  if (todos.length === 0) {
    todosList.innerHTML =
      '<div class="empty-message">No todos yet. Add one above!</div>';
    return;
  }

  todos.forEach((todo) => {
    const todoItem = document.createElement("div");
    todoItem.className = "todo-item";
    todoItem.dataset.id = todo.id;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "todo-checkbox";
    checkbox.checked = todo.completed;
    checkbox.addEventListener("change", () =>
      toggleTodo(todo.id, checkbox.checked)
    );

    const todoText = document.createElement("span");
    todoText.className =
      "todo-text" + (todo.completed ? " todo-completed" : "");
    todoText.textContent = todo.title;

    const deleteBtn = document.createElement("button");
    deleteBtn.className = "btn danger";
    deleteBtn.textContent = "Delete";
    deleteBtn.addEventListener("click", () => deleteTodo(todo.id));

    todoItem.appendChild(checkbox);
    todoItem.appendChild(todoText);
    todoItem.appendChild(deleteBtn);
    todosList.appendChild(todoItem);
  });
}

// Add Todo
async function addTodo(title) {
  if (!currentUserId) return;

  try {
    const response = await fetch(`${API_URLS.todos}/todos`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        user_id: parseInt(currentUserId),
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to add todo");
    }

    // Refresh todos list
    loadTodos();
  } catch (error) {
    alert("Failed to add todo: " + error.message);
  }
}

// Toggle Todo (complete/incomplete)
async function toggleTodo(id, completed) {
  try {
    const response = await fetch(`${API_URLS.todos}/todos/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ completed }),
    });

    if (!response.ok) {
      throw new Error("Failed to update todo");
    }

    // Update the UI without full reload
    const todoText = document.querySelector(
      `.todo-item[data-id="${id}"] .todo-text`
    );
    if (todoText) {
      if (completed) {
        todoText.classList.add("todo-completed");
      } else {
        todoText.classList.remove("todo-completed");
      }
    }
  } catch (error) {
    alert("Failed to update todo: " + error.message);
    // Reload in case of error
    loadTodos();
  }
}

// Delete Todo
async function deleteTodo(id) {
  try {
    const response = await fetch(`${API_URLS.todos}/todos/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error("Failed to delete todo");
    }

    // Remove from DOM without full reload
    const todoItem = document.querySelector(`.todo-item[data-id="${id}"]`);
    if (todoItem) {
      todoItem.remove();

      // Check if list is now empty
      if (todosList.children.length === 0) {
        todosList.innerHTML =
          '<div class="empty-message">No todos yet. Add one above!</div>';
      }
    }
  } catch (error) {
    alert("Failed to delete todo: " + error.message);
    // Reload in case of error
    loadTodos();
  }
}

// Logout Function
function logout() {
  // Call the logout endpoint
  fetch(`${API_URLS.auth}/auth/logout`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  }).catch((err) => console.error("Logout error:", err));

  // Clear user info
  currentUser = null;
  currentUserId = null;
  currentUsername = null;

  localStorage.removeItem("currentUserId");
  localStorage.removeItem("currentUsername");

  // Reset forms
  loginForm.reset();
  todoForm.reset();

  // Switch views
  loginContainer.classList.remove("hidden");
  todosContainer.classList.add("hidden");
}

// Event Listeners
loginForm.addEventListener("submit", handleLogin);

todoForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("todo-title").value.trim();
  if (title) {
    addTodo(title);
    document.getElementById("todo-title").value = "";
  }
});

logoutBtn.addEventListener("click", logout);

// Initialize the app
function init() {
  checkServiceStatus();

  // Check if we have a stored user ID and try to auto-login
  if (currentUserId && currentUsername) {
    userNameSpan.textContent = currentUsername;
    loginContainer.classList.add("hidden");
    todosContainer.classList.remove("hidden");
    loadTodos();
  }

  // Check service status periodically
  setInterval(checkServiceStatus, 30000); // every 30 seconds
}

// Start the app
init();
