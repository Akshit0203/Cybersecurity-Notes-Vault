# Task 2 Elastic Stack Overview

many SOC teams use ELK almost as a SIEM solution. 

Elastic Stack is a collection of different open-source components that work together to collect data from any source, store and search it, and visualize it in real time. 

![Shows Elastic Stack components|700x243](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/f858c0d22d015b663438dae207981532.png)

## 1. Elasticsearch
The first component, Elasticsearch, is a full-text search and analytics engine for JSON-formatted documents. It stores, analyzes, and correlates data and supports a RESTful API for interacting with it.
## 2. Logstash
Logstash is a data processing engine that takes data from different sources, filters it, or normalizes it, and then sends it to the destination, which could be Kibana or a listening port. A Logstash configuration file is divided into three parts, as shown below.

1. The **Input** part is where the user defines the source from which the data is being ingested.
2. The **Filter** part is where the user specifies the filter options to normalize the log ingested above. 
3. The **Output** part is where the user wants the filtered data to be sent. It can be a listening port, Kibana Interface, Elasticsearch database, or file. 
4. 
Logstash supports many Input, Output, and Filter plugins.
![Shows the Logstash configuration file pattern|188x293](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/31e9ef413089c7b15ad64e09d3655c04.png)

## 3. Beats
Beats are host-based agents known as data-shippers that ship/transfer data from the endpoints to Elasticsearch. Each beat is a single-purpose agent that sends specific data to Elasticsearch. All available beats are shown below. 

![Shows beats components](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/0f2969b20c466e7a371a49bc809a6d5b.png)
## 4. Kibana
Kibana is a web-based data visualization tool that works with Elasticsearch to analyze, investigate, and visualize data streams in real time. It allows users to create multiple visualizations and dashboards for better visibility.

## How they work together:

Now that we have learned about all the components of the Elastic Stack, let's see how these components work together step-by-step:

- **Beats** collect data from multiple agents. For example, Winlogbeat collects Windows event logs, and Packetbeat collects network traffic flows.
- **Logstash** collects data from beats, ports, or files, parses/normalizes it into field value pairs, and stores them into Elasticsearch.
- **Elasticsearch** acts as a database used to search and analyze data.
- **Kibana** is responsible for displaying and visualizing the data stored in Elasticsearch. The data stored in Elasticsearch can easily be shaped into different visualizations, time charts, infographics, etc., using Kibana.

![ELK components](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/ec4f681a412aa825b284523dcd5b8650.png)

# Task 4 Discover Tab

ELK's front-end interface
Kibana is the component of ELK that supports these interactions with the front end.

## Discover Tab

The Discover tab is where the SOC analysts spend most of their time. This tab shows the ingested logs, the search bar, normalized fields, and more. Analysts can search for the logs, investigate anomalies, and apply filters based on search terms and time periods.

![Shows the Discover tab with key functionalities numbered](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/9635453d465f7625f5dfda21966aa6a6.png)

Let's briefly see what each element (as highlighted in the above screenshot) of the Discover tab does: 

1. **Logs  
    **Each row shows a single log containing information about the event, along with the fields and values found in that log.
2. **Fields Pane  
    **The left panel of the interface shows the list of fields parsed from the logs. We can click on any field to add it to the filter or remove it from the search.
3. **Index Pattern  
    **Each type of log is stored in a different index pattern. We can select the index pattern from which we need the logs. For example, for VPN logs, we would need to select the index pattern in which VPN logs are stored.
4. **Search Bar  
    **It is a place where the user adds search queries and applies filters to narrow down the results. In the next task, we will learn how to perform searches through queries.
5. **Time Filter  
    **We can narrow down results based on any specific time duration. 
6. **Time Interval  
    **This chart shows the event counts over time.
7. **TOP Bar  
    **This bar contains various options to save the search, open the saved searches, share or save the search, etc.
8. **Discover Tab  
    **This is the main workspace in Kibana for exploring, searching, and analyzing raw data.
9. **Add Filter  
    **We can apply filters to specific fields to narrow down results, rather than manually typing entire queries.


**Index Pattern**

