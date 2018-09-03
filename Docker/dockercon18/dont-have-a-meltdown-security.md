# Don't have a meltdown!
## Liz Rice - Aqua Security & Justin Cormack - Docker

### code quality
- static analysis
    + add static analysis tools either to your dockerfile or somewhere else in pr process
- code reviews

### security testing
- add automated security testing for encryption, TLS, SSL, etc
- docker trusted registry (EE) scans for security vulnerabilities
- microscanner from aqua security
- Clair

### minimal attack surface
- minimize the amount of code that you have (less code less surface area to attack)
- minimize what is running on the host, run everything in the container
- host configuration
    + Center for Internet Security
    + Docker Bench for Security v1.3.4

### least privilege
- only give access when needed
- if it doesn't need to write, don't give it write access
- minimize bind mounts
- set USER in dockerfile (don't leave as `root`)
- avoid `--privileged`

### defense in depth
- monitor the host at runtime to detect unexpected behavior
- can use aqua to monitor expected behavior and alert and stop actions if executables or other files are found that are not expected for the app
- runtime protection
    + seccomp/apparmor
    + commercial tools
    + new runtimes

**Resources and Examples: github.com/lizrice/no-meltdown** 
