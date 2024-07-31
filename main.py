def main():
    scheduler = TaskScheduler()

    # Add tasks to the scheduler
    scheduler.add_task(Task(priority=2, description="Complete project report"))
    scheduler.add_task(Task(priority=1, description="Prepare for meeting"))
    scheduler.add_task(Task(priority=3, description="Respond to emails"))

    # Peek at the next task
    scheduler.peek_next_task()

    # Get tasks based on priority
    while not scheduler.is_empty():
        scheduler.get_next_task()

if __name__ == "__main__":
    main()
