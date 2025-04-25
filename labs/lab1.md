# Kubernetes Hands-on Labs

These hands-on labs will help you explore and understand key Kubernetes concepts including ReplicaSets, Deployments, and NodePort Services. Each lab contains exercises without solutions, encouraging you to explore Kubernetes functionality.

## Prerequisites

Before starting these labs, ensure you have:

1. A running Kubernetes cluster (Minikube, Docker Desktop, or any other Kubernetes cluster)
2. `kubectl` command-line tool installed and configured to access your cluster
3. Basic understanding of Kubernetes concepts
4. A text editor for creating YAML files

Verify your setup with:

```bash
kubectl version
kubectl get nodes
```

## Lab 1: ReplicaSet - Self-healing and Scaling

**Objective:** Learn how ReplicaSets maintain a specific number of pod replicas and provide self-healing capabilities.

### Exercise 1.1: Create a ReplicaSet

1. Create a file named `nginx-replicaset.yaml` with a ReplicaSet configuration for nginx:
   - Use the image `nginx:1.19`
   - Set 3 replicas
   - Use appropriate labels to select the pods

2. Apply the configuration:
   ```bash
   kubectl apply -f nginx-replicaset.yaml
   ```

3. Verify the ReplicaSet and pods were created:
   ```bash
   kubectl get replicasets
   kubectl get pods
   ```

### Exercise 1.2: Test Self-healing

1. Pick one of the pods created by the ReplicaSet and delete it:
   ```bash
   kubectl delete pod <pod-name>
   ```

2. Immediately check the pods:
   ```bash
   kubectl get pods
   ```

3. What happened? How quickly did the ReplicaSet respond?

4. Run the following command to watch pod creation in real-time:
   ```bash
   kubectl get pods -w
   ```

5. Delete another pod while watching and observe what happens.

### Exercise 1.3: Scaling ReplicaSets

1. Scale the ReplicaSet to 5 replicas using the `kubectl scale` command:
   ```bash
   kubectl scale replicaset <replicaset-name> --replicas=5
   ```

2. Verify the new pods are being created:
   ```bash
   kubectl get pods
   ```

3. Now scale down to 2 replicas. Which pods get terminated? Is there a pattern?

4. Edit the YAML file to set replicas to 4, then apply it:
   ```bash
   kubectl apply -f nginx-replicaset.yaml
   ```

5. What's the difference between scaling using the `kubectl scale` command versus editing the YAML file?

### Exercise 1.4: ReplicaSet Challenges

1. Attempt to change the pod template in your ReplicaSet (e.g., change the nginx version to 1.20), apply the change, and observe what happens to existing pods. Why?

2. Create a pod manually that matches the labels of your ReplicaSet. What happens when you apply it? What happens if you then check the total number of pods?

3. Delete the ReplicaSet but keep the pods by using the `--cascade=orphan` flag:
   ```bash
   kubectl delete replicaset <replicaset-name> --cascade=orphan
   ```
   What happens to the pods? Re-create the ReplicaSet with the same selector. What happens?

## Lab 2: Deployments - Rolling Updates and Rollbacks

**Objective:** Understand how Deployments manage ReplicaSets to enable rolling updates and rollbacks.

### Exercise 2.1: Create a Deployment

1. Create a file named `nginx-deployment.yaml` with a Deployment configuration:
   - Use nginx:1.19 image
   - Create 3 replicas
   - Add appropriate labels
   - Define a RollingUpdate strategy with maxSurge=1 and maxUnavailable=1

2. Apply the Deployment:
   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```

3. Check the Deployment, ReplicaSet, and Pods:
   ```bash
   kubectl get deployments
   kubectl get replicasets
   kubectl get pods
   ```

### Exercise 2.2: Perform a Rolling Update

1. Update the image in your `nginx-deployment.yaml` file to nginx:1.20

2. Apply the updated Deployment:
   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```

3. Watch the rolling update in action:
   ```bash
   kubectl get pods -w
   ```

4. In another terminal, check the ReplicaSets:
   ```bash
   kubectl get replicasets
   ```
   
5. What's happening with the ReplicaSets during the update?

### Exercise 2.3: Rollback a Deployment

1. View the rollout history of your Deployment:
   ```bash
   kubectl rollout history deployment <deployment-name>
   ```

2. Update the image again to an invalid one (e.g., nginx:nonexistent-version)

3. Apply the change and watch what happens:
   ```bash
   kubectl apply -f nginx-deployment.yaml
   kubectl get pods
   ```

4. Once you see pods failing to start, roll back to the previous version:
   ```bash
   kubectl rollout undo deployment <deployment-name>
   ```

5. Check the status of the rollout:
   ```bash
   kubectl rollout status deployment <deployment-name>
   ```

### Exercise 2.4: Deployment Scaling and Challenges

1. Scale the Deployment to 5 replicas using the kubectl command.

2. Pause the Deployment's rollout:
   ```bash
   kubectl rollout pause deployment <deployment-name>
   ```

3. Change the image version again, apply it, and observe what happens.

4. Resume the rollout:
   ```bash
   kubectl rollout resume deployment <deployment-name>
   ```

