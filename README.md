## 2025 DoD Cyber Sentinel Challenge Writeup

On the morning of June 14 at precisely 11 a.m., the highly anticipated 2025 [DoD Cyber Sentinel Challenge](https://www.correlation-one.com/dod-cyber-sentinel) kicked off. As the clock struck the start time, thousands of participants around the world logged in to face off against a diverse set of [Capture The Flag (CTF)](https://ctf101.org/) problems designed by the Department of Defense. For me, this marked my inaugural foray into CTF competitions—a realm blending creative problem solving, practical cybersecurity skills, and rapid adaptation. Recognizing the steep learning curve ahead, I deliberately mapped out a structured, step-by-step approach. My goal was to build confidence and momentum by first conquering the foundational “easy” tasks, then gradually escalating to medium and hard challenges once I had assimilated key techniques and workflows.

#### Easy Questions

I deliberately began with the easy problems because their hints were both free of cost and provided a gentle introduction to the kinds of puzzles I would see later, guiding me toward the right tools and thought processes. To dissect captured network traffic, I turned to tcpdump, filtering packet captures for suspicious DNS queries, HTTP requests, and unusual payload signatures. For web-based challenges—such as retrieving hidden API endpoints or parsing dynamically generated content—I employed curl alongside simple shell scripting to automate repetitive HTTP GET and POST operations. When faced with binaries, I ran strings to pull out embedded ASCII artifacts, searched for human-readable hints, and identified potential command-and-control structures. With each solved easy flag, I not only added a new technique to my repertoire but also gained the rationale for why one tool worked over another, thereby laying a solid foundation for more intricate puzzles.

#### Medium Questions

Boosted by my success in the easy category, I progressed to medium-level challenges that demanded deeper analysis and sharper deductive reasoning. I made use of two hints—each costing 25 points—hoping they would accelerate my progress. However, these paid hints presupposed more extensive cybersecurity knowledge than I had acquired, so they provided limited tangible benefit. Undeterred, I reverted to the core methods I had mastered: intensive packet analysis via filtered tcpdump sessions, nuanced HTTP request crafting with curl (including custom headers and cookie manipulation), and detailed manual inspection of binary executables using strings in combination with hexdumps. By piecing together clues from log file inconsistencies, unconventional HTTP status codes, and binary section anomalies, I ultimately unraveled every medium challenge. This process reinforced that even in the absence of useful hints, disciplined critical thinking and creative application of familiar tools could bridge the gap.

#### Hard Questions

Upon reaching the hard problems, I encountered obstacles of significantly greater complexity: multi-stage exploits, advanced reverse-engineering tasks, and cryptographic puzzles requiring specialized knowledge well beyond my current skill set. Rather than spin my wheels on blind attempts or risk accruing penalty points, I made the conscious decision to conclude the competition.

#### Lessons Learned

- Start simple to build confidence. Tackling easy challenges first demystified common CTF formats and introduced essential tools in a low-risk context.
- Free guidance is invaluable. The complimentary hints in the easy section accelerated my learning curve and clarified problem structures.
- Hints have context.  Not-free hints proved ineffective on medium problems without deeper domain expertise; deep understanding cannot be shortcut by points.
- Know when to pause. Confronting hard challenges too early can lead to frustration; dedicating time to strengthen fundamentals is a better long-term strategy.
- Document your work for write ups. 

Moving forward, I will continue refining my skill set in cyber security and a build a stronger foundation before my next CTF.

## Solved Problems
Satus|Title|Category|Points|Notes|
|-----|-----|--------|----------|------------|
|<ul><li>- [x] </li></ul>|Secret.txt Society|Web Security|75|PCAP Analysis|
|<ul><li>- [x] </li></ul>|[Field Report Mayhem](https://github.com/h-weng/20025CyberSentinel/blob/main/extract_field_report.py))|Web Security|150|HTTP|
|<ul><li>- [x] </li></ul>|Behind the Beat|Forensics|75|Metadata|
|<ul><li>- [x] </li></ul>|Hidden in Plain Sight|Forensics|75|Metadata|
|<ul><li>- [x] </li></ul>|Cafe Confidential|OSNIT|75|Google Maps|
|<ul><li>- [x] </li></ul>|Problem in North TORbia|OSNIT|150|Tor|
|<ul><li>- [x] </li></ul>|Inspo|OSNIT|200|Google|
|<ul><li>- [x] </li></ul>|Packet Whisperer|Networking|75|Strings|
|<ul><li>- [x] </li></ul>|Hardcoded Lies|Reverse Engineering|75|TCP|
|<ul><li>- [x] </li></ul>|Encoded Evidence|Reverse Engineering|75|Encoding|
