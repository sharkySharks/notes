# Proactive Ops for Container Orchestration
## John Harris - Docker

### Proactive | Reactive | Manual
Proactive 
- Application-centric data collection
- end-to-end observability
- key metrics and thresholds well understood
- semi-automated analysis and remediation

You can improve anything incrementally

### Blackbox monitoring
Cindy Sridharan - has a new book out, into treating the app like a blackbox to get info

- healthchecks (docker healthchecks - add a linter to not allow anything to go up without a healthcheck in the file)
- USE model (utilization, saturation, errors)
    + Prometheus and Graphana for showing metrics on basic monitoring metrics
- RED model (rate, error, duration)

### Whitebox monitoring
- Instrumentation 
- predictive vs active
- context/metadata

### How to improve
- Can get information tracked through Prometheus about the health and activity of the pods and containers.
- structured logging (json logging)
    + add structured logging for jenkins
    + ELK : elasticsearch, kibana, logstash
    + add as much context/metadata to events, traces, and metrics

### Chaos Engineering
principlesofchaos.org

**Improve Incrementally for Big Wins**
