# Todo FastAPI Bootcamp

A modern, full-featured Todo List application built with FastAPI and Jinja2 templating. This project demonstrates CRUD operations with a clean, responsive web interface.

## Features

- ✅ **Add Tasks** - Create new todo items with validation
- ✏️ **Edit Tasks** - Inline editing with current value as placeholder
- 🗑️ **Delete Tasks** - Remove tasks with confirmation
- 🎨 **Modern UI** - Clean, responsive design with Tailwind CSS
- 🔄 **Real-time Updates** - Immediate feedback after operations
- 📱 **Mobile Friendly** - Responsive design for all devices

## Tech Stack

- **Backend**: FastAPI (Python web framework)
- **Templating**: Jinja2 (HTML templating engine)
- **Styling**: Tailwind CSS (utility-first CSS framework)
- **Data Storage**: JSON file-based storage
- **Icons**: Custom SVG icons for actions

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todo-fastapi-bootcamp
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Open your browser**
   Navigate to `http://localhost:8000`

## API Endpoints

### GET `/`
- **Description**: Main page displaying all tasks
- **Response**: HTML page with task list and add form

### POST `/add`
- **Description**: Add a new task
- **Parameters**: 
  - `task` (string): The task description
- **Response**: Redirects to main page with success message

### POST `/edit`
- **Description**: Edit an existing task
- **Parameters**:
  - `task_id` (string): ID of the task to edit
  - `new_task` (string): New task description
- **Response**: Redirects to main page with updated task

### POST `/delete`
- **Description**: Delete a task
- **Parameters**:
  - `task_id` (string): ID of the task to delete
- **Response**: Redirects to main page with task removed

## Project Structure

```
todo-fastapi-bootcamp/
├── main.py              # FastAPI application and routes
├── templates/
│   └── todolist.html    # Jinja2 template for the UI
├── db.json              # JSON database for task storage
├── requirements.txt     # Python dependencies
├── README.md           # This documentation
└── venv/               # Virtual environment (not in git)
```

## Usage

### Adding a Task
1. Type your task in the input field at the bottom
2. Click "Add Task" or press Enter
3. The task will appear in the list above

### Editing a Task
1. Hover over any task to reveal action buttons
2. Type your changes in the edit input field (shows current value as placeholder)
3. Click the pencil icon to save changes

### Deleting a Task
1. Hover over any task to reveal action buttons
2. Click the dustbin icon to delete the task
3. The task will be immediately removed

## Data Storage

Tasks are stored in `db.json` with the following structure:
```json
{
  "1": "First task",
  "2": "Second task",
  "3": "Third task"
}
```

Task IDs are auto-generated as sequential numbers.

## Development

### Running in Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Key Implementation Details

- **Redirect Handling**: Uses HTTP 303 status code for proper POST-to-GET redirects
- **Input Validation**: Server-side validation for empty task names
- **Error Handling**: Graceful error handling with user feedback
- **Responsive Design**: Mobile-first approach with Tailwind CSS

## Customization

### Styling
The application uses Tailwind CSS classes. You can customize the appearance by modifying the classes in `templates/todolist.html`.

### Icons
SVG icons are embedded directly in the HTML. You can replace them with different icons by modifying the SVG paths in the template.

### Database
To use a different storage backend, modify the file operations in `main.py` to use your preferred database.

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

If you encounter any issues or have questions, please open an issue in the repository.