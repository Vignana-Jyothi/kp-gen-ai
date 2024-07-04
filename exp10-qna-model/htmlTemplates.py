css = """
<style>
    .chat-box {
        max-width: 700px;
        margin: auto;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
    .user-message {
        text-align: right;
        color: #fff;
        background-color: #007bff;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    .bot-message {
        text-align: left;
        color: #000;
        background-color: #e0e0e0;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
"""

user_template = """
<div class="chat-box user-message">
    {{MSG}}
</div>
"""

bot_template = """
<div class="chat-box bot-message">
    {{MSG}}
</div>
"""
