# VerifyDesk — Streamlit edition

Independent, AI-assisted cybersecurity portfolio prototype for Anjalo Theophine Wilson. Fictional suppliers and simulated roles only.

## Upload to GitHub

Create a separate repository named `verifydesk`. Upload these four files into the repository root (top level):

- app.py
- requirements.txt
- verifydesk.html
- README.md

Extract the ZIP first. Do not upload the ZIP itself or place the four files inside an extra folder. Public makes your source visible to everyone; Private keeps source restricted. This package contains fictional data and no credentials.

## Deploy through Streamlit Community Cloud

At https://share.streamlit.io choose Create app and deploy from GitHub. Select your verifydesk repository, branch main, and main file path app.py. If prompted for Python, choose 3.12. Click Deploy. No API keys, secrets or payment details are required. GitHub access and app visibility are managed separately in your accounts.

## Try it

Open Atlas Fleet Parts as Alex. Tick the simulated callback confirmation, write an evidence note, then click Record callback. Switch to Sam, review the activity log and approve with a second note. For a failed fictional verification, reject the request instead. Cedar demonstrates an unusual sender domain and urgent language.

## Implementation

app.py hosts a self-contained HTML/JavaScript interface inside Streamlit using st.iframe. This is an adaptation for Streamlit hosting, not a rewrite of the workflow into Python. The complete UI, styling and workflow source are in verifydesk.html. There is no dependency on the private ChatGPT Site or external JavaScript files. Streamlit is pinned to 1.67.0, the version used for the launcher check.

## Limitations

The workflow remains browser-only. Roles are not authenticated, approvals are simulated, and activity logs are editable. There is no banking connection, real call, payment execution, shared database or audit-grade retention. Browser refresh or iframe reload resets the scenario. The app contains no real supplier data. Never enter personal, confidential or banking information. This app demonstrates a process and does not guarantee prevention of fraud.

A production system would require authenticated users with MFA, server-side authorisation, protected supplier onboarding, append-only audit records, concurrency controls, secure retention and independent security testing.

## Run locally (optional)

Python 3.12 recommended:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Portfolio description

An AI-assisted prototype exploring supplier bank-detail verification. The project compares requests against saved supplier records, highlights review signals, records simulated independent verification and requires a separate demo approver. Includes a request inbox, fictional scenario creation and JSON activity export. Learn and explain the workflow before presenting it as your portfolio work. No customer deployment or measured fraud reduction is claimed.

## Interface v2
Created by Anjalo Theophine Wilson · Independent project demo.
Interactive status cards filter requests; review progress updates after decisions; the four-step walkthrough explains the process.
