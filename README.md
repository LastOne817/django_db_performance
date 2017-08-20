# DB Performance test

Load test for different database in django

## Requirements

  - django
  - any database you would test (configure `performance/setting` for each database)
  - locust

## Execution

  - `python3 manage.py runserver`
  - `locust -f load_test.py --host=http://localhost:8000 --no-web -c [number of clients] -r [spawn rate] -n [number of requests] --only-summary`
