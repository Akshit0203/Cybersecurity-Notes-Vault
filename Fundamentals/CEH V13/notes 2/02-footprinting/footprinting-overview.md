# Footprinting overview

- Also known as **fingerprinting** or **reconnaissance**
- 📝 Gathering information about a target system
- E.g. software, network protocols, operating systems or hardware devices.
- End goal is to find a way to break into the system.
- 🤗 Often offered as separate service bought by companies to check against leaks and to see what data is there.
- See also • [Reconnaissance | Hacking stages](../01-introduction/hacking-stages.md#1-reconnaissance) and • [Information Gathering | Penetration testing phases](../01-introduction/penetration-testing-phases.md#information-gathering)

## Footprinting types

### Passive footprinting

- Also known as **passive reconnaissance**, **passive fingerprinting** or **passive information gathering**
- 📝 No direct contact with target
- Rely on information that is publicly available.
- Most difficult to detect
- E.g. • News • job postings • [WHOIS](whois-geoiplocation-and-dns-interrogation.md#whois) databases • government records • document sifting • [dumpster diving | Social engineering](../10-social-engineering/social-engineering-types.md#dumpster-diving) • [competitive analysis](#competitive-intelligence) • browser search • map lookup • DNS lookup • Facebook/Twitter search

#### Open-source intelligence (OSINT)

- 📝 Collection and analysis of information that is gathered from public, or open, sources
- ❗ "Open-source" is unrelated to open-source software or collective intelligence
- Categories: • media • internet • public government data • professional and academic publications • commercial data • grey literature
- [awesome-osint | list of tools](https://github.com/jivoi/awesome-osint), [OsintFramework | graph of tools](https://osintframework.com/)

#### Competitive intelligence

- Also known as **competitive analysis**
- Assessment of the strengths and weaknesses of current and potential competitors
- Tools include
  - Traffic statistics: [Alexa](https://alexa.com)
  - News: [Google finance](https://finance.google.com)
  - Company plans/finances: • [SEC Info](https://www.secinfo.com) • [experian](https://experian.com) • [Market Watch](https://marketwatch.com) • [Wall Street Monitor](https://twst.com) • [EuroMonitor](https://euromonitor.com)
  - Company origins and development: • [EDGAR Database](https://sec.gov/edgar.shtml) • [Hoovers](https://hoovers.com) • [LexisNexis](https://lexisnexis.com) • [Business Wire](https://businesswire.com)

### Active footprinting

- Also known as **active reconnaissance**, **active fingerprinting** or **active information gathering**
- 📝 Direct contact with target including
- Possible for target to be aware e.g. through tasks that may be logged or recorded
- Examples
  - Buying beers for company employees to see what you can extract.
  - Network mapping with `nmap`, perimeter mapping, port scanning, web profiling...
  - • E-mail tracking • Phishing scheme with an email • Querying name servers • File metadata • Social engineering • Extracting DNS information • [Traceroute](network-footprinting.md#traceroute) analysis
- 💡 Easier idea to start with passive footprinting by gathering all publicly available data
  - Then organizing it, and putting in one place.
  - Then use active footprinting with starting probing for ports, networks, possible vulnerabilities etc.
- 💡Good to learn more about stuff (employees) of a company
  - through them you can learn a lot more and gain a lot more access
  - e.g. contact them through social media and start a conversation
    - e.g. join a conference that you see the person is attending on LinkedIn and meet him.

## Footprinting information

- **Network information**
  - Domains, subdomains
  - IP addresses
  - [Whois](whois-geoiplocation-and-dns-interrogation.md#whois) and DNS records
  - VPN firewalls using e.g. [ike-scan](https://github.com/royhills/ike-scan)
- **System information**
  - Web server operating systems
  - Server locations
  - Users
  - Passwords
- **Organization information**
  - Employee information
  - Organization's background
  - Phone numbers
  - Locations

## Footprinting objectives

- **Learn security posture**
  - Analyze security
  - Find loopholes
  - Create an attack plan
- **Identify focus area**
  - Narrow down the range of IP addresses.
- **Find vulnerabilities**
  - Identify weaknesses in the target's security.
- **Map the network**
  - Graphical representation of target's network a guide during the attack.

## Footprinting tools

- Collects and visualizes information e.g. • IP location • routing • business • address • phone number • social security number • source of an email and a file • DNS • domain
- 📝 **[Maltego](https://www.maltego.com/)**
  - Proprietary software for open-source intelligence (OSINT)
  - Provides graphical link for investigative tasks.
- **[Recon-ng (The Recon-ng Framework)](https://github.com/lanmaster53/recon-ng)**
  - Open source CLI tools for open source web-based reconnaissance
- **[FOCA](https://github.com/ElevenPaths/FOCA)**
  - Fingerprinting Organizations with Collected Archives
  - Open-source tool to find metadata and hidden information in the documents:
    1. Finds documents (e.g. PDF, SVG) through search engines or manual upload
    2. Analyze them and identify which documents are created by same team, using which servers/clients.
- **[Recon-dog](https://github.com/s0md3v/ReconDog)**
  - Open-source CLI tool self-claimed as Reconnaissance Swiss Army Knife
  - Can extracts targets from STDIN (piped input) and act upon them
  - Passive reconnaissance tool extracting all information with APIs without any contact with target
- **[Dmitry](https://github.com/jaygreig86/dmitry)** (DeepMagic Information Gathering Tool)
  - CLI tool to analyze a website e.g. `dmitry https://cloudarchitecture.io`
  - • Performs [WHOIS](whois-geoiplocation-and-dns-interrogation.md#whois) lookup on IP and domain • Retrieves [Netcraft](search-engines-and-online-resources.md#netcraft) information • Search for subdomains/email addresses • Performs TCP scanning • Grabs banner for each port

## Footprinting reports

- Includes
  - Details about the performed tests
  - Used techniques
  - Test results
- It should also include
  - List of vulnerabilities and how they can be fixed
    - E.g. wrong configuration in webserver because you're allowing a forward and somebody is using your proxy for reflection attacks.
      - Reflection attack = Send a packet from A to B, A gives wrong source IP for DDoS attacks.
  - List sources of information e.g. DNS, social medial, social engineering.
  - List what information you gathered from each source
    - E.g. login pages, technologies, files, contact details, GPS location, IP address, email servers.
- Should be kept highly confidential

## Countermeasures

- Enforcing security policies
- Educating employees about security threats
  - Raises awareness, reduces risks dramatically
- Encrypting sensitive information
  - 💡 Use proper encryption everywhere
    - 🤗 Many companies uses VPN/proxy with encryption for outside communication, but service communicate with each other without any encryption.
- Disabling protocols that are not required
- Proper service configuration
  - Double check all services that application depends.
  - Do not disable/enable configuration without knowing consequences.
- Scrutinize information released to the public domain
  - E.g. you post on social media which routers the company has just bought
    - Allows hacker to
      - know default router configurations
      - get image of OS in the router and conduct tests in a VM
- Limit site caching
  - Inform search engines what they're supposed to index through e.g. `robots.txt`
    - E.g `User-agent: * Disallow: /` prevents indexing any page (`Disallow: /`) for any crawler (`User-agent: *`)
- Use Whois Guard
- Restricting access to social media
  - Extra risk as you click on many links and giving away companies IP address
