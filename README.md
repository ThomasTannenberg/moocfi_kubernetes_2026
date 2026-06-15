# Mooc.fi DevOps with Kubernetes 2026

This repository contains my local K3s setup and course exercises.

## K3s instead of k3d

Instead of k3d, I am using a local K3s setup running on KVM/libvirt.
The setup creates virtual machines for a small Kubernetes lab cluster.

## Cluster nodes

| Name | Role | MAC address | IP address |
|---|---|---|---|
| k3s-lb-1 | Load balancer | 52:54:00:00:00:10 | 192.168.122.10 |
| k3s-server-1 | Control plane | 52:54:00:00:00:11 | 192.168.122.11 |
| k3s-server-2 | Control plane | 52:54:00:00:00:12 | 192.168.122.12 |
| k3s-server-3 | Control plane | 52:54:00:00:00:13 | 192.168.122.13 |
| k3s-agent-1 | Worker | 52:54:00:00:00:21 | 192.168.122.21 |
| k3s-agent-2 | Worker | 52:54:00:00:00:22 | 192.168.122.22 |
| k3s-agent-3 | Worker | 52:54:00:00:00:23 | 192.168.122.23 |

The control plane nodes are tainted, so application workloads run on the worker nodes.

## Usage

Create the VMs and install the cluster with:

```bash
make install
```

# Kubernetes Submissions
## Exercises
### Chapter 2

| Exercise | Link |
|---|---|
| 1.1 | [Log output](https://github.com/thomastannenberg/moocfi_kubernetes_2026/tree/1.1/exercises/log-output) |
| 1.2 | [Todo app](https://github.com/ThomasTannenberg/moocfi_kubernetes_2026/tree/1.2/exercises/todo-app) |
| 1.3 | [Log output](https://github.com/ThomasTannenberg/moocfi_kubernetes_2026/tree/1.3/exercises/log-output) |
