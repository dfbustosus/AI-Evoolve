from diagrams import Cluster, Diagram, Edge
from diagrams.azure.analytics import Databricks
from diagrams.azure.compute import VM
from diagrams.azure.database import CosmosDb
from diagrams.azure.storage import BlobStorage
from diagrams.azure.devops import Pipelines
from diagrams.azure.network import ApplicationGateway

with Diagram("Azure Databricks ML Recommendation Service", show=False):
    ingress = ApplicationGateway("ingress")

    with Cluster("Data Processing"):
        databricks = Databricks("Azure Databricks")
        model = VM("ML Model")

    with Cluster("Storage"):
        data_storage = BlobStorage("Data Storage")
        database = CosmosDb("Database")

    devops = Pipelines("CI/CD Pipeline")

    ingress >> Edge(color="darkgreen") >> databricks
    databricks >> Edge(color="darkorange") >> model
    databricks >> Edge(color="blue") >> data_storage
    model >> Edge(color="purple") >> database
    database >> Edge(color="darkred") >> ingress
    devops >> Edge(color="black", style="dashed") >> databricks
