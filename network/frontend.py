from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.aws.compute import AppRunner
from diagrams.aws.storage import S3
from diagrams.aws.network import CF
from diagrams.onprem.monitoring import Sentry

with Diagram("", show=False):
    with Cluster("Frontend"):
        app = AppRunner("Frontend App")
        CF("Cloudfront") >> [
                S3("Static assets"),
                app
            ]

    app >> [
            Sentry("Sentry"),
            Custom("PostHog", "./assets/posthog.png")
        ]
