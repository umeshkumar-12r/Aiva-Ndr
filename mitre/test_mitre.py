from correlation.test_correlation import events
from correlation.engine import correlate_events

from hypothesis.engine import generate_hypotheses
from mitre.mapper import map_mitre_techniques


activities = correlate_events(events)

hypotheses = generate_hypotheses(activities)


for hypothesis in hypotheses:

    activity_id = hypothesis.hypothesis_id.replace(
        "hyp-",
        ""
    )

    activity = next(
        (
            activity
            for activity in activities
            if activity.activity_id == activity_id
        ),
        None
    )

    if activity is None:
        continue

    techniques = map_mitre_techniques(
        hypothesis,
        activity
    )

    print("\n======================")
    print("MITRE ATT&CK")
    print("======================")

    for technique in techniques:

        print(
            technique.model_dump_json(indent=2)
        )
