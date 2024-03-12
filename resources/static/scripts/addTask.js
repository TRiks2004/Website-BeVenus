function addTask(groupId) {
    fetch('/add_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({groupId: groupId})
    })
    .then(response => {
        if (response.ok) {
            console.log('Task added successfully');
            // После успешного добавления задачи, обновляем содержимое списка
            updateTodoList(groupId);
        } else {
            console.error('Failed to add task');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateTodoList(groupId) {
    fetch('/get_todos?groupId=' + groupId)
    .then(response => response.json())
    .then(data => {
        // Очищаем текущий список задач
        const todoList = document.querySelector('.todo-list');
        todoList.innerHTML = '';

        // Перебираем полученные задачи и добавляем их в список
        data.todos.forEach(todo => {
            const listItem = document.createElement('li');
            listItem.className = 'todo-item';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = 'item' + todo.id;

            const label = document.createElement('label');
            label.htmlFor = 'item' + todo.id;
            label.textContent = todo.text;

            listItem.appendChild(checkbox);
            listItem.appendChild(label);
            todoList.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function addElementBeforeButton(groupId) {

    var lastTwelve = groupId.substr(-12);

    var addButton = document.querySelector('.group[name="' + lastTwelve + '"] .add-button[name="Add"]' );

    newHTML = "<p>Новый текст или HTML-разметка: " + groupId + "</p>";

    if (addButton) {
        // Добавляем HTML-разметку перед кнопкой "Add Task"
        addButton.insertAdjacentHTML('beforebegin', newHTML);
    } else {
        console.error('Кнопка "Add Task" не найдена');
    }
}


