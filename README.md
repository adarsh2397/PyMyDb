# PyMyDb (beta)
A simple python package that acts as wrapper over PyMySQL to simplify the usage of MySQL databases using functions instead of SQL Commands

---

### Table of Contents

<ol>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#prerequisites">Usage</a></li>
  <ol>
  <li><a href="#creating-a-connection">Creating a Connection</a></li>
  </ol>
</ol>

---

### Prerequisites

This is a wrapper package that allows to use MySQL databases in your Python application. There you need to have the following already on your system:

* pip (This is the package installer to install the package)
* MySQL DBMS (Checkout [Digital Ocean - How to install MySQL on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04))
* Python (Currently supports v2.70)

---
### Installation

You can install PyMyDb using `pip` as: `pip install pymydb`

This will install PyMyDb along with PyMySQL which it uses to interact with the database

---

### Usage

Import PyMyDb to your project using: `import pymydb`

#### Creating a Connection

Connect to your database by creating an object of type `pymydb.MySQL`: 

` connection = pymydb.MySQL(host='localhost', user='root', password='root') `


This will create an object called connection that is connected to your MySQL Service but not yet connected to any database. Next we'll see how to use `connection.use()` to connect to a database of your choice.

---

## Things to be done

* Viewing tables
* Add Exception Handling
* Add support to export table as CSV
* Create a complete documentation/wiki
