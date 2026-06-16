

const startButton = document.getElementById("start-btn");
const nextButton = document.getElementById("next-btn");
const shareButton = document.getElementById("share-btn");
const homeButton = document.getElementById("home-btn")
const cardsDisplay = document.getElementById("cards-display")
const messageArea = document.getElementById("message-area")

const solutionsButton = document.getElementById("solutions-btn")
const solutionsContainer = document.getElementById("solutions-container");
const solutionsList = document.getElementById("solutions-list");


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
        solutionsButton.style.display = "inline-block"


        renderCards(result.cards, cardsDisplay)
        let solutions = result.solutions

        // Clear previous solutions
        solutionsList.innerHTML = ""

        // Add new solutions to the list
        solutions.forEach(solution => {
            const li = document.createElement("li")
            li.textContent = solution
            solutionsList.appendChild(li)
        })
        
    } else {
        console.error("Error starting game:", response.status)
    }
});


nextButton.addEventListener("click", async () => {
    const response = await fetch('/next')
    if (response.ok) {
        const result = await response.json()
        let solutions = result.solutions
        
        solutionsContainer.style.display = "none";
        solutionsButton.textContent = "Show Solutions";

        renderCards(result.cards, cardsDisplay)

        // Clear previous solutions
        solutionsList.innerHTML = ""
        
        // Add new solutions to the list
        solutions.forEach(solution => {
            const li = document.createElement("li")
            li.textContent = solution
            solutionsList.appendChild(li)
        })

    } else {
        console.error("Error getting next card:", response.status)
    }
});

solutionsButton.addEventListener("click", async () => {
    if (solutionsContainer.style.display === "none") {
        solutionsContainer.style.display = "block";
        solutionsButton.textContent = "Hide Solutions";
    } else {
        solutionsContainer.style.display = "none";
        solutionsButton.textContent = "Show Solutions";
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