5. Create two identical Deployments but with different update strategies:
   - One with RollingUpdate and maxUnavailable=0
   - One with Recreate strategy
   
   Update both and observe the differences in behavior.

## Lab 3: NodePort Services - Exposing Applications

**Objective:** Learn how to expose applications outside the cluster using NodePort Services.

### Exercise 3.1: Create a Deployment to Expose

1. Create a file named `web-deployment.yaml` with a Deployment for a web application:
   - Use the image `nginx:1.19`
   - Set 3 replicas
   - Add appropriate labels (app: web)

2. Apply the Deployment:
   ```bash
   kubectl apply -f web-deployment.yaml
   ```

3. Verify the Deployment and pods:
   ```bash
   kubectl get deployments
   kubectl get pods
   ```

### Exercise 3.2: Expose the Deployment via NodePort

1. Create a file named `web-nodeport.yaml` with a NodePort Service configuration:
   - Target the pods from your web Deployment using selector
   - Expose port 80
   - Set the NodePort type
   - Optionally, specify a nodePort value between 30000-32767

2. Apply the Service:
   ```bash
   kubectl apply -f web-nodeport.yaml
   ```

3. Get information about the Service:
   ```bash
   kubectl get svc
   kubectl describe svc <service-name>
   ```

### Exercise 3.3: Access the Application

1. Determine the node's IP address:
   - For Minikube: `minikube ip`
   - For other setups: check your node IPs with `kubectl get nodes -o wide`

2. Access the application using the Node IP and NodePort in your browser:
   ```
   http://<node-ip>:<node-port>
   ```

3. Try scaling your Deployment up and down. Does the Service still work correctly? How does it determine which pods to send traffic to?

### Exercise 3.4: NodePort Service Challenges

1. Create a second Deployment with different content but the same labels as your web Deployment.

2. What happens to the Service routing? How are requests distributed?

3. Update the Service to use a different selector and observe the changes.

4. Create a NodePort service without specifying a nodePort value. What port does it select?

5. Try to create a NodePort service with a port outside the allowed range (e.g., 29000). What happens?

## Lab 4: Multi-tier Application Deployment

**Objective:** Deploy a multi-tier application with frontend and backend components, using Deployments and Services.

### Exercise 4.1: Create a Backend Deployment

1. Create a file named `backend-deployment.yaml` for a backend service:
   - Use an API or database image of your choice (e.g., `redis:6`)
   - Set 2 replicas
   - Add appropriate labels (app: backend, tier: db)

2. Apply the Deployment:
   ```bash
   kubectl apply -f backend-deployment.yaml
   ```

### Exercise 4.2: Create a Backend Service

1. Create a file named `backend-service.yaml` for a service to expose your backend:
   - Use ClusterIP type (internal access only)
   - Map to the appropriate port for your backend
   - Use selectors matching your backend pods

2. Apply the Service:
   ```bash
   kubectl apply -f backend-service.yaml
   ```

### Exercise 4.3: Create a Frontend Deployment

1. Create a file named `frontend-deployment.yaml` for a frontend application:
   - Use an appropriate web image (e.g., `nginx:1.19`)
   - Set 3 replicas
   - Add appropriate labels (app: frontend, tier: web)
   - Configure it to communicate with the backend service (this may require custom configuration or environment variables)

2. Apply the Deployment:
   ```bash
   kubectl apply -f frontend-deployment.yaml
   ```

### Exercise 4.4: Expose the Frontend via NodePort

1. Create a file named `frontend-nodeport.yaml` for a NodePort service:
   - Target your frontend pods
   - Expose the web port
   - Set type: NodePort

2. Apply the Service:
   ```bash
   kubectl apply -f frontend-nodeport.yaml
   ```

3. Access the frontend application through the NodePort service.

### Exercise 4.5: Chaos Testing

1. Delete a backend pod and observe what happens. Does the Service redirect traffic properly to the remaining pod?

2. Delete a frontend pod during an active session. What happens to the user experience?

3. Scale the backend to 0 replicas. How does the frontend respond? Is there any error handling?

4. Scale the backend back to 2 replicas. Does the frontend recover?

5. Simulate a rolling update of the frontend while monitoring the application availability.

## Lab Cleanup

After completing each lab, clean up the resources to avoid conflicts with subsequent labs:

```bash
kubectl delete deployment <deployment-name>
kubectl delete service <service-name>
kubectl delete replicaset <replicaset-name>
```

Or, if you've named all your resources consistently, you can use labels:

```bash
kubectl delete all -l app=web
kubectl delete all -l app=frontend
kubectl delete all -l app=backend
```


# questions:

1. What is the relationship between a Deployment and a ReplicaSet?
2. How does Kubernetes ensure high availability through ReplicaSets?
3. What are the advantages of using Deployments over directly using ReplicaSets?
4. How do NodePort Services enable external access to applications?
5. What limitations exist with NodePort Services in production environments?
6. How would you implement a zero-downtime deployment strategy in Kubernetes?
7. What is the difference between the various Service types in Kubernetes?
8. How can you troubleshoot if a Service is not routing traffic to your Pods?