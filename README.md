# ProjectThreatDetectionSystem

This repository will contain information about the implementation of the threat detection algorithm. The Threat detecton system will be using various machigitne learning algorithms in its implementation. 
For predicting threat patterns.  

### About the data
To cite the dataset please reference it as “Stratosphere Laboratory. A labeled dataset with malicious and benign IoT network traffic. January 22th. Agustin Parmisano, Sebastian Garcia, Maria Jose Erquiaga. https://www.stratosphereips.org/datasets-iot23

This dataset includes labels that explain the linkages between flows connected with harmful or possibly malicious activity to provide network malware researchers and analysts with more thorough information. These labels were painstakingly created at the Stratosphere labs using malware capture analysis.

We present a concise explanation of the labels used for the identification of malicious flows, based on manual network analysis, below:

Attack: This label signifies the occurrence of an attack originating from an infected device directed towards another host. Any flow that endeavors to exploit a vulnerable service, discerned through payload and behavioral analysis, falls under this classification. Examples include brute force attempts on telnet logins or header-based command injections in GET requests.

Benign: The "Benign" label denotes connections where no suspicious or malicious activities have been detected.

C&C (Command and Control): This label indicates that the infected device has established a connection with a Command and Control server. This observation is rooted in the periodic nature of connections or activities such as binary downloads or the exchange of IRC-like or decoded commands.

DDoS (Distributed Denial of Service): "DDoS" is assigned when the infected device is actively involved in a Distributed Denial of Service attack, identifiable by the volume of flows directed towards a single IP address.

FileDownload: This label signifies that a file is being downloaded to the infected device. It is determined by examining connections with response bytes exceeding a specified threshold (typically 3KB or 5KB), often in conjunction with known suspicious destination ports or IPs associated with Command and Control servers.

HeartBeat: "HeartBeat" designates connections where packets serve the purpose of tracking the infected host by the Command and Control server. Such connections are identified through response bytes below a certain threshold (typically 1B) and exhibit periodic similarities. This is often associated with known suspicious destination ports or IPs linked to Command and Control servers.

Mirai: This label is applied when connections exhibit characteristics resembling those of the Mirai botnet, based on patterns consistent with common Mirai attack profiles.

Okiru: Similar to "Mirai," the "Okiru" label is assigned to connections displaying characteristics of the Okiru botnet. The parameters for this label are the same as for Mirai, but Okiru is a less prevalent botnet family.

PartOfAHorizontalPortScan: This label is employed when connections are involved in a horizontal port scan aimed at gathering information for potential subsequent attacks. The labeling decision hinges on patterns such as shared ports, similar transmitted byte counts, and multiple distinct destination IPs among the connections.

Torii: The "Torii" label is used when connections exhibit traits indicative of the Torii botnet, with labeling criteria similar to those used for Mirai, albeit in the context of a less common botnet family.


|Field Name	| Description| Type|
|-----------|-----------|------|
|ts|The timestamp of the connection event.	|time|
|uid	|A unique identifier for the connection.	|string|
|id.orig_h	|The source IP address.	|addr|
|id.orig_p	|The source port.	|port|
|id.resp_h	|The destination IP address.	|addr|
|id.resp_p	|The destination port.	|port|
|proto	|The network protocol used (e.g., 'tcp').	|enum|
|service|The service associated with the connection.	|string|
|duration	|The duration of the connection.	|interval|
|orig_bytes	|The number of bytes sent from the source to the destination.	|count|
|resp_bytes	|The number of bytes sent from the destination to the source.	|count|
|conn_state	|The state of the connection.	|string|
|local_orig	|Indicates whether the connection is considered local or not.	|bool|
|local_resp	|Indicates whether the connection is considered local or not.	|bool|
|missed_bytes|The number of missed bytes in the connection.	|count|
|history	|A history of connection states.	|string|
|orig_pkts	|The number of packets sent from the source to the destination.	|count|
|orig_ip_bytes	|The number of IP bytes sent from the source to the destination.	|count|
|resp_pkts	|The number of packets sent from the destination to the source.	|count|
|resp_ip_bytes	|The number of IP bytes sent from the destination to the source.	|count|
|tunnel_parents	|Indicates if this connection is part of a tunnel.	|set[string]|
|label	|A label associated with the connection (e.g., 'Malicious' or 'Benign').	|string|
|detailed-label	|A more detailed description or label for the connection.	|string|
