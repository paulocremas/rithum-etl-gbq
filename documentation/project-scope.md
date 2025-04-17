### Project Scope for Estimated Development Time

#### This document contains information about the estimated development time and a detailed breakdown of the planned processes.
---

## Development Plan

Following our meeting and understanding of the project requirements, I’ve broken the work down into **six key stages**:

| Task | Total hours |
|----|---|
|1. [API Integration](#api-integration) | 18 |
|2. [Google BigQuery Integration](#gbq) | 7.5 |
|3. [Dashboard Development](#dashboard) | 3 |
|4. [E-mail Notificator (for errors and performance reports)](#email) | 2 |
|5. [Project Deployment](#deploy) | 8 |
|6. [Documentation](#doc) | 4.5 |
| Total | 43 |

#### Observation
To generate the desired sales chart discussed during the meeting, we will extract data specifically from the **items within orders**, selecting only the necessary fields. This approach allows for a visualization that reflects the actual sale dates of the items.

An important point:  
- Can orders be **canceled or returned**?
- If so, should these items be **excluded** from the final metrics?
  
If confirmed, the script will need logic to identify and exclude canceled items, likely by checking for a **status update**.

---

## Estimated Hours
<a id="api-integration"></a>
#### 1. API Integration (Total 18 hours)
 Estimated Time (in hours) | Task                                                               | Description                                                                                                                                                                       
---------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 3                         | Review API Documentation                                           | Understanding authentication, order endpoints, parameters, response format.                                                                                                       
 1                         | Environment Setup                                                  | Set up the project, install libraries (requests, [Postman](https://www.postman.com/) for testing).                                                                                                            
 2.5                       | Authentication Implementation                                      | Implement the flow using a refresh token to get an access token, handle token expiration, errors, etc.                                                                            
 3                         | API Call to Orders Endpoint                                        | Build the request with proper headers, query parameters, date/status filters, etc.                                                                                                
 1                         | Pagination Handling                                                | Handle pagination using `scrollId`. On the first request, Rithum returns a `scrollId` and the first page of results. Use this ID in subsequent calls to retrieve remaining pages. 
 2.5                       | Parsing the Response, Extracting Data and Creating Metadata Fields | Implementing the logic to parse the response format and extract the relevant order fields.                                                                                        
 3                         | Testing & Validation                                               | Ensure extracted data is accurate and complete.                                                                                                                                   
 1                         | Error Handling                                                     | Handle authentication errors, API limits, malformed data, etc.                                                                                                                    
 1                         | Code Documentation                                                 | Add comments and document key workflows.                                                                                                                                          

<a id="gbq"></a>
#### 2. Google BigQuery Integration  (Total 7.5 hours)

| Estimated Time (in hours)  | Task                           | Description                                                                                      |
|-----------------|--------------------------------|--------------------------------------------------------------------------------------------------|
| 1     | BigQuery Environment Setup   | Create GCP project, enable BigQuery API, create dataset and table(s)                               |
| 0.5      | Service Account & Auth       | Create a service account, generate a JSON key, and configure authentication in code                |
| 1       | Table Schema Design          | Define the table structure (columns, data types, normalization, etc.)                              |
| 2   | Data Upload Logic            | Implement data insertion using on the script |
| 0.5     | Metadata Table Creation            | Create a metadata table to store control info like `last_updated_at`.                 |
| 1     | Read & Update Metadata in Script   | Implement logic to read metadata before extracting data  |
| 0.5   | Validation  | Verify data consistency and run test queries                                                       |

<a id="dashboard"></a>
#### 3. Dashboard Development (Total 3 hours)
For the dashboard development, I estimate 3 hours to connect Looker to Google BigQuery, create the visualizations, implement interactive filters, and refine the overall layout and design.

<a id="email"></a>
#### 4. E-mail Notificator (Total 2 hours)
I estimate 2 hours to develop the notifier, integrate it with error handling, and implement logic to track performance metrics. 

<a id="deploy"></a>
#### 5. Project Deployment (Total 8 hours)

| **Estimated Time (in hours)** | **Task**                          | **Description**                                                                 |
|---------------------------|------------------------------------|---------------------------------------------------------------------------|
| 0.5                    | AWS Account Setup           | Configure IAM roles, permissions, and enable Lambda service.              |
| 1.5                     | Lambda Function Creation    | Package Python script with dependencies (`requests`, `google-cloud-bigquery`). |
| 1                       | Environment Variables       | Secure API keys and credentials using AWS Secrets Manager/KMS.            |
| 1                     | Trigger Configuration       | Set up EventBridge (CloudWatch Events) for scheduled execution.          |
| 3                     | Testing & Debugging         | Validate cold starts, timeouts, and memory settings (128MB–3GB).         |

#### **Key Cost Drivers**
- **Lambda Pricing**: ~$0.20/month (1M requests, 1GB memory).  
- **EventBridge**: ~$1/month (1M events).  
- **Secrets Manager**: ~$0.40/month per secret. (2 secrets estimated)

<a id="doc"></a>
#### 6. Documentation (Total 4.5 hours)
I estimate it will take 4.5 hours to document the script and its supporting infrastructure. (AWS Lambda and Google BigQuery) 
