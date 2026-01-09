# YouTube Mini OOP CLI Downloader

## Video Demo: url

## Description

YouTube Mini OOP CLI Downloader is a Python-based Command Line Interface (CLI) application that allows users to search, store, and download YouTube videos interactively. This project was created as a CS50P Final Project and is designed using an Object-Oriented Programming (OOP) approach so that the code is easy to maintain, test, and extend.

This application uses the `yt-dlp` library to perform YouTube video searching and downloading, and `tqdm` to display animated progress bars, making the terminal user experience more informative and clean. The entire application flow is built in a modular way with clear separation of responsibilities between the Domain, Repository, Service, and Infrastructure layers.

The main reason this project was designed with a layered and modular folder structure is to apply software engineering best practices learned throughout CS50P, particularly **Object-Oriented Programming, separation of concerns**, and **testability**. Each folder in the project represents a specific responsibility: the `models` layer defines core data objects, `repositories` manage how data is stored and retrieved, `services` contain the application’s business logic, `infrastructure` handles external dependencies such as YouTube and `yt-dlp`, and `utils` provides reusable helper functions for the CLI interface.

By organizing the project this way, the application becomes easier to understand, easier to test with unit tests, and easier to extend in the future (for example, replacing in-memory storage with a database or adding new download features). This structure also reflects real-world software development practices, ensuring that the project is not only functional but also well-structured, scalable, and maintainable.

---

## Main Features

* 🔍 **Search YouTube videos** by keyword
* 📂 **Store search results** in a temporary (in-memory) repository
* 📃 **Display a list of saved videos**
* ⬇ **Download one or multiple videos at once**
* 📊 **Animated progress bar** during search and download processes
* 🧹 **Clear the entire repository**
* 🧪 **Automated testing using pytest**

---

## How to Run the Program

Make sure Python 3.10 or newer is installed.

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the program:

   ```bash
   python project.py
   ```

3. Follow the interactive menu in the terminal:

   ```markdown
   1. Search Video
   2. List saved videos
   3. Download video
   4. Clear repository
   5. Exit
   ```

---

## Project Structure

```graphql
project/
│
├── project.py                 # Main program & required CS50P functions
├── requirements.txt           # Dependency list
├── README.md                  # Project documentation
│
├── models/
│   └── video.py               # Video entity
│
├── repositories/
│   └── memory_repository.py   # Temporary in-memory video storage
│
├── services/
│   ├── search_service.py      # Video search logic
│   └── download_service.py    # Video download logic
│
├── infrastructure/
│   └── yt_dlp/
│       ├── client.py          # yt-dlp wrapper
│       └── options.py         # yt-dlp configuration
│
├── utils/
│   └── cli_helper.py          # CLI helpers (clear screen, pause)
│
├── tests/
│   ├── test_cli.py
│   ├── test_search_service.py
│   ├── test_download_service.py
│   ├── test_memory_repository.py
│   └── test_video.py
│
└── test_project.py            # Tests for required CS50P functions
```

---

## Required CS50P Functions

According to the CS50P specification, this project includes **three additional functions** besides `main()`, all defined directly in `project.py`:

* `search_videos(search_service, keyword, max_results)`
* `list_videos(repo)`
* `download_single_video(download_service, video, path)`

---

## Design & Technical Considerations

* **Object-Oriented Programming (OOP)** is used to separate responsibilities of each component.
* **Dependency Injection** is applied to make the code easy to test without an internet connection.
* **pytest + pytest-mock** are used to ensure all features can be tested automatically.
* **Progress bars are purely visual**, so they do not interfere with business logic and are safe during testing.
* The repository is implemented in-memory for simplicity and speed.

---

## Expected Outcome

* The program can be fully run from the terminal.

* All tests pass successfully by running:

  ```bash
  pytest -v
  ```

* The code is clean, readable, modular, and ready for further development.

---

## Closing Notes

This project was created as a practical exercise to apply Python, OOP, and automated testing in a real-world application. In the future, this application can be extended with additional features such as persistent storage, video quality configuration, or a graphical user interface.

Thank you for reviewing this project!
