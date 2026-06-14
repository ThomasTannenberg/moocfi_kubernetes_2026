.PHONY: vm-create vm-delete cluster-create cluster-delete install validate cleanup

KUBECONFIG_FILE := cluster/ansible/k3s.yaml

vm-create:
	cd cluster/libvirt && ./00-bootstrap.sh
	cd cluster/libvirt && ./01-deploy-cluster-cloudimg.sh

vm-delete:
	cd cluster/libvirt && ./99-cleanup.sh

cluster-create:
	cd cluster/ansible && ansible-playbook site.yml

cluster-delete:
	cd cluster/ansible && ansible-playbook uninstall.yml

install: vm-create cluster-create

validate:
	@echo "------------------------- Nodes ----------------------------"
	KUBECONFIG=$(KUBECONFIG_FILE) kubectl get nodes -o wide
	@echo "------------------------- Services -------------------------"
	KUBECONFIG=$(KUBECONFIG_FILE) kubectl get svc -A

cleanup: cluster-delete vm-delete
