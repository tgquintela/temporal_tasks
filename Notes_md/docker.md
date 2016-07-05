
#Docker
2016-06-01

Docker is an open-source project that automates the deployment of applications inside software containers. Docker containers wrap up a piece of software in a complete filesystem that contains everything it needs to run: code, runtime, system tools, system libraries (anything you can install on a server). This guarantees that it will always run the same, regardless of the environment it is running in.
Docker provides an additional layer of abstraction and automation of operating-system-level virtualization on Linux. Docker uses the resource isolation features of the Linux kernel such as cgroups and kernel namespaces, and a union-capable file system such as aufs and others to allow independent "containers" to run within a single Linux instance, avoiding the overhead of starting and maintaining virtual machines.

### Functionality
As actions are done to a Docker base image, union file system layers are created and documented, such that each layer fully describes how to recreate an action. This strategy enables Docker's lightweight images, as only layer updates need to be propagated (compared to full VMs, for example). Docker implements a high-level API to provide lightweight containers that run processes in isolation.

By using containers, resources can be isolated, services restricted, and processes provisioned to have an almost completely private view of the operating system with their own process ID space, file system structure, and network interfaces. Multiple containers share the same kernel, but each container can be constrained to only use a defined amount of resources such as CPU, memory and I/O.

Using Docker to create and manage containers may simplify the creation of highly distributed systems by allowing multiple applications, worker tasks and other processes to run autonomously on a single physical machine or across multiple virtual machines. This allows the deployment of nodes to be performed as the resources become available or when more nodes are needed, allowing a platform as a service (PaaS)-style of deployment and scaling for systems like Apache Cassandra, MongoDB or Riak. Docker also simplifies the creation and operation of task or workload queues and other distributed systems

***Tags***: Computer engineering, Software management tools

### See also
[DevOps](/devops)
## Material
* https://www.docker.com/
* https://docs.docker.com/

## Books
* Turnbull, James (2014). [The Docker Book: Containerization is the new virtualization](https://www.goodreads.com/book/show/22719521-the-docker-book). Kindle Edition
* Matthias, Karl; Kane, Sean P. (2015). [Docker: Up & Running](https://www.goodreads.com/book/show/25000037-docker). O'Reilly Media
* Mouat, Adrian (2015). [Using Docker](https://www.goodreads.com/book/show/25484101-using-docker). O'Reilly Media
* Goasguen, S. (2015). [Docker Cookbook](https://www.goodreads.com/book/show/24216689-docker-cookbook). O'Reilly Media
* Nickoloff, Jeff (2015). [Docker in Action](https://www.goodreads.com/book/show/23612990-docker-in-action). Manning Publications Co.


