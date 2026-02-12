# Case Study: LGPD Audit & Observability Module

**Project:** Holocron Sentinel (Compliance System)
**Role:** Cloud Security Architect
**Tech Stack:** AWS (EC2, CloudWatch, AWS Config, Systems Manager), Python (Boto3).

---

## The Challenge
Under **LGPD Article 37**, companies must keep a record of personal data processing operations. The client's legacy infrastructure lacked centralized logging, making it impossible to answer "Who accessed this data?" during an audit, exposing the firm to severe regulatory fines.

## The Solution
I architected a "Glass Box" observability framework integrated directly into the deployment pipeline:

*   **Infrastructure as Code (IaC):** Utilized **AWS Systems Manager (SSM)** Parameter Store to manage CloudWatch Agent configurations centrally, enabling immutable infrastructure practices.
*   **Deep Monitoring:** Deployed **CloudWatch Agent** to capture granular metrics (Memory Usage, Disk I/O) unavailable in standard monitoring.
*   **Log Aggregation:** Configured real-time streaming of Apache Access/Error logs to **CloudWatch Logs**, implementing **Metric Filters** to parse specifically for HTTP 404 anomalies.
*   **Automated Response:** Engineered **EventBridge** rules to trigger alerts on critical state changes (Stop/Terminate) and **SNS** topics for immediate team notification.
*   **Governance:** Activated **AWS Config** rules to enforce tagging policies and identify unattached EBS volumes (Cost Optimization).

## Key Results
*   **100% Visibility** into internal instance health (RAM/Swap).
*   **Proactive Security:** Web scanning attempts detected in < 1 minute via 404 rate alarms.
*   **Operational Efficiency:** Eliminated the need for SSH access for log retrieval, enhancing security posture.

---

### *Competencies Demonstrated*
`#AWSCloud` `#Observability` `#DevOps` `#CloudSecurity` `#SystemsManager` `#Troubleshooting`
