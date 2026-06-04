# Situational Question Answers

## TLSv1.0 Discovery

If I find TLSv1.0 enabled, I would first confirm it using tools like `nmap --script ssl-enum-ciphers`, `testssl.sh`, or SSL Labs. For a proof of concept, I would show that the server accepts TLSv1.0 connections and explain the risks, such as weak protocol support, compliance issues, and exposure to downgrade-related attacks. The remediation would be to disable TLSv1.0 and TLSv1.1, then enforce TLSv1.2 or TLSv1.3 with strong cipher suites.

## Kubernetes Identification

I would look for exposed Kubernetes-related ports, services, headers, certificates, and API responses. Useful checks include scanning for ports like `6443`, `10250`, `10255`, and checking whether the Kubernetes API server or kubelet endpoints are exposed. I would also review DNS names, response banners, cloud metadata, and any publicly exposed dashboards or container-related services.

## Missing Security Headers

If a website has no security headers, I would report the issue with impact and recommend headers based on the application’s behavior. Common recommendations include `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options` or `frame-ancestors`, `X-Content-Type-Options`, `Referrer-Policy`, and secure cookie flags like `HttpOnly`, `Secure`, and `SameSite`. I would also explain that headers should be tested carefully so they do not break legitimate application functionality.

## Operating System Identification

To identify the operating system, I would start with passive checks and then move to active fingerprinting if allowed. Tools and methods could include `nmap -O`, `nmap -A`, TTL analysis, service banner grabbing, HTTP headers, SSH banners, and responses from open ports. I would combine multiple signals instead of trusting a single tool result.

## CVE Validation and Security Posture Assessment

For each CVE, I would verify the affected product, version, configuration, and whether the vulnerable code path is actually reachable. I would use vendor advisories, NVD, CVE records, Exploit-DB, GitHub advisories, CISA KEV, and scanner plugin details to validate the finding. Then I would prioritize the CVEs based on exploitability, exposure, business impact, available patches, and whether there is evidence of active exploitation.
