## Setup 
pip install spacy
python -m spacy download en_core_web_sm

For language Translation
pip install transformers torch
pip install sentencepiece transformers torch

For Chat
python3 -m venv rasa-env
source ~/kpenvs/rasa-env/bin/activate




## Parked
Rasa requires python 3.7 to 3.10. But my python version is 3.12
And creating right environment for it is taking considerable time & effort
So I parking the RASA based chat interface. 

sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
    liblzma-dev python-openssl git

pip install rasa


## Sentiment Analysis

```
python3 2_sentiment_analysis.py
```

(base) kp@kuru:~/kp-gen-ai/exp7-nltk$ 
[nltk_data] Downloading package vader_lexicon to /home/kp/nltk_data...
[nltk_data]   Package vader_lexicon is already up-to-date!
Text: I love this product! It's fantastic.
Sentiment: {'neg': 0.0, 'neu': 0.27, 'pos': 0.73, 'compound': 0.8439}

Text: This is the worst service I have ever received.
Sentiment: {'neg': 0.369, 'neu': 0.631, 'pos': 0.0, 'compound': -0.6249}

Text: The movie was okay, not great but not bad either.
Sentiment: {'neg': 0.149, 'neu': 0.487, 'pos': 0.364, 'compound': 0.4728}

Text: I'm extremely happy with my purchase!
Sentiment: {'neg': 0.0, 'neu': 0.539, 'pos': 0.461, 'compound': 0.6468}

Text: The food was terrible and the place was dirty.
Sentiment: {'neg': 0.462, 'neu': 0.538, 'pos': 0.0, 'compound': -0.7184}

## Structured Info extraction
```
python3 3_extract_structured_info.py
```
Text: John Doe paid $29.99 for a book on January 5th, 2023.
Entity: John Doe, Label: PERSON
Entity: 29.99, Label: MONEY
Entity: January 5th, 2023, Label: DATE


Text: The conference will be held in New York on 21st July, 2024.
Entity: New York, Label: GPE
Entity: 21st July, 2024, Label: DATE


Text: Jane Smith purchased a new car for €20,000 on 3rd March 2022.
Entity: Jane Smith, Label: PERSON
Entity: 20,000, Label: MONEY
Entity: 3rd March 2022, Label: DATE


## Langauge translation using Helsinki-NLP/opus-mt

```
python3 4_language_translation.py 
```

Translations to French:
Original: Hello, how are you?
Translated: Bonjour, comment allez-vous?

Original: This is a test sentence.
Translated: C'est une phrase d'essai.

Original: I love programming.
Translated: J'adore la programmation.

Translations to Hindi:
Original: Hello, how are you?
Translated: हैलो, तुम कैसे हो?

Original: This is a test sentence.
Translated: यह एक जाँच वाक्य है.

Original: I love programming.
Translated: मैं प्रोग्रामिंग प्यार.

## Language translation using facebook/mbart-large-50-many-to-many-mmt

```
python3 5_language_translation.py
```

Translations to French:
Original: Hello, how are you?
Translated: Bonjour, vous êtes-vous bien?

Original: This is a test sentence.
Translated: Il s'agit d'une phrase d'essai.

Original: I love programming.
Translated: J'aime la programmation.

Translations to Hindi:
Original: Hello, how are you?
Translated: नमस्ते, आप कैसे हैं?

Original: This is a test sentence.
Translated: यह एक परीक्षा वाक्य है।

Original: I love programming.
Translated: मैं प्रोग्रामिंग को पसंद करता हूँ।


## Text summarisation using facebook/bart-large-cnn

```
python3 6_text_summarize.py 
```
### Input
The story begins in the kingdom of Ayodhya, ruled by the wise and just King Dasharatha. Despite having three queens, Kaushalya, Kaikeyi, and Sumitra, Dasharatha is initially childless and yearns for an heir. His longing for a successor leads him to perform a grand sacrifice, which is a turning point in the epic. This sacrifice is not only a display of his devotion and desperation but also sets the stage for the divine intervention that follows. The gods, pleased with Dasharatha’s devotion, grant him four sons, each born to one of his queens, marking the beginning of a new era in Ayodhya.

To obtain children, Dasharatha performs a grand sacrifice, and soon after, his queens give birth to four sons: Kaushalya bears Rama, Kaikeyi gives birth to Bharata, and Sumitra has twins, Lakshmana and Shatrughna. The birth of these princes brings immense joy and relief to Dasharatha, who sees in them the future of his dynasty. The princes are not only a fulfillment of Dasharatha’s wishes but also symbolize the virtues and divine qualities that will define their lives. As they grow up, each prince displays unique traits and skills, foreshadowing their roles in the epic saga that unfolds.

The four princes grow up to be brave, virtuous, and deeply devoted to each other. Rama, the eldest, is especially beloved and revered by all for his noble character and prowess. His virtues are evident from a young age, earning him the admiration and respect of his family and the people of Ayodhya. Lakshmana, his inseparable companion, shares a special bond with Rama, marked by unwavering loyalty and support. Bharata, known for his righteousness, and Shatrughna, the youngest, are also esteemed for their virtues. Together, the brothers represent the ideal qualities of courage, devotion, and filial piety.

### Output
Summary: The story begins in the kingdom of Ayodhya, ruled by the wise and just King Dasharatha. His longing for a successor leads him to perform a grand sacrifice, which is a turning point in the epic. The gods grant him four sons, each born to one of his queens, marking the beginning of a new era