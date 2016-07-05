
#Git
2016-06-01

Git is a version control system that is widely used for software development and other version control tasks. It is a _distributed revision control system_ (not as Subversion or CVS which are client-server models) with an emphasis on speed, data integrity, and support for distributed, non-linear workflows. Git was created by **Linus Torvalds** in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.

As with most other distributed version control systems, and unlike most client–server systems, every Git working directory is a full-fledged repository with complete history and full version-tracking capabilities, independent of network access or a central server. Like the Linux kernel, Git is free software distributed under the terms of the GNU General Public License version 2.

The main features of Git are:
* Strong support for non-linear development: Git supports rapid branching and merging, and includes specific tools for visualizing and navigating a non-linear development history.
* Distributed development: Like Darcs, BitKeeper, Mercurial, SVK, Bazaar and Monotone, Git gives each developer a local copy of the entire development history, and changes are copied from one such repository to another.
* Compatibility with existing systems/protocols: repositories can be published with HTTP, FTP, rsync or ssh.
* Efficient handling of large projects: Torvalds has described Git as being very fast and scalable, and performance tests done by Mozilla showed it was an order of magnitude faster than some version-control systems, and fetching version history from a locally stored repository can be one hundred times faster than fetching it from the remote server.
* Cryptographic authentication of history: The Git history is stored in such a way that the ID of a particular version (a commit in Git terms) depends upon the complete development history leading up to that commit.
* Toolkit-based design: Git was designed as a set of programs written in C, and a number of shell scripts that provide wrappers around those programs.
* Pluggable merge strategies: As part of its toolkit design, Git has a well-defined model of an incomplete merge, and it has multiple algorithms for completing it, culminating in telling the user that it is unable to complete the merge automatically and that manual editing is required.
* Garbage accumulates unless collected: Aborting operations or backing out changes will leave useless dangling objects in the database. Garbage collection can be called explicitly using `git gc --prune`.
* Periodic explicit object packing: Git stores each newly created object as a separate file. Although individually compressed, this takes a great deal of space and is inefficient. This is solved by the use of packs that store a large number of objects in a single file (or network byte stream) called packfile, delta-compressed among themselves.

There are several Git server services. The most popular ones (or the ones I know) are:
* GitLab: provides a software repository service. It is a web-based ruby-coded Git repository manager with wiki and issue tracking features. GitLab, the company, offers hosted accounts similar to GitHub, but also allows its software to be used on third-party servers.
* GitHub: is a website where copies of Git repositories can be uploaded. It is a Git repository hosting service, which offers all of the distributed revision control and source code management (SCM) functionality of Git as well as adding its own features. Unlike Git, which is strictly a command-line tool, GitHub provides a web-based graphical interface and desktop as well as mobile integration. It also provides access control and several collaboration features such as wikis, task management, bug tracking and other features that can be helpful for projects. It allows collaboration with other people on projects. It does that by providing a centralized location to share the repository, a web-based interface to view it, and features like forking, pull requests distributed revision control, issues, and wikis. It transformed the coding social.
* Bitbucket is a web-based hosting service for projects that use either the Git (since October 2011) or the Mercurial (since launch) revision control systems.

***Tags***: Computer engineering, Software management tools

## Material
* http://gitref.org/
* https://try.github.io/levels/1/challenges/1
* www.github.com
* https://git-scm.com/book/en/v1/Getting-Started

## Books
* Silverman, Richard E. (2013). [Git Pocket Guide](https://www.goodreads.com/book/show/17239270-git-pocket-guide). O'Reilly Media
* Chacon, Scott (2009). [Pro Git](https://www.goodreads.com/book/show/6518085-pro-git). Apress
* Loeliger, Jon (2009). [Version Control with Git](https://www.goodreads.com/book/show/6548113-version-control-with-git). O'Reilly Media
* Hogbin Westby, Emma Jane (2015) [Git for Teams: A User-Centered Approach to Creating Efficient Workflows in Git](https://www.goodreads.com/book/show/25653160-git-for-teams). O'Reilly Media
* Swicegood, Travis (2009). [Pragmatic Version Control Using Git](https://www.goodreads.com/book/show/3649826-pragmatic-version-control-using-git). Pragmatic Bookshelf


