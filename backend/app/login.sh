#!/usr/bin/bash
curl -X POST "http://localhost:8000/auth/login" -H "Content-Type: application/json" -d '{"email": "tester@test3.com", "password": "tester1234"}'