By default, Kibana requires an index pattern to access the data stored/ingested in Elasticsearch. The i**ndex pattern** tells Kibana which elasticsearch data we want to explore. Each Index pattern corresponds to certain defined properties of the fields. A single index pattern can point to multiple indices.

Each log source has a different log structure; therefore, when logs are ingested into Elasticsearch, they are first normalized into corresponding fields and values by creating a dedicated index pattern for the data source.

we will explore the index pattern `vpn_connections` which contains the VPN logs.

![Shows the Index Pattern tab](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/7a417aad777ee8afa398d98532f68478.png)


<span style="color:rgb(255, 0, 0)"><b>Fields Pane</b></span>

The left panel in the Discover tab shows the list of the normalized fields it finds in the available logs. <span style="color:rgb(255, 0, 0)">Click on any field, and it will show the top 5 values and the percentage of occurrence</span>.

We can use these values to apply filters to them. Clicking on the `+` button will add a filter to show the logs containing this value, and the `-` button will add a filter to show the results that do not have this value.

![Shows left panel fields](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/aa7c29f3d971ce34a6f69c0dd9b1be86.png)

We can also apply filters to any of the fields shown in the panel on the left. All we have to do is click the `Add filter` option under the search bar, which will allow us to apply a filter to the fields shown below.

![Shows steps to add a filter to the search](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/f8f4399d7fbfc14c0a6659da697af1db.gif)

**Time Filter**

The time filter allows us to apply a log filter based on time. It has many options.

![Shows the time filter tab](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/3691fb78e08f98b9b825fa6eaeefcf91.png)

**Timeline**

The timeline pane provides an overview of the number of events that occurred for the time/date, as shown below. We can only select the bar to show the logs in that period. The count at the top left displays the number of events found in the specified time.

![Shows timeline](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/5a2096f7dac927eaeb020c2c81e15565.png)

This bar is also helpful in identifying the spike in the logs. In the above screenshot, we can see an unusual log spike on 11th January 2022.

**Create Table**

By default, the logs are shown in raw form. We can click on any log and select important fields to create a table showing only those fields. This method reduces the noise and makes it more presentable and meaningful.

![Shows steps to create a table by selecting fields and removing noise](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/ed538dabafffd64020b51f88fabce8f9.gif)

You can also save the table format once it is created. It will then show the same fields every time a user logs into the dashboard.

# Task 5 KQL Overview

There is a special language that we can use inside this search bar to perform our searches. KQL **(Kibana Query Language)** is a search query language used to search the ingested logs/documents in Elasticsearch. 

![KQL tab](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/3327ee49838ed3b50aa9ffca5295b271.png)

With KQL, we can search for the logs in two different ways.

- Free text search
- Field-based search

## Free text Search

Free text search allows users to search for logs based on text only. That means a simple search of the term `security` will return all the documents that contain this term, irrespective of the field. Let's search for the text `United States` in the search bar. It will return all the logs that contain this term, regardless of the place or the field. This search returned 2304 hits, as shown below.

![Shows result for the search 'United States'](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/beb9f3912904e689952027ced1475755.png)

<span style="color:rgb(255, 0, 0)">What if we only search for the term `United`?</span> Do you think it will return any results?

![Shows result for the term 'United'](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/a4cbeb5fe4b5507762c0f3a7bfaf43ca.png)

<span style="color:rgb(255, 0, 0)">It didn't return any results because KQL looks for the whole term/word in the documents.</span> 

<span style="color:rgb(255, 0, 0)">KQL allows the wildcard `*` </span>to match parts of the word. Let's find out how to use this wild card in the search query.

<span style="color:rgb(255, 0, 0)"><b>Search Query:</b> `United*`</span>

![Shows result for the term United*](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/e4ce12cedbed2b6c7d5519d49a000881.png)

We have used the wildcard with the term `United` to return all the results containing the term United and any other term after it. <span style="color:rgb(255, 0, 0)">If we had logs with the term `United Nations`. It would also have returned those as a result of this wildcard.</span>

## Logical Operators (AND | OR | NOT)

