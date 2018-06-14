# Kubernetes in the Docker Platform
## Wayne Song & Guillaume Tardif - Docker

### start a k8 cluster
From the settings you can select to enable k8

This installs `kubectl` on the host and updates the ~/kube/config
In the VM, the kubelet is started and custom controllers are started. (kubeadm is also initiated)

K8 and Docker are running side by side - use both CLI

Choose between `k8` and `swarm` under the K8 desktop settings options. This will determine what kind of cluster is deployed when using `docker compose`

### Compose for K8
- new type: stack
    + `kubectl get stacks`
    + `docker stack ls`
    + automatically create pv for compose volume
    + *something else I did not get to write down =(*

EX: `trial.docker.com` || `docker.com/get-docker`
