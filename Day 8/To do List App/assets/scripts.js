// Getting The TODO item nd put it into an array
function get_todos() {
    var todos = new Array;
    var todos_str = localStorage.getItem('todo');
    if (todos_str !== null) {
        todos = JSON.parse(todos_str);
    }
    return todos;
}

// Adding the todo item to the adding existing todos
function add() {
    // This get whatever value the user typed in the input field.
    var task = document.getElementById('task-input').value;

    // this call the get_todos() function
    var todos = get_todos();
    // push or append to task
    todos.push(task);
    // JSON.stringy allows us to store the return string using localStorage.setItem
    localStorage.setItem('todo', JSON.stringify(todos));

    show();

    // This avoid further acton the user make. even if the user click submit.
    return false;
}

// This clear any value a user input in the input field after clicking on add todo
function clearDefault(a) {
    if (a.defaultValue == a.value) { a.value = "" }

};

// This remove todos on clicked
function remove() {
    var id = this.getAttribute('id');
    var todos = get_todos();
    todos.splice(id, 1);
    localStorage.setItem('todo', JSON.stringify(todos));

    show();

    return false;
}

// This display the created todo manually usin
function show() {
    var todos = get_todos();

    var html = '<ul>';
    for (var i = 0; i < todos.length; i++) {
        html += '<li>' + todos[i] + '<button class="remove" id="' + i + '">Delete</button> </li>';
    };
    html += '</ul>';

    document.getElementById('todos').innerHTML = html;

    var buttons = document.getElementsByClassName('remove');
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', remove);
    };
}

document.getElementById('add').addEventListener('click', add);
show();