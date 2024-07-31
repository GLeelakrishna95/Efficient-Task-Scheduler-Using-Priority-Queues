import heapq

class TaskScheduler:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        # Add a new task to the priority queue
        heapq.heappush(self.task_queue, task)
        print(f"Added: {task}")

    def get_next_task(self):
        # Get the task with the highest priority (lowest number)
        if self.task_queue:
            next_task = heapq.heappop(self.task_queue)
            print(f"Next task: {next_task}")
            return next_task
        else:
            print("No tasks in the queue.")
            return None

    def peek_next_task(self):
        # Peek at the task with the highest priority without removing it
        if self.task_queue:
            next_task = self.task_queue[0]
            print(f"Next task (peek): {next_task}")
            return next_task
        else:
            print("No tasks in the queue.")
            return None

    def is_empty(self):
        # Check if the task queue is empty
        return len(self.task_queue) == 0
