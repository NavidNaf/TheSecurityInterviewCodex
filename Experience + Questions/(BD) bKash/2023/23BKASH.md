# bKash (Bangladesh) Fintech Offensive Security Engineer Interview

| Field | Details |
| --- | --- |
| Position/Role | Engineer, Offensive Security & Compliance |
| Organization | bKash Ltd. |
| Term | Full-Time Employment |
| Role Description | Focuses on applying technical expertise in offensive security and penetration testing. |
| Knowledge Requirement | Penetration testing, web and mobile application security, vulnerability assessment, exploit validation, security compliance, and strong offensive security fundamentals. |

## Details

This was an assessment I prepared for the interview process at bKash Fintech Limited. The overall process was divided into four stages:

1. Resume screening
2. Technical assessment
3. Presentation on the submitted solutions
4. HR and final non-technical interview

## Assessment Questions

### Assessment Docker Image

- [bk-osrassessment Docker image](https://hub.docker.com/repository/docker/navidnaf/bk-osrassessment/general)

Candidates could pull the Docker image and solve the assessment tasks from there. The assessment included Python scripting, web vulnerability assessment, basic Android reverse engineering, and situational security questions.

### Python Problem Solving

#### URL Encoding

Write a Python script to URL-encode the following URLs. Clean code and proper comments were expected, and the `.py` file had to be submitted.

```text
https://api.example.com/v1/users/123456/profile/image.jpg?size=large&crop=true
https://www.example.com/blog/post/my-first-post/comment/54321#comment-54321
```

#### Custom Keyword Generator

Two CSV files were provided: `users.csv` and `pass.csv`. The task was to read both files and generate custom keywords using this format:

```text
User[first 3 letters]:Pass[last 4 letters]
```

For example, if the username was `Xenophilius` and the password was `abcd!@#$`, the generated keyword would be `Xen!@#$`. The expected submission was the Python script and the generated `keywords.txt` file.

#### HTTP Response Headers

Write a Python script to request `https://www.bkash.com` and print the response headers. The expected submission was a properly commented `.py` file.

### Web Vulnerability Assessment

#### Web VA Report

Perform a vulnerability assessment on `https://ginandjuice.shop`, identify key vulnerabilities, and map them to the OWASP Top 10. Open-source tools were allowed, but the report needed to provide clear insight for each issue.

The report was expected to include:

- Vulnerability name
- Proof of concept
- OWASP mapping
- Remediation remarks

Submission format: `.docx`, `.ppt`, or `.pdf`.

#### Enumeration Task

The question asked: while doing enumeration, what is the best weapon in your arsenal? The task was to perform enumeration on the same website used in the web vulnerability assessment and include screenshots in the Web VA report.

### Mobile Application Basic RE

Reverse the provided `.apk` file and find the resource that resembles bKash. The instruction also warned not to get misled.

The expected submission was a document describing the process and including a snapshot of the finding. Submission format: `.docx`, `.ppt`, or `.pdf`.

### Situational Questions

- Given the discovery of TLSv1.0 on a website's communication, describe the steps you would take to create a proof of concept that demonstrates the vulnerability. What tools and techniques would you use, and how would you assess the risk of the website still using TLSv1.0?
- In a general scenario, how would you know that Kubernetes is working on a server? Please provide your identification methodology. 
- You are hired as a pentester to test the security of a website. During your testing, you notice that the website is not setting any security headers. What would you do? Which security headers would you suggest for the team to implement based on the website’s usage? 
- You are a penetration tester for a security company. You have been tasked with identifying the operating system of https://scanme.org – what would you do to identify the OS? Please provide any list of commands or list of tools or methods you will employ to perform the task. 
- You've identified 10 CVEs associated with a vulnerable or outdated component via a Vulnerability Assessment in a system. Explain your approach to prove the existence of these CVEs and assess the system's security posture. How would you verify the accuracy of the information related to these CVEs, and what sources or tools would you use to gather additional intelligence about them?
