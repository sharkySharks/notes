# Creating effective container images: the remix
## Abby Fuller - AWS

### Reduce layers (and size of layers)
- limit the data written 
- choose the right (smallest) base image that does what you need
    + EX: ubuntu:latest = 81.2MB vs alpine:latest = 4.15MB
    + be conscious of the disk space that you're using
    + don't always need the os, sometimes you just need the runtime
        * security, compliance, ease of deving, more features (package managers)

### F is for flags
- `--cache-from`
- `--compress`

### Do better
- use `RUN` statements as effectively as possible - combine when possible!
    + less is more bc each statement creates a layer
- multi-stage builds is a newer thing
    + or use multiple docker files
    + the idea is to separate the heavy building parts from the basic running of the image
- cache node_modules!
- `.dockerignore` files you don't need to build
- see how to use cache more effectively
- clean up
    + docker image prune: `docker image prune -a`
    + docker system prune: `docker system prune -a`

### Tools to help with safety - scanning docker images
- aqua microscanner
- aqua continuous image assurance
- Trusted Registry Clair from CoreOS - Docker Security Scanner
- spotify-gc - 3rd party garbage collection
    + k8 already has an internal garbage collection
    + check out how openshift/k8 garbage collects

### Side note: Check out scratch
Blank dockerfile to work with

