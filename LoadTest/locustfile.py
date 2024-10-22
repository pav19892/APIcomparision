from locust import HttpUser, TaskSet, task, between

NODE_URL = "http://localhost:8012"
FAST_API = "http://localhost:8015"
FLASK_API = "http://localhost:8013"
DJANOG_DRF_API = "http://localhost:8014"


class UserBehavior(TaskSet):
    # Test the Node.js API (http://localhost:8012)
    @task(1)
    def test_nodejs_small(self):
        self.client.get(f"{NODE_URL}/small")

    @task(1)
    def test_nodejs_medium(self):
        self.client.get(f"{NODE_URL}/medium")

    @task(1)
    def test_nodejs_heavy(self):
        self.client.get(f"{NODE_URL}/heavy")

    # Test the Flask API (http://localhost:8013)
    @task(1)
    def test_flask_small(self):
        self.client.get(f"{FLASK_API}/small")

    @task(1)
    def test_flask_medium(self):
        self.client.get(f"{FLASK_API}/medium")

    @task(1)
    def test_flask_heavy(self):
        self.client.get(f"{FLASK_API}/heavy")

    # Test the FastAPI API (http://localhost:8015)
    @task(1)
    def test_fastapi_small(self):
        self.client.get(f"{FAST_API}/small")

    @task(1)
    def test_fastapi_medium(self):
        self.client.get(f"{FAST_API}/medium")

    @task(1)
    def test_fastapi_heavy(self):
        self.client.get(f"{FAST_API}/heavy")

    # Test the Django-DRF API (http://localhost:8014)
    @task(1)
    def test_django_small(self):
        self.client.get(f"{DJANOG_DRF_API}/small")

    @task(1)
    def test_django_medium(self):
        self.client.get(f"{DJANOG_DRF_API}/medium")

    @task(1)
    def test_django_heavy(self):
        self.client.get(f"{DJANOG_DRF_API}/heavy")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Wait between requests (1 to 5 seconds)

