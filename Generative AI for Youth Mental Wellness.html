<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MindfulGenie - Youth Mental Wellness</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: #4F46E5;
            color: white;
            padding: 1rem 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            display: flex;
            align-items: center;
        }
        
        .logo span {
            margin-left: 10px;
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-left: 20px;
        }
        
        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
        }
        
        .nav-links a:hover {
            color: #EC4899;
        }
        
        .hero {
            text-align: center;
            padding: 4rem 0;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: #4F46E5;
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 2rem;
            color: #4B5563;
        }
        
        .btn {
            display: inline-block;
            background: #4F46E5;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            font-size: 1rem;
        }
        
        .btn:hover {
            background: #7C3AED;
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background: #EC4899;
        }
        
        .btn-secondary:hover {
            background: #DB2777;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin: 4rem 0;
        }
        
        .feature-card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s;
            text-align: center;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .feature-card h3 {
            margin-bottom: 1rem;
            color: #4F46E5;
        }
        
        .chat-container {
            max-width: 800px;
            margin: 3rem auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .chat-header {
            background: #4F46E5;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        
        .chat-messages {
            height: 400px;
            overflow-y: auto;
            padding: 1rem;
            background: #F9FAFB;
        }
        
        .message {
            margin-bottom: 1rem;
            display: flex;
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message-content {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 18px;
        }
        
        .message.bot .message-content {
            background: #E5E7EB;
            color: #333;
        }
        
        .message.user .message-content {
            background: #4F46E5;
            color: white;
        }
        
        .chat-input {
            display: flex;
            padding: 1rem;
            background: white;
            border-top: 1px solid #E5E7EB;
        }
        
        .chat-input input {
            flex: 1;
            padding: 12px;
            border: 1px solid #D1D5DB;
            border-radius: 24px;
            margin-right: 10px;
            font-size: 1rem;
        }
        
        .chat-input button {
            background: #4F46E5;
            color: white;
            border: none;
            border-radius: 50%;
            width: 48px;
            height: 48px;
            font-size: 1.2rem;
            cursor: pointer;
        }
        
        .disclaimer {
            background: #FEF3C7;
            border-left: 4px solid #F59E0B;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 4px;
        }
        
        footer {
            background: #1F2937;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 4rem;
        }
        
        /* Mood Tracker Styles */
        .mood-tracker {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin: 3rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        
        .mood-tracker h2 {
            color: #4F46E5;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .mood-emojis {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        
        .mood-emoji {
            font-size: 4rem;
            cursor: pointer;
            transition: transform 0.2s;
            padding: 10px;
            border-radius: 50%;
        }
        
        .mood-emoji:hover {
            transform: scale(1.2);
            background: #EDE9FE;
        }
        
        .mood-emoji.selected {
            transform: scale(1.3);
            background: #4F46E5;
            color: white;
        }
        
        .mood-history {
            margin-top: 2rem;
            padding: 1rem;
            background: #F9FAFB;
            border-radius: 8px;
        }
        
        .mood-history h3 {
            color: #4F46E5;
            margin-bottom: 1rem;
        }
        
        .mood-entry {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid #E5E7EB;
        }
        
        .mood-entry:last-child {
            border-bottom: none;
        }
        
        .chart-container {
            margin-top: 2rem;
            height: 300px;
            position: relative;
        }
        
        /* Wellness Tools Styles */
        .wellness-tools {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin: 3rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        
        .wellness-tools h2 {
            color: #4F46E5;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .tool-card {
            background: #F9FAFB;
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
        }
        
        .tool-card h3 {
            color: #4F46E5;
            margin-bottom: 1rem;
        }
        
        .tool-card p {
            margin-bottom: 1rem;
            color: #6B7280;
        }
        
        .breathing-exercise {
            margin: 1.5rem 0;
        }
        
        .breathing-circle {
            width: 120px;
            height: 120px;
            background: #EC4899;
            border-radius: 50%;
            margin: 1.5rem auto;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1rem;
            font-weight: bold;
            transition: all 0.3s;
        }
        
        .breathing-circle.inhale {
            animation: inhale 4s ease-in-out;
        }
        
        .breathing-circle.hold {
            animation: hold 7s ease-in-out;
        }
        
        .breathing-circle.exhale {
            animation: exhale 8s ease-in-out;
        }
        
        @keyframes inhale {
            0% { transform: scale(1); }
            100% { transform: scale(1.5); }
        }
        
        @keyframes hold {
            0% { transform: scale(1.5); }
            100% { transform: scale(1.5); }
        }
        
        @keyframes exhale {
            0% { transform: scale(1.5); }
            100% { transform: scale(1); }
        }
        
        .affirmation {
            font-size: 1.5rem;
            font-style: italic;
            color: #4F46E5;
            margin: 1.5rem 0;
            min-height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        
        .journaling-prompts {
            text-align: left;
            margin: 1.5rem 0;
        }
        
        .journaling-prompts ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        .journaling-prompts li {
            padding: 0.8rem 0;
            border-bottom: 1px solid #E5E7EB;
            position: relative;
            padding-left: 2rem;
        }
        
        .journaling-prompts li:before {
            content: "✍️";
            position: absolute;
            left: 0;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .nav-links {
                display: none;
            }
            
            .features {
                grid-template-columns: 1fr;
            }
            
            .mood-emojis {
                gap: 15px;
            }
            
            .mood-emoji {
                font-size: 3rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">
                🧠 <span>MindfulGenie</span>
            </div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#chat">Chat</a></li>
                <li><a href="#mood">Mood Tracker</a></li>
                <li><a href="#wellness">Wellness Tools</a></li>
            </ul>
        </nav>
    </header>

    <section id="home" class="hero">
        <div class="container">
            <h1>Generative AI for Youth Mental Wellness</h1>
            <p>Your personal AI companion for mental wellness support, available 24/7</p>
            <a href="#chat" class="btn">Start Chatting</a>
        </div>
    </section>

    <div class="container">
        <div class="disclaimer">
            <strong>Important:</strong> MindfulGenie is not a replacement for professional mental health care. If you're in crisis, please call 988 or text HOME to 741741.
        </div>
        
        <section class="features">
            <div class="feature-card">
                <div class="feature-icon">💬</div>
                <h3>AI Chat Companion</h3>
                <p>Talk to our AI companion about your feelings and get supportive responses anytime, anywhere.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Mood Tracking</h3>
                <p>Track your emotions and identify patterns to better understand your mental health journey.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🧘</div>
                <h3>Wellness Tools</h3>
                <p>Access guided meditations, breathing exercises, and mindfulness activities designed for youth.</p>
            </div>
        </section>

        <section id="chat" class="chat-container">
            <div class="chat-header">
                <h2>Chat with MindfulGenie</h2>
                <p>I'm here to listen and support you</p>
            </div>
            
            <div id="chat-messages" class="chat-messages">
                <div class="message bot">
                    <div class="message-content">
                        Hi! I'm MindfulGenie. How are you feeling today?
                    </div>
                </div>
            </div>
            
            <div class="chat-input">
                <input type="text" id="user-input" placeholder="Type your message here...">
                <button id="send-btn">➤</button>
            </div>
        </section>

        <section id="mood" class="mood-tracker">
            <h2>Mood Tracker</h2>
            <p style="text-align: center; margin-bottom: 1rem;">How are you feeling today? Select your mood:</p>
            
            <div class="mood-emojis">
                <div class="mood-emoji" data-mood="happy" data-value="7">😊</div>
                <div class="mood-emoji" data-mood="excited" data-value="6">🤩</div>
                <div class="mood-emoji" data-mood="calm" data-value="5">😌</div>
                <div class="mood-emoji" data-mood="sad" data-value="2">😔</div>
                <div class="mood-emoji" data-mood="anxious" data-value="1">😰</div>
                <div class="mood-emoji" data-mood="angry" data-value="0">😠</div>
                <div class="mood-emoji" data-mood="tired" data-value="3">😴</div>
                <div class="mood-emoji" data-mood="confused" data-value="4">😕</div>
            </div>
            
            <div style="text-align: center;">
                <button id="save-mood" class="btn">Save Mood</button>
            </div>
            
            <div class="mood-history">
                <h3>Your Mood History</h3>
                <div id="mood-entries">
                    <p style="text-align: center; color: #6B7280;">No mood entries yet. Start tracking your mood!</p>
                </div>
                
                <div class="chart-container">
                    <canvas id="moodChart"></canvas>
                </div>
            </div>
        </section>

        <section id="wellness" class="wellness-tools">
            <h2>Wellness Tools</h2>
            
            <div class="tools-grid">
                <div class="tool-card">
                    <h3>Breathing Exercise</h3>
                    <p>Try the 4-7-8 breathing technique to reduce stress and anxiety</p>
                    
                    <div class="breathing-exercise">
                        <div id="breathing-circle" class="breathing-circle">Breathe</div>
                        <button id="start-breathing" class="btn">Start Exercise</button>
                    </div>
                </div>
                
                <div class="tool-card">
                    <h3>Daily Affirmation</h3>
                    <p>Generate a positive affirmation to start your day</p>
                    
                    <div id="affirmation-text" class="affirmation">Click the button below to generate an affirmation</div>
                    <button id="generate-affirmation" class="btn">Generate Affirmation</button>
                </div>
                
                <div class="tool-card">
                    <h3>Journaling Prompts</h3>
                    <p>Reflect on these questions to explore your thoughts and feelings</p>
                    
                    <div class="journaling-prompts">
                        <ul>
                            <li>What are three things you're grateful for today?</li>
                            <li>Describe a challenge you overcame recently</li>
                            <li>What's something that made you smile this week?</li>
                            <li>Write a letter to your future self</li>
                            <li>What does self-care look like for you?</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <footer>
        <div class="container">
            <p>&copy; 2023 MindfulGenie. Created for Generative AI for Youth Mental Wellness.</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Chat functionality
            const chatMessages = document.getElementById('chat-messages');
            const userInput = document.getElementById('user-input');
            const sendBtn = document.getElementById('send-btn');
            
            // Chatbot responses
            const responses = {
                greetings: [
                    "Hi there! How can I support you today?",
                    "Hello! I'm here to listen. What's on your mind?",
                    "Hey! I'm glad you're here. How are you feeling?"
                ],
                feelingSad: [
                    "I'm sorry you're feeling this way. Would you like to talk about what's bothering you?",
                    "It sounds like you're going through a tough time. Remember that feelings are temporary and you're not alone.",
                    "I'm here for you. Let's try a simple breathing exercise together. Inhale for 4 counts, hold for 4, exhale for 6."
                ],
                feelingAnxious: [
                    "Anxiety can be really overwhelming. Let's try grounding: Name 5 things you can see right now.",
                    "I understand anxiety can be paralyzing. Try this: Place your hand on your heart and feel its rhythm. You're safe right now.",
                    "When anxiety strikes, try the 5-4-3-2-1 method: Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste."
                ],
                feelingStressed: [
                    "Stress can feel overwhelming. Let's break it down: What's one small thing you can do right now to feel better?",
                    "I hear that you're stressed. Try this: Tense your muscles for 5 seconds, then release. Notice the difference.",
                    "When stressed, our thoughts can spiral. Try writing down what's worrying you, then ask: 'Is this true? Is this helpful?'"
                ],
                crisis: [
                    "I'm really concerned about you. Please call 988 or text HOME to 741741. I'm here while you wait.",
                    "Your safety is the most important thing. Please reach out to a crisis counselor at 988. You don't have to go through this alone.",
                    "I'm here with you. Please call 988 or text HOME to 741741. You matter and there are people who want to help."
                ],
                default: [
                    "I'm here to listen. Can you tell me more about how you're feeling?",
                    "Your feelings are valid. What would be most helpful for you right now?",
                    "I'm here to support you. What's on your mind today?"
                ]
            };
            
            // Function to add message to chat
            function addMessage(message, isUser = false) {
                const messageDiv = document.createElement('div');
                messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
                messageDiv.innerHTML = `<div class="message-content">${message}</div>`;
                chatMessages.appendChild(messageDiv);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
            
            // Function to get bot response
            function getBotResponse(userMessage) {
                const message = userMessage.toLowerCase();
                
                // Crisis detection
                if (message.includes('suicide') || message.includes('kill myself') || 
                    message.includes('end it') || message.includes('hurt myself') || 
                    message.includes('die') || message.includes('worthless')) {
                    return responses.crisis[Math.floor(Math.random() * responses.crisis.length)];
                }
                
                // Feeling detection
                if (message.includes('sad') || message.includes('depress') || message.includes('cry') || message.includes('lonely')) {
                    return responses.feelingSad[Math.floor(Math.random() * responses.feelingSad.length)];
                }
                
                if (message.includes('anxious') || message.includes('anxiety') || message.includes('panic') || message.includes('worried')) {
                    return responses.feelingAnxious[Math.floor(Math.random() * responses.feelingAnxious.length)];
                }
                
                if (message.includes('stress') || message.includes('overwhelm') || message.includes('pressure')) {
                    return responses.feelingStressed[Math.floor(Math.random() * responses.feelingStressed.length)];
                }
                
                // Greeting detection
                if (message.includes('hi') || message.includes('hello') || message.includes('hey') || message.includes('good morning')) {
                    return responses.greetings[Math.floor(Math.random() * responses.greetings.length)];
                }
                
                // Default response
                return responses.default[Math.floor(Math.random() * responses.default.length)];
            }
            
            // Function to handle sending message
            function sendMessage() {
                const message = userInput.value.trim();
                if (message === '') return;
                
                // Add user message
                addMessage(message, true);
                
                // Clear input
                userInput.value = '';
                
                // Get and add bot response after a short delay
                setTimeout(() => {
                    const botResponse = getBotResponse(message);
                    addMessage(botResponse);
                }, 500);
            }
            
            // Event listeners for chat
            sendBtn.addEventListener('click', sendMessage);
            userInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
            
            // Mood Tracker functionality
            const moodEmojis = document.querySelectorAll('.mood-emoji');
            const saveMoodBtn = document.getElementById('save-mood');
            const moodEntriesContainer = document.getElementById('mood-entries');
            let selectedMood = null;
            let moodChart = null;
            
            // Load mood history from localStorage
            function loadMoodHistory() {
                const moodHistory = JSON.parse(localStorage.getItem('moodHistory')) || [];
                
                if (moodHistory.length === 0) {
                    moodEntriesContainer.innerHTML = '<p style="text-align: center; color: #6B7280;">No mood entries yet. Start tracking your mood!</p>';
                    return;
                }
                
                moodEntriesContainer.innerHTML = '';
                
                // Show last 7 entries
                const recentEntries = moodHistory.slice(-7).reverse();
                
                recentEntries.forEach(entry => {
                    const entryDiv = document.createElement('div');
                    entryDiv.className = 'mood-entry';
                    entryDiv.innerHTML = `
                        <span>${entry.date}</span>
                        <span>${entry.moodEmoji} ${entry.moodName}</span>
                    `;
                    moodEntriesContainer.appendChild(entryDiv);
                });
                
                // Update chart
                updateMoodChart(moodHistory);
            }
            
            // Initialize mood history on page load
            loadMoodHistory();
            
            // Mood emoji selection
            moodEmojis.forEach(emoji => {
                emoji.addEventListener('click', function() {
                    // Remove previous selection
                    moodEmojis.forEach(e => e.classList.remove('selected'));
                    
                    // Add selection to clicked emoji
                    this.classList.add('selected');
                    selectedMood = {
                        emoji: this.textContent,
                        name: this.dataset.mood,
                        value: parseInt(this.dataset.value)
                    };
                });
            });
            
            // Save mood
            saveMoodBtn.addEventListener('click', function() {
                if (!selectedMood) {
                    alert('Please select a mood first');
                    return;
                }
                
                // Get current date
                const now = new Date();
                const dateStr = now.toLocaleDateString();
                
                // Get existing mood history
                const moodHistory = JSON.parse(localStorage.getItem('moodHistory')) || [];
                
                // Add new entry
                moodHistory.push({
                    date: dateStr,
                    moodEmoji: selectedMood.emoji,
                    moodName: selectedMood.name,
                    value: selectedMood.value
                });
                
                // Save to localStorage
                localStorage.setItem('moodHistory', JSON.stringify(moodHistory));
                
                // Reset selection
                moodEmojis.forEach(e => e.classList.remove('selected'));
                selectedMood = null;
                
                // Reload mood history
                loadMoodHistory();
                
                // Show success message
                alert('Mood saved successfully!');
            });
            
            // Update mood chart
            function updateMoodChart(moodHistory) {
                const ctx = document.getElementById('moodChart').getContext('2d');
                
                // Prepare data for chart
                const labels = [];
                const data = [];
                
                // Get last 7 entries
                const recentEntries = moodHistory.slice(-7);
                
                recentEntries.forEach(entry => {
                    labels.push(entry.date);
                    data.push(entry.value);
                });
                
                // Destroy existing chart if it exists
                if (moodChart) {
                    moodChart.destroy();
                }
                
                // Create new chart
                moodChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Mood Level',
                            data: data,
                            borderColor: '#4F46E5',
                            backgroundColor: 'rgba(79, 70, 229, 0.1)',
                            borderWidth: 3,
                            pointBackgroundColor: '#4F46E5',
                            pointRadius: 6,
                            pointHoverRadius: 8,
                            fill: true,
                            tension: 0.4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 7,
                                ticks: {
                                    stepSize: 1,
                                    callback: function(value) {
                                        const moods = ['😠', '😰', '😔', '😴', '😕', '😌', '🤩', '😊'];
                                        return moods[value] || '';
                                    }
                                },
                                title: {
                                    display: true,
                                    text: 'Mood'
                                }
                            },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Date'
                                }
                            }
                        },
                        plugins: {
                            legend: {
                                display: false
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        const moods = ['Angry', 'Anxious', 'Sad', 'Tired', 'Confused', 'Calm', 'Excited', 'Happy'];
                                        return 'Mood: ' + moods[context.parsed.y];
                                    }
                                }
                            }
                        }
                    }
                });
            }
            
            // Wellness Tools functionality
            const breathingCircle = document.getElementById('breathing-circle');
            const startBreathingBtn = document.getElementById('start-breathing');
            const affirmationText = document.getElementById('affirmation-text');
            const generateAffirmationBtn = document.getElementById('generate-affirmation');
            
            // Breathing exercise
            let breathingInterval;
            let breathingPhase = 'inhale';
            let breathingCount = 0;
            
            startBreathingBtn.addEventListener('click', function() {
                if (breathingInterval) {
                    // Stop exercise
                    clearInterval(breathingInterval);
                    breathingInterval = null;
                    breathingCircle.className = 'breathing-circle';
                    breathingCircle.textContent = 'Breathe';
                    startBreathingBtn.textContent = 'Start Exercise';
                    return;
                }
                
                // Start exercise
                startBreathingBtn.textContent = 'Stop Exercise';
                breathingPhase = 'inhale';
                breathingCount = 0;
                
                breathingInterval = setInterval(() => {
                    breathingCount++;
                    
                    if (breathingPhase === 'inhale') {
                        breathingCircle.className = 'breathing-circle inhale';
                        breathingCircle.textContent = 'Inhale...';
                        
                        if (breathingCount >= 4) {
                            breathingPhase = 'hold';
                            breathingCount = 0;
                        }
                    } else if (breathingPhase === 'hold') {
                        breathingCircle.className = 'breathing-circle hold';
                        breathingCircle.textContent = 'Hold...';
                        
                        if (breathingCount >= 7) {
                            breathingPhase = 'exhale';
                            breathingCount = 0;
                        }
                    } else if (breathingPhase === 'exhale') {
                        breathingCircle.className = 'breathing-circle exhale';
                        breathingCircle.textContent = 'Exhale...';
                        
                        if (breathingCount >= 8) {
                            // Reset cycle
                            breathingPhase = 'inhale';
                            breathingCount = 0;
                        }
                    }
                }, 1000);
            });
            
            // Affirmation generator
            const affirmations = [
                "You are stronger than you know",
                "This feeling will pass",
                "You deserve kindness and compassion",
                "Your feelings are valid",
                "You are not alone",
                "You have survived 100% of your hardest days",
                "You are enough just as you are",
                "Every day is a new opportunity",
                "You are capable of amazing things",
                "Your mental health is a priority"
            ];
            
            generateAffirmationBtn.addEventListener('click', function() {
                const randomAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
                affirmationText.textContent = randomAffirmation;
            });
            
            // Smooth scrolling for navigation links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        });
    </script>
</body>
</html>