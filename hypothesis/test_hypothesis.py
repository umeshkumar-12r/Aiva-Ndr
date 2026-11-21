from correlation.test_correlation import events
from correlation.engine import correlate_events

from hypothesis.engine import generate_hypotheses


activities = correlate_events(events)

hypotheses = generate_hypotheses(activities)


for hypothesis in hypotheses:
    print("\nHYPOTHESIS")

    print(
        hypothesis.model_dump_json(indent=2)
    )
