import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    """Add a new task."""
    title = input("\nColoque o titulo da sua tarefa: ").strip()
    hour = input("Coloque a hora da sua tarefa: ").strip()
    if title:
        tasks.append({"title": title, "hour": hour, "Completa": False})
        save_tasks(tasks)
        print("✓ tarefa adicionada!")
    else:
        print("✗ O título da tarefa não pode ser vazio.")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNenhuma tarefa encontrada.")
        return
    
    print("\n--- Tarefas ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["Completa"] else "○"
        print(f"{i}. [{status}] {task['Titulo']}")

def mark_completed(tasks):
    """Marca a tarefa como completa."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        index = int(input("\nDigite o número da tarefa para marcar como completa: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["Completa"] = True
            save_tasks(tasks)
            print("✓ Tarefa marcada como completa!")
        else:
            print("✗ Número de tarefa inválido.")
    except ValueError:
        print("✗ Por favor, digite um número válido.")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        index = int(input("\nDigite o número da tarefa para excluir: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"✓ Tarefa '{removed['title']}' excluída!")
        else:
            print("✗ Número de tarefa inválido.")
    except ValueError:
        print("✗ Por favor, digite um número válido.")

def show_menu():
    """Display the main menu."""
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Marcar tarefa como completa")
    print("4. Excluir tarefa")
    print("5. Sair")

def main():
    """Main program loop."""
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("\nDigite sua escolha (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nAté mais!")
            break
        else:
            print("✗ Escolha inválida. Por favor, digite um número entre 1 e 5.")

if __name__ == "__main__":
    main()
    