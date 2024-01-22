# MongoDB Data Generation Script

This Python script generates and inserts over 300 MongoDB documents into a local instance. The documents follow a specific structure with nested routing parameters. Unique keywords are incorporated in the "name" field, creating a dataset for the 'data_set' collection in the 'day22data' database using pymongo.

## Getting Started

These instructions will help you run the script on your local machine.

### Prerequisites

- Python (3.x recommended)
- MongoDB installed and running locally

### Installing Dependencies

Install the required Python packages using the following command:

```bash
pip install pymongo
