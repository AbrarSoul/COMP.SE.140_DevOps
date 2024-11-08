# COMP.SE.140 - NGINX Hands-On

## Version History
- **V1.0 (23.10.2024)**: First internal version for course staff
- **V1.1 (24.10.2024)**: Staff feedback
- **V1.2 (28.10.2024)**: Corrected fixes pointed out by students
- **V1.3 (30.10.2024)**: Additional correction

## Synopsis
The task is to add an NGINX gateway and Web interface in front of the previous exercise (Docker Compose hands-on). The gateway will implement basic authentication and load balancing.

## Learning Goals
This exercise aims to teach students:
- Load-balancing, access control, and other gateway functionalities.
- Hands-on experience with NGINX and its integration into applications.

## Task Definition
1. **Service Requirements**:
   - Services 1 and 2 run similarly to the previous exercise, with some modifications:
     - Service 1 has a 2-second delay after responding to a request and cannot respond to another request during this time.
     - Three instances of Service 1 are created.
   
2. **NGINX Setup**:
   - NGINX is added as a service in `docker-compose`, listening on port **8198** (the only exposed port).
   - NGINX acts as a web server; testing is done via a browser.

3. **Load Balancing**:
   - NGINX is configured to distribute requests across the three instances of Service 1, using the default round-robin algorithm.

4. **Basic Authentication**:
   - Basic authentication is configured in NGINX, with a single user initialized.

5. **System Behavior**:
   - Accessing `http://localhost:8198` prompts a login page.
   - On successful login, a new page appears with **REQUEST** and **STOP** buttons, and a text area.
     - Invalid credentials either prompt an error or re-request the login.
   - **REQUEST** button sends a request to one of the Service 1 instances via the load balancer; the response appears in the text area.
   - **STOP** button closes all containers, terminating the `docker compose` process.

## Implementation Notes
This task is challenging, and there is flexibility in the implementation approach. Failure to fully implement will result in minor point deductions.

## Deadlines
Refer to the course Moodle for specific deadlines.

## Submitting for Grading
In the git repository under branch `exercise4`, submit:
- All Dockerfiles and `docker-compose.yaml`
- Source code for the applications
- Output of `docker container ls` and `docker network ls` (while services are running) in `docker-status.txt`
- `login.txt` containing the username and password

Please avoid including extra files. Any git service accessible to course staff without extra effort is acceptable.

**Testing Instructions** (Linux):
```bash
$ git clone -b exercise4 <your_git_url>
$ docker compose up --build
# Wait for 10 seconds
# Open a browser and navigate to http://localhost:8198
$ docker compose down
