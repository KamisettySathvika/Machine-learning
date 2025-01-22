class Todo_Item:
    priority_options = ["High", "Medium", "Low"]

    def __init__(self, task: str, priority: str = None, done: bool = False):
        if type(task) == str:
            if task:
                self.task = task
            else:
                raise Exception("Task should not be empty")
        else:
            raise Exception("Task needs to be a string")

        if type(done) == bool:
            self.done = done
        else:
            raise Exception("Done argument needs to be a boolean")

        if priority:
            if priority in Todo_Item.priority_options:
                self.priority = priority
            else:
                raise Exception(
                    f"priority setting should be one of {Todo_Item.priority_options}")
        else:
            self.priority = None

    def __str__(self):
        return f'[{"x" if self.done else "o"}] - {self.priority if self.priority else "None"} : {self.task}'

    def finish(self):
        self.done = True

    def raise_priority(self):
        if not self.priority:
            return

        if self.priority == "Low":
            self.priority = "Medium"
        if self.priority == "Medium":
            self.priority = "High"


class Todo_List:
    def __init__(self, owner: str, todo_list: list = []):
        for item in todo_list:
            if type(item) != Todo_Item:
                raise Exception(f"Expected Todo Item got {type(item)}")

        self.todo_items = todo_list

        if type(owner) == str:
            if owner:
                self.owner = owner
            else:
                raise Exception("Owner name should not be empty")
        else:
            raise Exception("Owner name needs to be a string")

    def __str__(self):
        output = f"{self.owner}'s ToDo List\n"

        for item in self.todo_items:
            output += str(item) + "\n"

        return output

    def info(self):
        pending_tasks = {"High": 0, "Medium": 0, "Low": 0}
        finished_tasks = 0

        for item in self.todo_items:
            if item.done:
                finished_tasks += 1
            else:
                if item.priority:
                    pending_tasks[item.priority] += 1

        pending_summary = ", ".join(
            [f"{priority} - {count}" for priority, count in pending_tasks.items()])

        print(f"{self.owner}'s Todo list\n\nPending Tasks: {len(self.todo_items) - finished_tasks} \n{pending_summary}\nFinished Tasks: {finished_tasks}\n------------")

    def add_todo_item(self, todo_item):
        if type(todo_item) == Todo_Item:
            self.todo_items.append(todo_item)
        else:
            raise Exception(
                f"ToDo item must be of datatype Todo_Item not {type(todo_item)}")

    def create_todo_item(self, task: str, priority: str = None, done: bool = False):
        item = Todo_Item(task, priority, done)
        self.todo_items.append(item)

    def search_todo_item(self, query):
        output = []

        for item in self.todo_items:
            if query.lower() in item.task.lower():
                output.append(item)

        return output

    def list_todo_items(self, priority: str = "All", done: bool = None, sort: bool = False):
        output1 = []
        
        for item in self.todo_items:
            if (done == True) and (item.done == True):
                output1.append(item)
            elif (done == False) and (item.done == False):
                output1.append(item)
            elif (done == None):
                output1.append(item)

        output2 = []

        if priority == "All":
            output2 = output1
        else:
            for item in output1:
                if priority == item.priority:
                    output2.append(item)

        
        if sort:
            priority_dict = {
                "High":[],
                "Medium":[],
                "Low":[],
                None:[],
                "Finished":[]
            }
            for item in output2:
                if item.done:
                    priority_dict["Finished"].append(item)
                else:
                    priority_dict[item.priority].append(item)
            
            output3 = priority_dict["High"] + priority_dict["Medium"] + priority_dict["Low"] + priority_dict[None] + priority_dict["Finished"]
        else:
            output3 = output2

        return output3

    # goes to the number and finishes that task
    def finish_todo_item(self, number):
        try:
            self.todo_items[number].finish()
        except IndexError:
            raise Exception("Invalid task number")

    # deletes the number item
    def delete_todo_item(self, number):
        try:
            del self.todo_items[number]
        except IndexError:
            raise Exception("Invalid task number")


# Sample items for demonstration
sample_items = [
    Todo_Item("Task 1", "High"),
    Todo_Item("Task 4", "Medium"),
    Todo_Item("Task 6", "Low", done=True),
    Todo_Item("Task 3", "High"),
    Todo_Item("Task 7", "Low", done=True),
    Todo_Item("Task 2", "High"),
    Todo_Item("Task 5", "Medium", done=True),
    Todo_Item("Task 11"),
    Todo_Item("Task 12", done=True),
    Todo_Item("Task 8", "Low"),
    Todo_Item("Task 9"),
    Todo_Item("Task 10", done=True),
]

# Create a Todo_List instance
sample_todo = Todo_List("Sample Person", sample_items)

# Print initial list
print("Initial Todo List:")
print(sample_todo)

# Finish task at index 0
try:
    sample_todo.finish_todo_item(0)
    print("\nTask at index 0 finished:")
    print(sample_todo)
except Exception as e:
    print(f"Error finishing task: {e}")

# Delete task at index 5
try:
    sample_todo.delete_todo_item(5)
    print("\nTask at index 5 deleted:")
    print(sample_todo)
except Exception as e:
    print(f"Error deleting task: {e}")
