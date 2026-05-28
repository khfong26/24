

const startButton = document.getElementById("start-btn");
const nextButton = document.getElementById("next-btn");
const shareButton = document.getElementById("share-btn");
const homeButton = document.getElementById("home-btn")
const cardsDisplay = document.getElementById("cards-display")
const messageArea = document.getElementById("message-area")


// helper function to show cards
// helper function to show cards
function renderCards(cardsArray, containerElement) {
    containerElement.innerHTML = ""; 

    cardsArray.forEach(cardName => {
        const img = document.createElement("img");
        
        // Convert "King of Diamonds" to "king_of_diamonds"
        const safeFileName = cardName.toLowerCase().replace(/ /g, "_");
        
        img.src = `/static/cards/${safeFileName}.png`; 
        img.alt = cardName;
        img.classList.add("card");

        containerElement.appendChild(img);
    });
}

// starts the game and gives first 4 cards
startButton.addEventListener("click", async () => {
    const response = await fetch('/start')
    if (response.ok) {
        const result = await response.json()
        nextButton.style.display = "inline-block"
        shareButton.style.display = "inline-block"
        startButton.style.display = "none"
        homeButton.style.display = "inline-block"


        renderCards(result.cards, cardsDisplay)
    } else {
        console.error("Error starting game:", response.status)
    }
});

nextButton.addEventListener("click", async () => {
    const response = await fetch('/next')
    if (response.ok) {
        const result = await response.json()
        
        renderCards(result.cards, cardsDisplay)
    } else {
        console.error("Error getting next card:", response.status)
    }
});

shareButton.addEventListener("click", async () => {
    const response = await fetch('/share')
    if (response.ok) {
        const result = await response.json()
        await navigator.clipboard.writeText(result.cards);

        // Show a temporary message confirming the share action
        messageArea.textContent = "Numbers copied to clipboard!"
        setTimeout(() => {messageArea.textContent = ""}, 3000);

    } else {
        console.error("Error sharing game:", response.status)
    }
});


homeButton.addEventListener("click", () => {
    window.location.href = "/"
})