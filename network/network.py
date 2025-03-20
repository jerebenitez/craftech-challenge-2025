from diagrams import Diagram, Cluster
from diagrams.aws.database import DDB, RDS
from diagrams.aws.compute import EB, ECS
from diagrams.aws.mobile import Amplify, APIGateway
from diagrams.onprem.client import Users
from diagrams.aws.network import ELB

with Diagram("Network Diagram", show=False):
    users = Users("Users")

    app = Amplify("Frontend App")

    with Cluster("Backend"):
        api = EB("Elastic Beanstalk")
        api >> [RDS("Relational Database"), DDB("NoSQL Database")]

    with Cluster("Microservices"):
        with Cluster("Cluster 1"):
            ms1 = ECS("Microservice 1")

        with Cluster("Cluster 2"):
            ms2 = ECS("Microservice 2")

        gateway2 = APIGateway("API Gateway")
        gateway2 >> ELB("Load balancer") >> [ms1, ms2]

    gateway = APIGateway("API Gateway")

    app >> gateway >> api
    api >> gateway2
    users >> app
