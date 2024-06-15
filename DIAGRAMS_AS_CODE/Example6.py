from diagrams import Diagram, Cluster, Edge
from diagrams.azure.analytics import Databricks
from diagrams.azure.database import CosmosDb
from diagrams.azure.storage import BlobStorage
from diagrams.azure.devops import Pipelines
from diagrams.onprem.client import Users

with Diagram("Time Series Forecasting Model Deployment in Azure Databricks", show=False):

    with Cluster("Azure Databricks"):
        databricks = Databricks("Databricks")

        with Cluster("Data Preparation"):
            blob_storage = BlobStorage("Blob Storage")
            cosmos_db = CosmosDb("Cosmos DB")

        with Cluster("Model Training"):
            databricks = Databricks("Databricks")

        with Cluster("Model Deployment"):
            pipelines = Pipelines("Azure Pipelines")

    users = Users("Users")

    users >> Edge(label="Data", color="blue") >> blob_storage
    blob_storage >> Edge(color="blue") >> databricks
    databricks >> Edge(color="blue") >> cosmos_db
    cosmos_db >> Edge(label="Training Data", color="blue") >> databricks
    databricks >> Edge(color="blue") >> pipelines
    pipelines >> Edge(color="blue") >> users
