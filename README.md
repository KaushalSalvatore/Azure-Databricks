#### Azure-Databricks

-  **Azure Databricks** is a fast, easy to use, and collaborative Apache Spark-based analytics platform optimized for Azure. It makes it  easy to process large datasets, train machine learning models, and run real-time queries on streaming data

- An interactive workspace for data engineers, data scientists, and analysts.
- Integration with Azure services like ADLS, Synapse, Key Vault, etc.
- Support for various programming languages (Python, Scala, SQL, R, Java).

##### Key Components of Azure Databricks

**Workspace**

- A collaborative environment where notebooks, libraries, dashboards, and experiments can be created and shared.

**Clusters**
- Cluster = Set of VMs where Spark jobs are executed.
- Types:
- **Interactive (All-purpose)**: Used for development, notebooks.
- **Job Cluster**: Spawned automatically for scheduled jobs.

**Notebook**
- A web-based interface where code can be written in Python, Scala, SQL, R.
- Supports visualizations and markdown.

**Jobs**
- Used to schedule and run notebooks or JAR/whl files as automated tasks.

**Libraries**
- External packages (e.g., PyPI, Maven) that are installed on clusters.

**DBFS (Databricks File System)**
- A distributed file system layer over cloud object storage like Azure Data Lake Storage (ADLS) or Blob Storage.

**Delta Lake**
- An open-source storage layer providing ACID transactions, schema enforcement, and time travel for big data.

**Databricks Runtime**
- A set of core components (Apache Spark, ML libraries, Delta Lake) optimized by Databricks.

**Architecture Diagram**

```
          +--------------------+
          |   Azure Services   |  (ADLS, Synapse, Blob, Key Vault)
          +--------------------+
                   |
           +----------------+
           | Azure Databricks |
           +----------------+
        Workspace   Clusters   Jobs
            |           |        |
       Notebooks   Spark Engine  |
                      /   \     |
                Driver   Executors

```