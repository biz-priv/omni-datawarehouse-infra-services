Version: 1.0.1
BizDev Replica for Omni data warehouse service APIs. 

This contains Cloud Formation configuration files and templates for DynamoDB, AWS API Gateway and SSM. 

The code is used for building API's for OMNI Logistics. 
1. Shipment Info
2. Shipment Detail
3. Invoice Detail
4. Create Shipment
5. Bill of Lading


# New resource Create and Deployment Steps

============================= 1. Create resource on Dev Env.==========================

1. Redirect to location /config/dev/{Required-Resource-Directory}
    Example : /config/dev/ssm
2. Create directory for your resource file or Re-use existing directory if resource is belongs to it
    Example : /config/dev/ssm/api-domain
3. Create resource .yaml file in directory
    Example : /config/dev/ssm/api-domain/DomainName.yaml
4. For reference copy content from another .yaml file which exists in any other "/config/dev/{Resource-Directory}"
    Example : Copy file content from /config/dev/ssm/create-shipment/worldtrak-url.yaml and paste in your newly created file i.e. DomainName.yaml
5. Change value for keys i.e. Name,Value,Description and Value2(If Exist)

============================= 2. Create resource on Prod Env.==========================

1. Redirect to location /config/prod/{Required-Resource-Directory}
    Example : /config/prod/ssm
2. Copy directory which you've created for Dev Env. and paste in /confi/prod/{Required-Resource-Directory}
    Example : /config/prod/ssm/api-domain/DomainName.yaml
3. Change value for keys i.e. Value,Description and Value2(If Exist)

================================3. Local Deployment Steps ====================================
Install Sceptre
 - `pip install sceptre`
2. Open and Edit `/config/config.yaml`
3. Add line at end `profile: {your-local-aws-profile}` 
    Example : `profile: sls-dev`
4. Deploy specific resource using Sceptre : `sceptre create dev/ssm/api-domain/DomainName.yaml`