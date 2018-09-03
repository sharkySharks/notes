# Container Orchestration from Theory to Practice
## Stephen Day & Laura Frank Tacho

Orchestration: a control system for your cluster

* Building data structures that can easily show build consistency

### Manager-worker communication
* push/pull model pattern
    - push model uses a discovery system, sometimes harder to troubleshoot
    - pull model needs to always maintain connection to the manager
* Swarmkit uses pull pattern
    - manager dictates heartbeat rate to worker
    - implements Raft algorithm directly, instead of via etcd
        - secretlivesofdata.com 
    - `swarm-rafttool` <-- check spelling
* Github:
    - docker/swarmkit
    - CoreOS/etcd

**side note: check out `strings` on command line**
