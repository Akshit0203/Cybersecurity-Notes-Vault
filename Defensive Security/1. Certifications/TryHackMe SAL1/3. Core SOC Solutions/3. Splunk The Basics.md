# Task 3 Splunk Components

Splunk has three main components: Forwarder, Indexer, and Search Head.
![image-2.png](attachments/image-2.png)

## Splunk Forwarder

Splunk Forwarder is a lightweight agent installed on the endpoint intended to be monitored, and its main task is to collect the data and send it to the Splunk instance. It does not affect the endpoint's performance as it takes a few resources to process. Some of the key data sources are:

- Web server generating web traffic.
- Windows machine generating Windows Event Logs, PowerShell, and Sysmon data.
- Linux host generating host-centric logs.
- Database generating DB connection requests, responses, and errors.

![Splunk Forwarder](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/2369fa2efc856b793f1ecbf415681d4d.png)

The forwarder collects the data from the log sources and sends it to the Splunk Indexer.
## Splunk Indexer

Splunk Indexer plays the main role in processing the data it receives from forwarders. It parses and normalizes the data into field-value pairs, categorizes it, and stores the results as events, making the processed data easy to search and analyze.

![Splunk Indexer|700x426](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/e699eaa9af523513e9c6a6ab8aaaa6a2.png)

Now, the data, which is normalized and stored by the indexer, can be searched by the Search Head, as explained below.

## Search Head

Splunk Search Head is the place within the **Search & Reporting App** where users can search the indexed logs, as shown below. The searches are done using the **SPL** (Search Processing Language), a powerful query language for searching indexed data. When the user performs a search, the request is sent to the indexer, and the relevant events are returned as field-value pairs.

![Image showing Splunk Search Head](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/0f7738f88ca807d1edf2ac7d84f6951c.png)

The Search Head also allows you to transform results into presentable tables and visualizations such as pie, bar, and column charts, as shown below:

![Image showing the Visualization tab](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/ce38f9780efac6e22af23c2574367255.png)

# Task 4 Navigating Splunk

When you access Splunk, you will see the default **home screen** as shown below:

![An image showing the Splunk Interface](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/3880f2e7938460c3aab5da62d622ceac.png)

Let's look at each section of this home screen.

## Splunk Bar

The top panel is the **Splunk Bar** as shown below: 

![An image showing the Splunk Bar](https://assets.tryhackme.com/additional/splunk-overview/splunk-bar.png)

In the Splunk Bar, we have the following options available:

- **Messages:** View system-level notifications and messages.
- **Settings:** Configure Splunk instance settings.
- **Activity:** Review the progress of search jobs and processes.
- **Help:** View tutorials and documentation.
- **Find:** Search across the App.

The Splunk Bar, allows users to switch between installed Splunk apps instead of using the Apps panel.

**Apps Panel**  

Next is the **Apps Panel**. This panel shows the apps installed for the Splunk instance. The default app for every Splunk installation is **Search & Reporting**. 

![An image showing the App Panel](https://assets.tryhackme.com/additional/splunk-overview/splunk-apps-panel.png)

You can also switch between the Splunk Apps directly from the Splunk Bar, as shown below, without using the Apps Panel.

![Shows App Bar](https://assets.tryhackme.com/additional/splunk-overview/splunk-bar2.png)

**Explore Splunk** 

The next section is **Explore Splunk** . This panel contains quick links to add data to the Splunk instance, add new Splunk apps, and access the Splunk documentation. 

![An image showing the option to add data, access documentation, and add new Splunk apps](https://assets.tryhackme.com/additional/splunk-overview/explore-splunk.png)

**Splunk Dashboard**

The last section is the **Home Dashboard**. By default, no dashboards are displayed. You can choose from a range of dashboards readily available within your Splunk instance. You can select a dashboard from the dropdown menu or by visiting the **dashboards listing page**.

![An image showing the Splunk dashboard](https://assets.tryhackme.com/additional/splunk-overview/splunk-add-dashboard.gif)

You can also create dashboards and add them to the Home Dashboard. The dashboards you create can be viewed separately from the other dashboards by clicking on the **Yours** tab.

Please review the Splunk documentation on Navigating Splunk [here](https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/NavigatingSplunk).

# Task 5 Adding Data

Splunk can ingest any data. According to the Splunk documentation, when data is added to Splunk, the data is processed and transformed into a series of individual events. The data sources can be event logs, website logs, firewall logs, etc. The data sources are grouped into categories.

 Below is a chart listing from the Splunk documentation detailing each data source category.

![Data sources supported by Splunk](https://assets.tryhackme.com/additional/splunk-overview/splunk-data-sources.png)

In this task, we're going to focus on **VPN logs**. We're presented with the following screen when we click on the `Add Data` link on the Splunk home screen.

![Data sources Option](https://assets.tryhackme.com/additional/splunk-overview/splunk-add-data.png)

We will use the `Upload` Option to upload the data from our local machine.

## Practical

Download the log file `VPN_logs` from the `Download Task Files` button below and upload it to the Splunk instance we started in Task #2. If you are using the AttackBox, the log file is available in the `/root/Rooms/SplunkBasic/` directory.

To upload the data successfully, you must follow five steps, which are explained below:

1. **Select Source:** Choose the Log file and the data source.
2. **Select Source Type:** Select what type of logs are being ingested, e.g, JSON, syslog.
3. **Input Settings:** Select the index where these logs will be dumped and the HOSTNAME to be associated with the logs.
4. **Review:** Review all the configurations.
5. **Done:** Complete the upload. Your data will be uploaded successfully and ready to be analyzed.

![Data Ingestion Example](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/c36a6f1c70007602251f331aee914d5c.gif)

