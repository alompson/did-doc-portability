# DID Portability PoC

This project provides a proof-of-concept (PoC) for enabling portability between Decentralized Identifiers (DIDs) using a cross-referencing mechanism in the DID Document layer. In this implementation, we simulate the migration between two DIDs—named "DID_01" (the old DID) and "DID_02" (the new DID)—by modifying the `alsoKnownAs` field in each DID Document to create a verifiable link between them. This PoC uses JWK-formatted keys and a DID method similar to did:ethr.

## Project Structure

|─ main.py # The main Python script containing the logic for creating and modifying DIDs. 

|─ Makefile # Makefile for building and running the project in Docker. 

|─ Dockerfile # Dockerfile for creating the project's containerized environment. 

|─ requirements.txt # List of Python dependencies. |─ README.md # This file.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) must be installed on your system.
- Basic knowledge of Python is helpful.

### Building and Running the PoC

1. **Build the Docker image**

Open a terminal in the project root and run:
```bash
   make build

   Run the Project
```
Start the container using:

```bash
make run
```