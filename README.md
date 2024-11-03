# QRTU - A Quick Roblox T-Shirt Uploader

# Setup
1. Download the latest release from the releases.

2. Unzip the zip file you just downloaded.

3. Setup your api key and enter it into your credentials.json, along with your userid.

4. Run the exe and your all good to go!


# Creating An API Key
If you dont know how to setup your api key then, 
To create an API key:

Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).

In the left navigation menu, select Open Cloud → API Keys.

![image](https://github.com/user-attachments/assets/8bb7e002-e67e-4d38-9145-75ea5ac09053)

Click the Create API Key button.

![image](https://github.com/user-attachments/assets/6e04cc71-df8e-42f5-9be4-66ec708c2258)


Enter a unique name for your API key.

In the Access Permissions section, select "**asset:read** and **asset:write**" from the Select API System menu and click the Add API System button. 
![image](https://github.com/user-attachments/assets/e4105eec-3608-4d0a-bec8-67be90122126)

![image](https://github.com/user-attachments/assets/a61f5c9a-2897-40ff-92b2-1b57a55d255a)

In the Security section, explicitly set IP access to the key using CIDR notation, otherwise you can't use the API key. You can find the IP address of your local machine and add it to the Accepted IP Addresses section along with additional IP addresses for those that need access. If you don't have a fixed IP, or you are using the API key only in a local environment, you can just add **0.0.0.0/0** to the Accepted IP Addresses section to allow any IPs to use your API key.

![image](https://github.com/user-attachments/assets/892dd6b7-c034-42e3-824f-346cbe49f0e3)

(Optional): To add additional protection for your resources, set an explicit expiration date so your key automatically stops working after that date.

Click the Save and Generate key button.

![image](https://github.com/user-attachments/assets/5b8d4ea5-c4d0-4d81-a45e-2a24c430f0b7)

Copy and save the API key string to a secure location.  

Check your created API key on the Credentials page of [Creator Dashboard](https://create.roblox.com/dashboard/creations).
