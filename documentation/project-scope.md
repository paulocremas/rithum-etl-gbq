### Project Scope for Estimated Development Time

#### This document contains information about the estimated development time and a detailed breakdown of the planned processes.
---

## Development Plan

Following our meeting and understanding of the project requirements, I’ve broken the work down into **four key stages**:

1. [API Integration](#api-integration)
2. Google BigQuery Integration  
3. Dashboard Development  
4. Project Deployment

#### Observation
To generate the desired sales chart discussed during the meeting, we will extract data specifically from the **items within orders**, selecting only the necessary fields. This approach allows for a visualization that reflects the actual sale dates of the items.

An important point:  
- Can orders be **canceled or returned**?
- If so, should these items be **excluded** from the final metrics?
  
If confirmed, the script will need logic to identify and exclude canceled items, likely by checking for a **status update**.

---

## Estimated Hours
<a id="api-integration"></a>
#### 1. API Integration
