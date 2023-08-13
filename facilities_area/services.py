from facilities_area.models import Event, Task


class EventService:
    """class to encapsulate reusable logic of handling events"""

    def create(self, new_event: dict):
        """when created new event, also will be created two default tasks"""

        created_event = Event.objects.create(**new_event)
        open_event_task = Task(
            title=f"Открытие мероприятия {created_event.title}",
            event=created_event,
            reward=12,
        )
        close_event_task = Task(
            title=f"Закрытие мероприятия {created_event.title}",
            event=created_event,
            reward=12,
        )
        Task.objects.bulk_create((open_event_task, close_event_task))

        return created_event
