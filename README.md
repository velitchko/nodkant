# The following contains the source code to create the edge list and instruction manual for NODKANT

## Server Setup for `index.html`

This guide provides step-by-step instructions to set up a simple web server to host an `index.html` file using Python. This setup is suitable for lightweight testing and development purposes.

---

## Prerequisites

1. **Python**  
   Ensure Python is installed on your system.  
   - For macOS/Linux: Python is usually pre-installed.  
   - For Windows: [Download Python here](https://www.python.org/downloads/).

   Verify installation by running:  
   ```bash
   python --version
   ```

2. Steps to Run the Web Server
Navigate to the Directory
Open your terminal or command prompt and navigate to the directory containing your index.html file:


```bash
cd /path/to/your/directory
```

Start the Web Server
Run one of the following commands depending on your Python version:

For Python 3.x:
```bash
python3 -m http.server 8000
```

For Python 2.x:
```bash
python -m SimpleHTTPServer 8000
```
The server will start and listen on http://localhost:8000.

3. Access the Web Server
Open your browser and go to:
```http://localhost:8000```
