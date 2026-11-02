# AI Offer Creator - Real Estate Commando

Revolutionary AI-powered tool for generating strategic real estate offer scenarios.

## Features

- **Dual Mode Interface**: Simple and Advanced modes for different user needs
- **Strategy Selection**: Choose from 5 different offer strategies
- **Weighted Offers**: Control attractiveness of each offer (80/20, 50/50, etc.)
- **Quick Presets**: Subject-To vs Cash, Two Subject-To, Creative Options, Stacked Deck
- **AI-Powered Generation**: Uses GPT-4.1-mini for intelligent offer creation
- **Multiple Export Formats**:
  - On-screen results
  - Branded PDF (with Real Estate Commando branding)
  - Pro PDF (clean, unbranded for seller presentations)
- **Presentation Scripts**: Ready-to-use scripts for presenting offers
- **Investor Notes**: Strategic guidance for negotiations

## Offer Strategies

1. **All Cash** - Traditional cash purchase, fastest and simplest
2. **Subject-To** - Take over existing mortgage payments
3. **Lease Option** - Lease with option to purchase later
4. **Seller Financing** - Seller acts as the bank
5. **Hybrid** - Combination of cash and creative financing

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

```bash
OPENAI_API_KEY=your_openai_api_key
PORT=5000
```

## Running Locally

```bash
python app.py
```

## Deployment

Designed for Railway deployment with automatic scaling.

```bash
railway up
```

## Usage

1. Select two offer strategies
2. Adjust weight sliders to control attractiveness
3. Enter property and seller information
4. Set your investment criteria
5. Generate strategic offers
6. Export as branded or pro PDF

## Technology Stack

- **Backend**: Python Flask
- **AI**: OpenAI GPT-4.1-mini
- **PDF Generation**: ReportLab
- **Frontend**: Vanilla JavaScript with responsive design
- **Styling**: Custom CSS with military tactical aesthetic

## License

Proprietary - Real Estate Commando

## Version

1.0.0 - November 2025

<!-- Trigger redeploy to pick up shared OPENAI_API_KEY variable -->


## Members interface

The existing forms, strategy calculations, AI calls and exports are unchanged. The interface loads bundled members styles from `static/members/`: the members app stylesheet, the business look and `tool.css` for this tool's existing layout. The stylesheet query suffixes are the first 10 characters of each file's SHA-256; refresh them whenever the file changes. The bundle is served locally by Flask, so rendering adds no request to another service.

Check the initial form and results at 1280 and 390 pixels, keyboard focus and reduced motion. Exercise the existing action and PDF buttons against the running app. The deal analyzer also checks each of its 4 strategies. Theme changes do not change environment settings, usage limits or provider credentials.

This repository is connected to Railway production. Updating its deployed branch is a live release; prepare and verify the change before that trigger.
