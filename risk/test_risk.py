from correlation.test_correlation import events
from correlation.engine import correlate_events

from hypothesis.engine import generate_hypotheses
from evidence.engine import evaluate_hypothesis

from risk.engine import calculate_assessment


activities = correlate_events(events)

hypotheses = generate_hypotheses(activities)


for hypothesis in hypotheses:

    matching_activity = None

    for activity in activities:

        activity_id = hypothesis.hypothesis_id.replace(
            "hyp-", ""
        )

        if activity.activity_id == activity_id:
            matching_activity = activity
            break

    if matching_activity is None:
        continue

    evidence = evaluate_hypothesis(
        hypothesis,
        matching_activity
    )

    assessment = calculate_assessment(
        hypothesis,
        evidence
    )

    print("\n==========================")
    print("RISK ASSESSMENT")
    print("==========================")

    print(
        f"Risk: {assessment['risk']}"
    )

    print(
        f"Confidence: "
        f"{assessment['confidence'] * 100:.0f}%"
    )
