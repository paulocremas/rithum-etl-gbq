# Connecting Rithum data to Looker through API and Google BigQuery

### Context

This project aims to integrate Rithum API data into Looker to automate sales reporting. Key data points include:

* Sales volume (quantity sold);
* Revenue;
* Supplier name.

The goal is to build a Looker dashboard tracking sales by supplier, with daily automatic updates for accurate, real-time insights.

---

### Approach 1
#### Python + Lambda + Google BigQuery

A flexible, serverless approach for processing data at scale, leveraging cloud-native services with pay-per-use pricing for cost efficiency.

Implementation Overview:
Rithum API will be integrated using Python in an AWS Lambda function, triggered on-demand or via a scheduler (e.g., EventBridge).
Processed data will be stored in Google BigQuery.
Looker Studio will connect directly to BigQuery for visualization.

Advantages:
Scalable & serverless – Handles large data volumes without managing infrastructure.
Cost-effective – Pay only for compute (Lambda) and storage (BigQuery) used.
Automation-friendly – Lambda can be scheduled or event-driven.

![Diagram 1st approach](https://github.com/user-attachments/assets/f9b0a3aa-329d-42b8-85b4-393cb3934277)

---
 
### Approach 2 (Tiny Data)
#### Apps Script + Google Sheets

A lightweight, cost-effective approach for processing limited data volumes without the need for scalable infrastructure or additional investments.

Implementation Overview:
Rithum API will be integrated via Google Apps Script, running directly within Google Sheets (hosted on Google Drive).
Processed data will be visualized in Looker Studio for reporting and analytics.

Advantages:
Minimal infrastructure – No external servers or complex setup required.
Direct data access – Users can manage the database Google Sheets.

Operational Considerations:
Small data volumes only – Optimized for low to moderate processing needs.
Not scalable – Not suitable for large-scale or high-performance workloads.

![Diagram 2nd approach](https://github.com/user-attachments/assets/4d2a998c-389c-4a05-9e3a-8b9234d6e5f5)

---

### Approach 3 (Big Data)
#### Dataflow + Apache Beam (Python) + Google BigQuery

A cloud-native data processing solution designed for high-throughput, scalable workloads with enterprise-grade performance.

Implementation Overview:
Rithum API will be integrated via Apache Beam (Python) and executed on Google Dataflow, enabling distributed data processing.
Processed data will be stored in Google BigQuery for analytics and visualized in Looker Studio for reporting.

Advantages:
Massively Scalable Processing – Apache Beam on Dataflow enables distributed, parallel execution, handling high-volume data with ease.
Enterprise-Grade Reliability – Built-in fault tolerance, monitoring, and auto-recovery for mission-critical pipelines.

Operational Considerations:
More expensive – Overkill for simple tasks.

![Diagram 3rd approach](https://github.com/user-attachments/assets/c6342e02-2cd8-4f49-ac46-667b383e30b0)

