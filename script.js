document.addEventListener("DOMContentLoaded", () => {
  const chatMessages = document.getElementById("chat-messages");
  const userInput = document.getElementById("user-input");
  const sendButton = document.getElementById("send-button");

  const botResponses = {
    hello: "Hello! How can I help you today?",
    hi: "Hi there! How can I assist you?",
    "how are you": "I am doing well, thank you! How about you?",
    "what can you do": "I can answer simple questions and have basic conversations.",
    bye: "Goodbye! Have a great day!",
    default: "I'm not sure I understand. Could you try asking something else?"
  };

  function addMessage(message, isUser = false) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(isUser ? "user-message" : "bot-message");

    const messageText = document.createElement("p");
    messageText.textContent = message;
    messageDiv.appendChild(messageText);

    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function getBotResponse(userMessage) {
    const lowerMessage = userMessage.toLowerCase();
    for (const [key, value] of Object.entries(botResponses)) {
      if (lowerMessage.includes(key)) {
        return value;
      }
    }
    return botResponses.default;
  }

  function sendMessage() {
    const message = userInput.value.trim();
    if (message) {
      addMessage(message, true);
      userInput.value = "";

      setTimeout(() => {
        const botReply = getBotResponse(message);
        addMessage(botReply);
      }, 500);
    }
  }

  sendButton.addEventListener("click", sendMessage);
});
