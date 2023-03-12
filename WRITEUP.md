# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

When considering the deployment of a CMS app, both a virtual machine (VM) and an App Service solution can be viable 
options. Which one is more appropriate solution can be based on the following factors:
1. In terms of costs, VMs can be more expensive as they require more infrastructure and maintenance costs. App Service 
is more cost-effective as it provides a managed platform with no additional infrastructure or maintenance costs.
2. Regarding scalability, VMs can be scaled vertically or horizontally, but require manual setup and configuration.App 
Service provides automatic horizontal scaling and easy configuration for vertical scaling.
3. For availability, VMs can experience downtime due to hardware failure or maintenance. On the other hand, App Service 
provides high availability with automatic fail-over and built-in redundancy.
4. Finally, for workflow, VMs require more manual setup and configuration and may have a longer deployment time while App 
Service provides a streamlined deployment process with easy integration with source control and continuous deployment tools.

Based on the above analysis, i would choose App Service for deployment for CMS app. It provides a cost-effective, scalable, 
and highly available managed platform with an easy deployment process.Additionally, it provides easy integration with source 
control and continuous deployment tools, making the workflow more streamlined.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If there were significant changes to the requirements or needs of the CMS app or other factors, it could change the appropriate 
solution for deployment. For example:
1. Cost: If the organization has a large existing investment in virtual machines and infrastructure, it may be more cost-effective 
to deploy the CMS app on a VM. Similarly, if the organization requires a high degree of customization or control over the environment, 
a VM may be a better choice.
2. Scalability: If the CMS app requires significant customization or configuration that is not supported by App Service, a VM may 
be a better choice.
3. Availability: If the organization has strict requirements for uptime and availability, a VM with a high-availability configuration 
may be a better choice. In addition, if the organization requires complete control over the backup and recovery process, a VM may be 
a better choice.
4. Workflow: If the organization has an existing deployment process that is tailored to VMs, it may be more efficient to continue using 
VMs. 