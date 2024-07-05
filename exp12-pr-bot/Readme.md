project/
│
├── input_data/
│   └── whatsapp_messages.json
│
├── content_generator.py
│
├── pr_content_generated.json
│
├── pr_content_reviewed.json
│
├── content_regenerator.py
│
└── pr_content_regenerated.json

pip install langchain openai python-dotenv


Run the Server
 source ~/kpenvs/GenAI/bin/activate
 python3 content_generator.py