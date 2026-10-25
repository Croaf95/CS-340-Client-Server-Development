## CS 340 Portfolio Reflection

## How do you write programs that are maintainable, readable, and adaptable?

I write maintainable, readable, and adaptable programs by focusing on modular design, clear organization, and thorough documentation. In Project One, I developed a CRUD Python module that separated database operations from the rest of the application. This approach allowed me to reuse the same functionality when building the dashboard in Project Two instead of rewriting database code. By creating a dedicated module, I was able to keep my code organized, easier to debug, and simpler to maintain. If a database operation needed to be updated, I only had to make changes in one location.

One of the biggest advantages of this approach was reusability. The CRUD module served as a bridge between the MongoDB database and the dashboard application, reducing code duplication and improving consistency. In the future, I could reuse this module as the foundation for other applications that require database connectivity, such as web applications, reporting tools, or inventory management systems. Designing code with reusability in mind helps reduce development time and increases software reliability.

## How do you approach a problem as a computer scientist?

When approaching a problem as a computer scientist, I first analyze the requirements and break the problem into smaller, manageable tasks. For the Grazioso Salvare project, I began by understanding the database requirements and how the dashboard would interact with the data. I then designed and tested the CRUD module before building the dashboard components that relied on it. This step-by-step process ensured that each part functioned correctly before integrating everything together.

This project differed from many previous assignments because it required connecting multiple technologies rather than solving a single programming problem. I needed to work with MongoDB, Python, Dash, and data visualization tools while ensuring they communicated effectively. In future projects, I would continue using a structured development process that includes requirement analysis, modular design, testing, and iterative improvement. These strategies help create databases and applications that meet client needs while remaining flexible for future enhancements.

## What do computer scientists do, and why does it matter?

Computer scientists develop systems and applications that help organizations manage, analyze, and use information more effectively. Their work matters because businesses rely on technology to make informed decisions, improve efficiency, and solve complex problems. By designing reliable software and databases, computer scientists transform raw data into meaningful information that organizations can use to achieve their goals.

The Grazioso Salvare dashboard demonstrates how technology can support business operations. The dashboard allows users to quickly filter, visualize, and analyze animal-rescue data without manually searching through large datasets. This saves time, improves accuracy, and provides valuable insights that can support decision-making. Projects like this show how software solutions can help organizations work more efficiently and ultimately better serve their missions.
