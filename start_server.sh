#!/bin/bash
python3.8 -m uvicorn api.main:_get_app --factory --reload --host 0.0.0.0 --port 8000 