KQL also allows users to utilize logical operators in the search query. Let's look at the examples below.

## **1. AND Operator**

Here, we will use the **AND** Operator to create a search that returns the logs containing the terms `"United States"` and `"Virginia"`.

**Search Query:** `"United States" AND "Virginia"`

![Shows results for United States AND Virginia](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/18302e0059d525f30f5627af20f309c9.png)

## 2. OR Operator

We will use the **OR** operator to show logs that contain either the `United States` or `England`.

**Search Query:** `"United States" OR "England"`

![Shows results for the term United States OR England](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/3397dcf2455056e7cab5a14a4fe28c45.png)

## 3. NOT Operator

Similarly, we can use the **NOT** Operator to remove a particular term from the search results. This search query will show the logs from **the United States**, including all states, but ignoring Florida.

**Search Query:** `"United States" **AND NOT** ("Florida")`
 ![Shows result for United States AND NOT Florida](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/12ba759b11ceebb78375a61097e826b3.png)

## Field-based search

In the Field-based search, we will provide the field name and the value we are looking for in the logs. This search has a special syntax as `Field: Value`. It uses a colon as a separator between the field and the value. Let's look at a few examples.

**Search Query:** `Source_ip : 238.163.231.224 AND UserName : Suleman` 

**Explanation:** We are telling Kibana to display all the logs in which the field `Source_ip` contains the value `238.163.231.224` and `UserName` is `Suleman`, as shown below.

![Shows result for Source_ip : 238.163.231.224    AND     UserName : Suleman](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/ffbf735277d98273d6229f4d9ee586bf.gif)

When we click on the search bar, we are presented with all the available fields that we can use in our search query.

Create a search query to filter the logs where **Source_Country** is the **United States** and show logs from User **James** or **Albert**.
```
Source_Country : "United States" AND (User : "James" OR User : "Albert")
```

# Task 6 Creating Visualizations

## Create Visualization

There are a few ways to navigate to the visualization tab. One way is to click on any field in the discover tab and click on the visualization as shown below.

![Shows the Visualization tab overview](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/334ed7c0a1e727de35844174434fd4fc.gif)

We can create multiple visualizations by selecting options like tables, pie charts, etc.

## Correlation Option

Often, we require creating correlations between multiple fields. Dragging the required field in the middle will create a correlation tab in the visualization tab. Here, we selected the `Source_Country` as the second field to show a correlation among the client `Source_IP`.

![Pie-chart for TOP 5 Source_Country](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/e5f27f38815a495499935f5a373728a6.png)

We can also create a table to show the values of the selected fields as columns, as shown below.

![Table with IPs VS country Count](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/819d71befcd64675b9450ee16d0b3d59.png)

The most important step in creating these visualizations is saving them. To do so, click on the save Option on the right side and fill in the descriptive values below. 

![Button to save Visualization](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/432f67edc84fff2cb9e6fc7bb6243b1b.png)

Steps to take after creating Visualizations:

- Create a visualization and click the Save button at the top right corner.
- Add the title and description to the visualization.
- Click Save and add to the library when it's done.

## Failed Connection Attempts Visualization

We'll use the knowledge gained above to create a table to show the user and the IP address involved in failed attempts.

![Showing how to create a visualization for failed Attempts](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/93e9aebb89efb58df9ab5a52eeb0177c.gif)


# Task 7 Creating Dashboards

**Creating a Custom Dashboard**

By now, we have saved a few `Searches` from the `Discover tab`, created some `Visualizations`, and saved them. It's time to explore the dashboard tab and create a custom dashboard. The steps to create a dashboard are:

- Go to the `Dashboard tab` and click on the `Create dashboard.`

![Image with a button to create a Dashboard](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/2b8beb35c48052335e21479f096e2cf2.png)

- Click on `Add from Library.`
- Click on the visualizations and saved searches. It will be added to the dashboard.
- Once the items are added, adjust them accordingly, as shown below.
- Don't forget to save the dashboard after completing it.

![steps to show how to add objects to the dashboard](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/05016a6cc1c12d40b90ce9d290525378.gif)


