from correlation.correlated_activity import CorrelatedActivity
from backend.app.models.hypothesis import Hypothesis


def generate_hypotheses(
    activities: list[CorrelatedActivity],
) -> list[Hypothesis]:

    hypotheses = []

    for activity in activities:

        has_suricata = "suricata" in activity.source_tools
        has_alert = "alert" in activity.event_types

        if has_suricata and has_alert:

            hypothesis = Hypothesis(
                hypothesis_id=f"hyp-{activity.activity_id}",

                title="Possible suspicious network activity",

                status="investigating",

                confidence=0.40,

                source_ip=activity.source_ip,

                related_events=activity.event_ids,

                reason=(
                    "The activity contains a Suricata alert "
                    "and multiple related network events."
                ),
            )

            hypotheses.append(hypothesis)

    return hypotheses
