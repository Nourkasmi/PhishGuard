from app import create_app
from models import Event, Target

app = create_app()

with app.app_context():
    events = Event.query.all()

    if not events:
        print('No events recorded yet.')
    else:
        print(f'Total events recorded: {len(events)}')
        print('-' * 40)
        for event in events:
            target = Target.query.get(event.target_id)
            print(f'Event: {event.event_type}')
            print(f'Target: {target.first_name} {target.last_name}')
            print(f'IP: {event.ip_address}')
            print(f'Time: {event.timestamp}')
            print('-' * 40)