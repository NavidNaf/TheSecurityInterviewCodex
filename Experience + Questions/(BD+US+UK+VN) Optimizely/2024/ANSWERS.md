## First Round Interview Questions (HR)

### Tell me a bit about yourself.

### What certifications do you have?

### Why are you applying to this job?

## Second Round Interview Questions (Technical)

### What is application security?

Application security is the practice of finding, preventing, and fixing security issues in software applications. It covers secure design, secure coding, code review, testing, vulnerability management, and working with developers to reduce risk.

### An image of an Nmap port scan output was given, and I was asked to explain what the open ports were used for. The ports were `21`, `22`, `443`, and `4444`.

Port `21` is usually FTP, port `22` is SSH, and port `443` is HTTPS. Port `4444` is commonly known as the default `LPORT` used by Metasploit payloads, such as `windows/x64/meterpreter/reverse_tcp`, for callback connections or reverse shells.

### What can you infer from port `4444` being open?

An open `4444` port can indicate a Metasploit-style callback listener or reverse shell, especially if it is not part of the expected service baseline. I would verify the process, network connections, service banner, and logs to confirm whether it is legitimate or suspicious.

### An image of a Tenable vulnerability scan was given, and I was asked to explain the listed findings. The findings included missing or misconfigured security headers, missing cookie flags such as `HttpOnly` and `SameSite`, and `Strict-Transport-Security` not being enabled.

- Missing or misconfigured security headers: This can weaken browser-side protections against issues like clickjacking, XSS impact, content injection, or insecure resource loading.
- Missing `HttpOnly` cookie flag: Without `HttpOnly`, client-side scripts may be able to access session cookies, which increases the impact of XSS.
- Missing `SameSite` cookie flag: Without `SameSite`, cookies may be sent in cross-site requests, which can increase CSRF risk.
- `Strict-Transport-Security` not enabled: Without HSTS, browsers may allow HTTP downgrade behavior and users may be more exposed to SSL stripping style attacks.

### Point out the vulnerabilities in `optiSourceCode.py`.

The code stores the valid password in plaintext and compares user input directly against it instead of using a salted password hash. It also compares the password character by character and returns early on mismatch, which can leak information through response-time differences.

### What is a SIEM, and why is it used?

A SIEM is a Security Information and Event Management system that collects and analyzes logs from different systems. It is used for monitoring, alerting, investigation, compliance, and detecting suspicious activity across an environment.

### What is correlation, and how is correlation used in incident response?

Correlation means connecting related events from different logs or systems to understand a bigger security story. In incident response, it helps identify attack patterns, reduce noise, and connect signals like failed logins, suspicious process execution, and network activity.

## Third Round Interview (Inter-Personal + Technical)

### Tell us a bit about yourself.

### Why are you interested in cybersecurity?

### How did you start your cybersecurity journey?

### They pointed to a project on my CV and asked how I built it.

### What is port `445`?

Port `445` is used for SMB over TCP, mainly for Windows file sharing, printer sharing, and domain-related communication. It is an important port to monitor because exposed or vulnerable SMB services have historically been abused in major attacks.

### If you find an entry point on port `445`, how would you approach it?

I would first identify the SMB version, host role, allowed authentication methods, and whether anonymous access is possible. Then I would check for known misconfigurations or vulnerabilities, validate findings carefully, and document the risk without disrupting the system.

### During forensic analysis, you find that a threat actor already entered through port `445`. How would you map that scenario into a red team activity?

I would map it as an initial access or lateral movement path involving SMB, depending on how the attacker used the service. I would also compare the observed TTPs, tools, indicators, and behavior with threat intelligence to see if it matches any known APT group. In a red team plan, I would recreate the behavior in a controlled way, define detection opportunities, and show how the organization can harden SMB exposure and monitoring.

## Fourth Round Interview (Communication)

### Tell us a bit about yourself.

### What is your plan in a conflicting situation?

I would first understand both sides clearly and separate the technical issue from personal opinions. Then I would focus on risk, impact, business priority, and a practical path forward that everyone can agree on.

### Do you prefer a team approach or an individual approach?

I prefer a team approach for security work because security usually depends on developers, infrastructure, product, and business teams working together. Individual focus is useful for deep work, but the best outcomes usually come from collaboration.

### Suppose there are developers who are reluctant to fix a particular problem that you found, how would you convince them that security should not be shelved?

I would explain the risk in terms of real impact, likelihood, and how it affects users or the business. I would also provide a practical fix, help reduce the implementation burden, and prioritize the issue based on severity instead of just saying it is important.

### Do you think AI will take away your job? What is your outlook about this? Do you use AI in your everyday task?

I do not think AI will fully replace security engineers, but it will change how security work is done. I see it as a tool for speeding up research, code review, documentation, and repetitive analysis, while human judgment is still needed for risk decisions and context.
