class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        # Priority queue needs to compare tasks based on their priority
        return self.priority < other.priority

    def __str__(self):
        return f"Task(priority={self.priority}, description='{self.description}')"
