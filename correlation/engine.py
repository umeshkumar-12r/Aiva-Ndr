from datetime import timedelta

from backend.app.models.normalized_event import NormalizedEvent
from correlation.correlated_activity import CorrelatedActivity


CORRELATION_WINDOW_SECONDS = 60


def correlate_events(
    events: list[NormalizedEvent],
) -> list[CorrelatedActivity]:

    if not events:
        return []

    events = sorted(events, key=lambda event: event.timestamp)

    activities = []
    current_events = []

    for event in events:

        if not current_events:
            current_events.append(event)
            continue

        last_event = current_events[-1]

        same_source = (
            event.source_ip == last_event.source_ip
        )

        within_window = (
            event.timestamp - last_event.timestamp
            <= timedelta(seconds=CORRELATION_WINDOW_SECONDS)
        )

        if same_source and within_window:
            current_events.append(event)

        else:
            activities.append(
                build_activity(current_events)
            )

            current_events = [event]

    if current_events:
        activities.append(
            build_activity(current_events)
        )

    return activities


def build_activity(
    events: list[NormalizedEvent],
) -> CorrelatedActivity:

    return CorrelatedActivity(
        activity_id=f"activity-{events[0].event_id}",

        source_ip=events[0].source_ip,

        start_time=events[0].timestamp,

        end_time=events[-1].timestamp,

        event_ids=[
            event.event_id
            for event in events
        ],

        event_count=len(events),

        event_types=list({
            event.event_type
            for event in events
        }),

        source_tools=list({
            event.source_tool
            for event in events
        }),
    )
