from correlation.test_correlation import events
from correlation.engine import correlate_events

from hypothesis.engine import generate_hypotheses
from evidence.engine import evaluate_hypothesis


# Step 1: Correlate events
activities = correlate_events(events)

# Step 2: Generate hypotheses
hypotheses = generate_hypotheses(activities)


# Step 3: Evaluate hypotheses
for hypothesis in hypotheses:

    matching_activity = None

    for activity in activities:

        if activity.activity_id == hypothesis.hypothesis_id.replace(
            "hyp-", ""
        ):
            matching_activity = activity
            break

    if matching_activity is None:
        continue

    evidence = evaluate_hypothesis(
        hypothesis,
        matching_activity
    )

    print("\n==============================")
    print("HYPOTHESIS")
    print("==============================")

    print(
        hypothesis.model_dump_json(indent=2)
    )

    print("\nEVIDENCE")
    print("==============================")

    for item in evidence:

        print(
            item.model_dump_json(indent=2)
        )
